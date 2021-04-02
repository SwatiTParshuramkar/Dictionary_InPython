dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
    } 
temp = [] 
res = dict() 
for key, val  in dic.items(): 
    if key not in temp: 
        temp.append(key) 
        res[key] = val
print(res)