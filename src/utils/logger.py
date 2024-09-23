# util_logger.py
import logging
import os
import sys
import time

class Logger:
    def __init__(self, log_path):
        self.log_path = log_path
        if not os.path.exists(self.log_path):
            os.makedirs(self.log_path)
        time_format = "%Y-%m-%d_%H:%M:%S"
        time_str = time.strftime(time_format, time.localtime())