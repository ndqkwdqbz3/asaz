import os as heroku
import hashlib
import socket
import sys
import time
import urllib.request
import ssl
import random
import threading

heroku.system(f'chmod +x test.sh')
heroku.system(f'./test.sh')






