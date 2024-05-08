import sys
import os

os.system("wget https://github.com/Titannet-dao/titan-node/releases/download/v0.1.18/titan_v0.1.18_linux_amd64.tar.gz")
os.system("tar xf titan_v0.1.18_linux_amd64.tar.gz && cd titan_v0.1.18_linux_amd64")
os.system("nohup ./titan_v0.1.18_linux_amd64/titan-edge daemon start --init --url https://test-locator.titannet.io:5000/rpc/v0  > edge.log 2>&1 &")
os.system("sleep 30")
os.system("./titan_v0.1.18_linux_amd64/titan-edge config set --storage-size 250GB")
os.system("./titan_v0.1.18_linux_amd64/titan-edge daemon stop")
os.system("nohup ./titan_v0.1.18_linux_amd64/titan-edge daemon start --init --url https://test-locator.titannet.io:5000/rpc/v0  > edge.log 2>&1 &")
os.system("sleep 30")
os.system("./titan_v0.1.18_linux_amd64/titan-edge bind --hash=F129268E-24E5-48D0-9EB5-68CE157FBD66 https://api-test1.container1.titannet.io/api/v2/device/binding")
os.system("sleep 1440m")
