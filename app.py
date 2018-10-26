
import time
from os import listdir
from os.path import isfile, join

class app:
    def __init__(self, config):
        self.Jobs = config

    def doJob(self, job):
        files = listdir(job.watchdir)
        for f in files:
            if isfile(join(job.watchdir, f)):
                fullPath = join(job.watchdir, f)
                job.execute(fullPath)

    def run(self):
        while (True):
            for job in self.Jobs:
                self.doJob(job)
            time.sleep(2)

