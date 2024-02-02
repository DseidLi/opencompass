import os
import subprocess
import time


kill_type = "parallel"
# 指定目录
directory = f'/mnt/petrelfs/limo/opencompass_fork/configs/needleinahaystack/{kill_type}'

# 列出目录下所有 Python 文件
files = [f for f in os.listdir(directory) if f.endswith('.py')]

# 依次执行每个文件
for file in files:
    command = f'tmux kill-session -t {file.split(".")[0]}'
    subprocess.run(command, shell=True)
    time.sleep(1)
