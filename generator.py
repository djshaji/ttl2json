import sys
import json

al = dict ()
base_id = 5001
base = 15000

def print_plugin (filename):
    global base, base_id
    f = open (filename)
    lines = f.read ()
    f.close ()
    j = json.loads (lines)
    data = dict ()
    data ["name"] = j ["-1"]["pluginName"]
    data ["id"] = base_id
    data ["index"] = 0
    data ["library"] = "rkrlv2.so"
    al [base] = data
    base += 1
    base_id += 1

for _f in sys.argv [1:]:
    print_plugin (_f)

print (al)
