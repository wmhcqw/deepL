import functools
from datetime import datetime


class Logger(object):

    def __init__(self, log_file_path, verbose=3):
        self.log_file_path = log_file_path
        self.log_file = None
        self.verbose = verbose
        self.logs = []

    def open(self):
        self.log_file = open(self.log_file_path)

    def close(self):
        while self.log_file is not None:
            self.log_file.close()
            self.log_file = None
    
    def info(self, msg):
        if msg:
            now = datetime.now()
            msg = f'[INFO] {now.strftime("%Y-%m-%d, %H:%M:%S")}: {msg}'
            self.logs.append(msg)
            if self.verbose > 0:
                self.log_file.write(msg)

    def warn(self, msg):
        if msg:
            now = datetime.now()
            msg = f'[WARN] {now.strftime("%Y-%m-%d, %H:%M:%S")}: {msg}'
            self.logs.append(msg)
            if self.verbose > 1:
                self.log_file.write(msg)

    def error(self, msg):
        if msg:
            now = datetime.now()
            msg = f'[ERROR] {now.strftime("%Y-%m-%d, %H:%M:%S")}: {msg}'
            self.logs.append(msg)
            if self.verbose > 2:
                self.log_file.write(msg)

    def log(self, msg):
        if msg.startswith("_info_"):
            self.info(msg[6:])
        elif msg.startswith("_warn_"):
            self.info(msg[6:])
        elif msg.startswith("_error_"):
            self.info(msg[7:])
        else:
            self.info(msg)

def log(log_path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger = Logger(log_path)
            logger.open()
            logger.log(func(*args, **kwargs))
            logger.close()

            