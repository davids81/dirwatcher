
import os
from os import listdir
from os.path import isfile, join
import subprocess

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
        print('Executing: ' + cmdText)
        print("")
        #subprocess.call(cmdText, stdout=FNULL, stderr=FNULL, shell=False)
