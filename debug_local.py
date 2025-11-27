# @Time    : 2025/11/27 17:22
# @Author  : xin.he
# @File    : debug_local.py.py
# @Software: PyCharm
# debug_local.py   一键本地模拟 GitHub 环境
import os
os.system("python -m pip install -r requirements.txt")  # 和 GitHub 完全一样的安装命令
os.system("python main.py")  # 或者你实际运行的脚本