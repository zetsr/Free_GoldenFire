# monitor.py

import os
import time
import shutil
from datetime import datetime
from config import LOG_FILE, TEMPLATE_FILE, DIRECTORY2, CHECK_INTERVAL
from modify_sav import replace_bytes_in_sav, convert_id_to_hex

def monitor_log_file(log_file, template_file, destination_directory):
    processed_ids = set()  # 已处理的ID集合

    while True:
        if not os.path.exists(log_file):
            print(f"日志文件 {log_file} 不存在。等待文件创建...")
            time.sleep(CHECK_INTERVAL)
            continue

        with open(log_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if "LogOnline: STEAM: Adding P2P connection information with user " in line:
                    parts = line.strip().split()
                    if len(parts) < 9:
                        continue  # 确保有足够的部分

                    steam_id = parts[8]
                    if len(steam_id) != 17 or not steam_id.isdigit():
                        continue  # 过滤不符合格式的ID

                    if steam_id in processed_ids:
                        continue  # 已处理过的ID

                    print(f"检测到玩家连接请求，SteamID: {steam_id}")
                    processed_ids.add(steam_id)

                    # 检查目标目录中是否存在对应的.sav文件
                    sav_file_name = f"{steam_id}.sav"
                    sav_file_path = os.path.join(destination_directory, sav_file_name)

                    if os.path.exists(sav_file_path):
                        print(f"文件 {sav_file_name} 已存在，跳过操作。")
                        continue  # 文件已存在，跳过

                    try:
                        # 复制模板文件并重命名
                        shutil.copy(template_file, sav_file_path)
                        print(f"已复制模板文件并重命名为 {sav_file_name}。")

                        # 进行自定义编码和HEX转换
                        steam_id_hex = convert_id_to_hex(steam_id)
                        # print(f"SteamID HEX编码后: {steam_id_hex}")

                        # 替换.sav文件中的特定字节
                        replace_bytes_in_sav(sav_file_path, steam_id_hex)

                        print(f"文件 {sav_file_name} 处理完成。")

                    except Exception as e:
                        print(f"处理 SteamID {steam_id} 时发生错误: {e}")

        time.sleep(CHECK_INTERVAL)  # 每秒检查一次

if __name__ == "__main__":
    monitor_log_file(LOG_FILE, TEMPLATE_FILE, DIRECTORY2)
