import sys
import json

f = open (sys.argv[1])
lines = f.read ()
f.close ()
print (lines)
j = json.loads (lines)
print (j)
