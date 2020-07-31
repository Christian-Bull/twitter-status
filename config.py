# basic config

import os.path
import configparser

def loadConfig(file):
    # checks to ensure file is present
    if os.path.isfile(file):
        config = configparser.ConfigParser()
        config.read(file)
        return config
    else:
        print(file + " not found")
