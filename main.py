import json
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
    appConfig = loadConfiguration('config.json')
    application = app(appConfig)
    application.run()

if __name__ == "__main__" : 
    main()

    