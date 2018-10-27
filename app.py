
import time
import sys
from os import listdir
from os.path import isfile, join
from datetime import datetime

class app:
    def __init__(self, config):
        self.Jobs = config

    def doJob(self, job):
        files = listdir(job.watchdir)
        for f in files:
            if isfile(join(job.watchdir, f)):
                fullPath = join(job.watchdir, f)
                job.execute(fullPath)

    def run(self, id, stop):
        start = time.time()
        while (True):
            for job in self.Jobs:
                self.doJob(job)
            print('     pulse: ' + datetime.now().strftime('%H:%M:%S'), end='\r')
            while (time.time() - start < 7):
                if (stop()):
                    print("background watch exited")
                    return
                time.sleep(.5)
            start = time.time()


