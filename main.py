import json
import threading
import time
from job import job
from app import app

def loadConfiguration(cfgFile):
    with open(cfgFile, 'r') as configFile:
        configuration = json.loads(configFile.read())
        jobArr = []
        for jObj in configuration['jobs']:
            newJob = job(jObj['watchdirectory'], jObj['command'], jObj['parameters'])
            jobArr.append(newJob)
        return jobArr

def main():
    stop_threads = False
    appConfig = loadConfiguration('config.json')
    application = app(appConfig)
    t1 = threading.Thread(target=application.run, args=(1, lambda: stop_threads))
    t1.start()
    while (t1.is_alive()):
        if (stop_threads == True):
            continue
        usrMsg = input("")
        if (usrMsg.lower() == "exit"):
            stop_threads = True
    t1.join()
    print("bye bye...")

if __name__ == "__main__" : 
    main()

    