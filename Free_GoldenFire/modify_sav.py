# modify_sav.py
from config import SEARCH_STRING

def convert_id_to_hex(steam_id):
    # 将Steam ID转换为整数，然后转换为十六进制字符串
    return steam_id.encode('utf-8').hex()

def replace_bytes_in_sav(file_path, replacement_hex):
    replacement = bytes.fromhex(replacement_hex)
    
    with open(file_path, "rb") as f:
        data = f.read()
    
    # 查找所有"PlayerSteamID"的位置
    positions = []
    start = 0
    while True:
        pos = data.find(SEARCH_STRING, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + len(SEARCH_STRING)
    
    # 定位第一个"PlayerSteamID"后的第31个HEX字节并替换
    first_position = positions[0] + len(SEARCH_STRING) + 30
    data = data[:first_position] + replacement + data[first_position + len(replacement):]
    
    # 将修改后的数据保存回文件
    with open(file_path, "wb") as f:
        f.write(data)
    
    print(f"文件 {file_path} 已成功修改。")
