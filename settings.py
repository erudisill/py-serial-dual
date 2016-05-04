'''
Created on Dec 19, 2014
@author: ericrudisill
'''
from cpSerial import CpSerialSettings
import json

class SettingsEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, (Settings, CpSerialSettings)):
            return super(SettingsEncoder, self).default(obj)
        return obj.__dict__
    
    
class Settings(object):

    def __init__(self):
        self.filename = ""
        self.cpSerial1 = CpSerialSettings()
        self.cpSerial2 = CpSerialSettings()
 
    def __str__(self):
        s = "CpSerial1: " + str(self.cpSerial1) + "\r\n" + "CpSerial2: " + str(self.cpSerial2) + "\r\n" 
        return s
