import json
import functions

  
filename ="itemsmod.json"
 
with open(filename) as f:
    #dump of char inventory
    dump = json.load(f)

#type(dump)
#print(dump.keys())
#invetory section
inv='playerInventory'
#char name
name="Rocco"


if name in dump["characterInventories"]:
  
  c = 0
  print('inventory:\n')
  c = functions.printer(dump,name,inv,c)
  print(c)
  
  print('stesh:\n')

  inv='stashInventory'
  functions.printer(dump,name,inv,c)
else:
  print("name error")