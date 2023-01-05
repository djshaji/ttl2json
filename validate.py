import sys
import json

f = open (sys.argv[1])
lines = f.read ()
f.close ()
j = json.loads (lines)
i = False
o = False
for key in j:
    if ("AudioPort" in j[key] and "InputPort" in j [key]):
        i = True
    if ("AudioPort" in j[key] and "OutputPort" in j [key]):
        o = True

if (not i):
    print ("No input port in " + sys.argv [1])
if (not o):
    print ("No output port in " + sys.argv [1])
