import sys
import os

os.system("chmod +x run.sh")
os.system("./run.sh")
os.system("sleep 30")
os.system("./titan-edge bind --hash=CD2CDC28-C8D8-4F03-8D36-64EB2B86A0EB https://api-test1.container1.titannet.io/api/v2/device/binding")
os.system("sleep 1440m")
