# basic config

import os
import configparser
import tweepy
import sqlite3


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
            self.url = c['PARAMS']['URL']
            self.database = c['DATABASE']['file']

        else:
            print(self.configfile + " not found")


# reads config file
def loadconfig(file):
    c = Config(file)
    c.readconfig()
    return c


# creates api instance based on parameters set in config
def createapi(configobject):

    # OAuth
    auth = tweepy.OAuthHandler(
        configobject.apikey,
        configobject.apisecretkey
    )
    api = tweepy.API(auth)

    # returns api instance
    return api


# converts data into list
def loaddata(src):
    with open(src, newline='') as f:
        data_list = f.read().split('\n')
        return data_list


# db connection
def connectdb(db_file):
    conn = sqlite3.connect(db_file)
    return conn
