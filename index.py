import json


def is_leggendary(ls,i):
 
  for i in range(len(ls['characterInventories']['Rocco']['stashInventory'])):
    for j in range(len(ls['characterInventories']['Rocco']['stashInventory'][i]['ItemCardEntries'])):
      if(str(ls['characterInventories']['Rocco']['stashInventory'][i]['ItemCardEntries'][j]['text']) == 'legendaryMods'):
        return True
      
  return False
  
  

 
with open('itemsmod.json') as f:
    dump = json.load(f)

#type(dump)
print(dump.keys())

#for
for i in range(len(dump['characterInventories']['Rocco']['playerInventory'])): 
  for j in range(len(dump['characterInventories']['Rocco']['playerInventory'][i]['ItemCardEntries'])):
      if dump['characterInventories']['Rocco']['playerInventory'][i]['damage'] > 0 and str(dump['characterInventories']['Rocco']['playerInventory'][i]['ItemCardEntries'][j]['text']) == 'DESC':
        print(str(i)+"."+str(dump['characterInventories']['Rocco']['playerInventory'][i]['text'])+""+str(dump['characterInventories']['Rocco']['playerInventory'][i]['ItemCardEntries'][j]['value']))

print('stesh')

for i in range(len(dump['characterInventories']['Rocco']['stashInventory'])):
  if is_leggendary(dump,i):
    for j in range(len(dump['characterInventories']['Rocco']['stashInventory'][i]['ItemCardEntries'])):
      #if  str(dump['characterInventories']['Rocco']['stashInventory'][i]['ItemCardEntries'][j]['text']) == 'DESC':
        print(str(i)+"."+str(dump['characterInventories']['Rocco']['stashInventory'][i]['text'])+""+str(dump['characterInventories']['Rocco']['stashInventory'][i]['ItemCardEntries'][j]['value']))

#str(dump['characterInventories']['Rocco']['stashInventory'][i]['ItemCardEntries'][j]['text']) == 'legendaryMods'and
