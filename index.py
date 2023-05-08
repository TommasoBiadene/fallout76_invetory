import json


def is_leggendary(ls,i,inv):
  for j in range(len(ls['characterInventories']['Rocco'][str(inv)][i]['ItemCardEntries'])):
    if(str(ls['characterInventories']['Rocco'][str(inv)][i]['ItemCardEntries'][j]['text']) == 'legendaryMods'):
      return True    
  return False
  
  

 
with open('itemsmod.json') as f:
    dump = json.load(f)

#type(dump)
print(dump.keys())

inv='playerInventory'

#for
for i in range(len(dump['characterInventories']['Rocco']['playerInventory'])): 
  if is_leggendary(dump,i,inv):
    for j in range(len(dump['characterInventories']['Rocco']['playerInventory'][i]['ItemCardEntries'])):
      if  str(dump['characterInventories']['Rocco']['playerInventory'][i]['ItemCardEntries'][j]['text']) == 'DESC':
        print(str(i)+"."+str(dump['characterInventories']['Rocco']['playerInventory'][i]['text'])+""+str(dump['characterInventories']['Rocco']['playerInventory'][i]['ItemCardEntries'][j]['value']))

print('stesh')

inv='stashInventory'

for i in range(len(dump['characterInventories']['Rocco']['stashInventory'])):
  if is_leggendary(dump,i,inv):
    for j in range(len(dump['characterInventories']['Rocco']['stashInventory'][i]['ItemCardEntries'])):
      if  str(dump['characterInventories']['Rocco']['stashInventory'][i]['ItemCardEntries'][j]['text']) == 'DESC':
        print(str(i)+"."+str(dump['characterInventories']['Rocco']['stashInventory'][i]['text'])+""+str(dump['characterInventories']['Rocco']['stashInventory'][i]['ItemCardEntries'][j]['value']))

#str(dump['characterInventories']['Rocco']['stashInventory'][i]['ItemCardEntries'][j]['text']) == 'legendaryMods'and
