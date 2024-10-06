# config.py
import os

# 目录配置
DIRECTORY1 = r"C:\server_free_goldenfire\Dragons\Saved\Logs"  # Dragons.log所在目录
DIRECTORY2 = r"C:\server_free_goldenfire\Dragons\Saved\SaveGames\Players"  # 存档文件存放目录
DIRECTORY3 = r"C:\Users\Administrator\Desktop\Free_GoldenFire"  # Dragons_Legacy_GoldenFire.sav所在目录

# 文件路径
LOG_FILE = os.path.join(DIRECTORY1, "Dragons.log")
TEMPLATE_FILE = os.path.join(DIRECTORY3, "Dragons_Legacy_GoldenFire.sav")
SEARCH_STRING = b"PlayerSteamID"

# 检查间隔（秒）
CHECK_INTERVAL = 1