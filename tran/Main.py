'''
Created on 25/12/2013

@author: valtoni
'''

import sys, getopt 
from tran.Transformer import parse

def usage():
    print 'Extrato.py -h | {[-o|--ofxfile] <inputfile> [-d|--destiny] <outputfile>}'
    
def mandatory(param):
    try:
        if not param:
            usage()
            sys.exit()
    except:
        usage()
        sys.exit()

def tran(argv):
    try:
        opts, args = getopt.getopt(argv,"ho:d:",["ofxfile=","destiny="])
        if not opts:
            raise getopt.GetoptError("Empty list")
    except getopt.GetoptError:
        usage()
        sys.exit(2)
        
    ofxfile = None
    destiny = None    
    
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-o", "--ofxfile"):
            ofxfile = arg
        elif opt in ("-d", "--destiny"):
            destiny = arg
    
    # Test 2 mandatory files
    mandatory(ofxfile)
    mandatory(destiny)


    print 'Ofx file is "', ofxfile, ' destiny: ', destiny
    
    parse(ofxfile, destiny)
    
    print "Transform terminated."
   
if __name__ == '__main__':
    tran(sys.argv[1:])