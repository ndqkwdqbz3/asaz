import sys
import os

os.system("wget https://github.com/Titannet-dao/titan-node/releases/download/v0.1.18/titan_v0.1.18_linux_amd64.tar.gz")
os.system("tar xf titan_v0.1.18_linux_amd64.tar.gz && cd titan_v0.1.18_linux_amd64")
os.system("./titan_v0.1.18_linux_amd64/titan-edge config set --storage-size 200GB")
os.system("nohup ./titan_v0.1.18_linux_amd64/titan-edge daemon start --init --url https://test-locator.titannet.io:5000/rpc/v0  > edge.log 2>&1")
os.system("sleep 30")
os.system("./titan_v0.1.18_linux_amd64/titan-edge bind --hash=CD2CDC28-C8D8-4F03-8D36-64EB2B86A0EB https://api-test1.container1.titannet.io/api/v2/device/binding")
os.system("sleep 1440m")
