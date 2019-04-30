#!/usr/bin/env python

import sys
import time

def count():

    count = 20

    while True:

        if count < 0:
            print("\r")
            break

        if count < 10:
            string = "[!] Time to paste: %d" % count
            sys.stdout.write(string+ " "+ "\r")
            sys.stdout.flush()
            time.sleep(1)
            count -= 1
            
            
        string = "[!] Time to paste: %d" % count
        sys.stdout.write(string+"\r")
        sys.stdout.flush()
        time.sleep(1)
        count -= 1


