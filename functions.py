import json

def printer(dump,name,invtp,counter):
  for i in range(len(dump['characterInventories'][name][invtp])): 
    if dump['characterInventories'][name][invtp][i]['isLegendary'] == True:
    
      for j in range(len(dump['characterInventories'][name][invtp][i]['ItemCardEntries'])):
        if str(dump['characterInventories'][name][invtp][i]['ItemCardEntries'][j]['text']) == 'DESC':
          pr_right_way(str(dump['characterInventories'][name][invtp][i]['ItemCardEntries'][j]['value']))
         # print(str(counter)+"."+str(dump['characterInventories'][name][invtp][i]['text'])+""+str(dump['characterInventories'][name][invtp][i]['ItemCardEntries'][j]['value']))
          counter = counter + 1
  return counter

def pr_right_way(str):
  datab="ita_prefix.json"  
  
  with open(datab) as fa:
    file = json.load(fa)
     
  res = str.split("\n");
  iswp = False 
  isarmor = False
  pos = 0
  

  for j in range(len(res)):
    #print(res[j])
    if(isarmor == False) :
      for key, value in enumerate(file["weapon"]):
         if finder(file,"weapon",value,res[j]) == True :
            break
      



#find a string in a dictionary
def finder(dic,tp,perk,st):
    print(st+"=",end="")
    for i in range(len(dic[tp])):  
        if(st == dic[tp][perk][i]["descr"]):
            print(dic[tp][perk][i]["sum"])
            return True
    print()
    return False
