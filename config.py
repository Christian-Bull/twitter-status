# basic config

import os.path
import configparser
import tweepy


class Config:
    def __init__(self, configfile):
        self.configfile = configfile

    def readconfig(self):
        if os.path.isfile(self.configfile):
            c = configparser.ConfigParser()
            c.read(self.configfile)

            self.apikey = c['TOKEN']['apikey']
            self.apisecretkey = c['TOKEN']['apisecretkey']
            self.user = c['PARAMS']['user']
            self.count = c['PARAMS']['count']

        else:
            print(self.configfile + " not found")


# reads config file
def loadconfig(file):
    c = Config(file)
    c.readconfig()
    return c


# creates api instance based on parameters set in config
def createapi(configfile):
    # load config
    config = loadconfig(configfile)

    # set variables
    apikey = config.apikey
    apisecretkey = config.apisecretkey

    # # OAuth
    auth = tweepy.OAuthHandler(apikey, apisecretkey)
    api = tweepy.API(auth)

    # returns api instance
    return api
