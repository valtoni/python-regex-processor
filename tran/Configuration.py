'''
Created on 25/12/2013

@author: valtoni
'''

import ConfigParser

def loadexpressions():
    config = ConfigParser.ConfigParser()
    config.read("config.cfg")
    return config.items("transform")