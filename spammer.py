#!/bin/python3
import pyautogui as auto
import time
import sys

if len(sys.argv) == 3 :
    try :
        while True:
            auto.write(sys.argv[1])
            auto.press('enter')
            time.sleep(float(sys.argv[2]))
    except KeyboardInterrupt:
        print('\nExitting')
elif len(sys.argv) == 2:
    print('Syntax : python3 spammer.py "The message you want to spam" [delay]')
else:
    print('Syntax : python3 spammer.py "The message you want to spam" [delay]')
