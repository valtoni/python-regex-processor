'''
Created on 25/12/2013

@author: valtoni
'''

import re
from tran.Configuration import loadexpressions

def parse(ofxfile, destiny):
    regexs = loadexpressions()
    f = open(ofxfile)
    fd = open(destiny, 'w+')
    
    for line in f:
        actual = line
        for regexp, value in regexs:
            try:
                actual = re.sub(regexp, value, actual, flags=re.IGNORECASE)
            except Exception as e:
                print "Error parsing '{0}': '{1}', actual - '{2}'".format(regexp, e, actual)
        fd.write(actual)
    f.close()
    fd.close()