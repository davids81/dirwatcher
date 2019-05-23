

def log(msg):
    with open("usage.log", 'a') as logFile:
        if (not msg.endswith('\n')):
            msg = msg + "\n"
        logFile.write(msg)