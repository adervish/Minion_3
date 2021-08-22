#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import os

GPIO.setwarnings(False)

wifi=22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(wifi, GPIO.OUT)
GPIO.output(wifi, 0)
time.sleep(4)
# Alex commented out this 
#os.system("sudo shutdown now")
