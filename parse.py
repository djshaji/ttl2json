import sys
import json
from rdflib import Graph

# Create a Graph
g = Graph()

# Parse in an RDF file hosted on the Internet
g.parse(sys.argv [1])

# Loop through each triple in the graph (subj, pred, obj)
label = None
filename = None
print (sys.argv[1])
for subj, pred, obj in g:
    # ~ print (f"subj: {subj} pred: {pred} obj: {obj}")
    # Check if there is at least one triple in the Graph
    if (pred.find ("doap#name") != -1 and label == None):
        label = obj
    if (subj.find ("http://rakarrack.sourceforge.net/effects.html#") == 0):
        filename = subj.split ("#")[1].split (":")[0]
    
    if (subj, pred, obj) not in g:
       raise Exception("It better be!")

# Print the number of "triples" in the Graph
# ~ print(f"Graph g has {len(g)} statements.")
# Prints: Graph g has 86 statements.

# Print out the entire Graph in the RDF Turtle format
j = g.serialize(format="json-ld")
y = json.loads (j)
data = dict ()
for array in y:
    index = -1
    control = dict ()
    for a in array:
        if a == "@id":
            continue
        _key = a.split ('lv2core#')[-1]
        _value = 0
        # ~ print (f"----| {a.split ('lv2core#')[-1]} | ------")
        for b in array [a]:
            # ~ print (b)
            if type (b) == type (data):
                for m in b.keys ():
                    # ~ print (b[m])
                    _value = b[m]
                    if _key == "index":
                        index = _value
                control [_key] = _value
            else:
                control [b.split ("lv2core#")[-1]] = True
    data [index] = control

data [-1]["pluginName"] = label
s = json.dumps (data)
# ~ print (s)
print (filename)
# ~ exit()
f = open (filename + ".json", "w")
# ~ f = open (sys.argv [1].split (".")[0] + ".json", "w")
f.write (s)
f.close ()
