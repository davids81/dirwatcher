
import os
from os import listdir
from os.path import isfile, join
from datetime import datetime
import subprocess
from logger import log


class job:
    def __init__(self, dir, cmd, params):
        self.watchdir = dir
        self.cmd = cmd
        self.switches = params

    def execute(self, file):
        cmdText = "\"" + self.cmd + "\""
        for p in self.switches:
            cmdText = cmdText + ' ' + p['option'] + ' '
        cmdText = cmdText + "\"" + file + "\""
        FNULL = open(os.devnull, 'w')
        
        message = 'Executing: ' + cmdText + " at: " + datetime.now().strftime('%H:%M:%S %d/%m/%Y ')
        log(message)
        print(message)
        print("")
        subprocess.call(cmdText, stdout=FNULL, stderr=FNULL, shell=False)
