'''
Created on Dec 19, 2014

@author: ericrudisill
'''
import getopt
import sys
from settings import Settings
import jsonpickle
from cpSerial import CpSerialService
import time

HOST, PORT = "localhost", 1337

def loadSettings(settingsFile=None):
    if not settingsFile:
        settingsFile = "settings.json"
    s = Settings()
    try:
        with open(settingsFile, "r") as f:
            j = f.read()
            s = jsonpickle.decode(j)
    except Exception, ex:
        print ex
        print "Settings file not found. Creating default template file. Add port there."
        with open(settingsFile, "w") as f:
            jsonpickle.set_encoder_options('json', indent=4)
            f.write(jsonpickle.encode(s))
        exit(2)

    s.filename = settingsFile
    
    return s


def main(argv):
    settingsFile = None
    try:
        opts, args = getopt.getopt(argv, "hs:", ["help","settings="])
    except getopt.GetoptError:
        print 'usage: py-serial-dual -s <settingsfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print 'usage: py-serial-dual -s <settingsfile>'
            sys.exit()
        elif opt in ("-s", "--settings"):
            settingsFile = arg
    
    settings = loadSettings(settingsFile)
    print "Loaded settings from " + settings.filename
    print str(settings)

    print "Starting serial service 1"
    serial1 = CpSerialService(settings.cpSerial1)
    serial1.start()
    
    print "Starting serial service 2"
    serial2 = CpSerialService(settings.cpSerial2)
    serial2.start()
    print "Use Control-C to exit."
    
    do_exit = False
    while do_exit == False:
        try:
            time.sleep(0.1)
        except KeyboardInterrupt:
            do_exit = True
         
    serial1.stop()
    serial2.stop()
 
    print "\r\nDone"
    
if __name__ == '__main__':
    main(sys.argv[1:])
