dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
# dic2.update(dic3)
# dic2.update(dic1)
for i, j in dic1.items():
    for k,l in dic2.items():
        
        if i==k:
       f     dic4[i]=j+l
    print(dic4)


            
# print(dic4)
# dic1.update(dic3)
# print(dic1)
# dic1.update(dic4)
# dic1.update(dic2)
# print(dic1)
# dic4=dict()
# 
