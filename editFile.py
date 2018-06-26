import sys
import re
import json
import sys
from itertools import *

for i in range(1,4): 
    servConfFile = sys.argv[i]
    f = open(servConfFile)
    filedata = f.read()
    f.close()
    fixeddata = filedata.replace("german",sys.argv[4])
    f = open(servConfFile, "w")
    f.write(fixeddata)
    f.close()
