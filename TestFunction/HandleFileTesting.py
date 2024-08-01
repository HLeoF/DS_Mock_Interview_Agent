import time
import unittest

import os, inspect,sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(current_dir)
sys.path.append('../')
    
from Module.HandleFile import *

class TestHandleFileFunctions(unittest.TestCase):

    def test_create_timestamp_function(self):
        h = HandleFile()
        self.assertTrue(abs(h.create_timestamp.invoke({"input":""}) - int(time.time()*1000) < 1000))
        

if __name__ == '__main__':
    unittest.main()
    