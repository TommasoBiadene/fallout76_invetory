import json


def printer(dump,name,invtp,counter):
  for i in range(len(dump['characterInventories'][name][invtp])): 
    if dump['characterInventories'][name][invtp][i]['isLegendary'] == True:
    
      for j in range(len(dump['characterInventories'][name][invtp][i]['ItemCardEntries'])):
        if str(dump['characterInventories'][name][invtp][i]['ItemCardEntries'][j]['text']) == 'DESC':
          print(str(counter)+"."+str(dump['characterInventories'][name][invtp][i]['text'])+""+str(dump['characterInventories'][name][invtp][i]['ItemCardEntries'][j]['value']))
          counter = counter + 1
  return counter





  
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
  printer(dump,name,inv,c)
  print(c)
  
  print('stesh:\n')

  inv='stashInventory'
  printer(dump,name,inv,c)
else:
  print("name error")