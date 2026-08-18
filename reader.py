import os

def readf(name):
    return open(os.path.join("/data", name)).read()
