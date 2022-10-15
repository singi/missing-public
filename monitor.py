#!/usr/bin/python3

import os
import sys
import time
import shutil
import signal
import datetime
import threading
import subprocess

CRASH_DIR = r"./crashes/"
TESTCASE_DIR = r"./testcase"

class crash_monitor():
	def __init__(self):
		if os.path.isdir(CRASH_DIR) != True:
			os.mkdir(CRASH_DIR)
		if os.path.isdir(TESTCASE_DIR) != True:
			os.mkdir(TESTCASE_DIR)

if __name__ == '__main__':
	monitor = crash_monitor()

	#{}/webkit/run-minibrowser 실행
	#크래시 모니터링
	#N sec 마다 kill 후 재실행 or reboot