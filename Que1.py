# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# # dic3={5:50,6:60}
# dic4={}
# for x,y in dic1.item():
#     for i,j in dic2.item():
#         dic4[i]=(y+j)
        

# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic4=dict()
# for i, j in dic1.items():
#     for k,l in dic2.items():
#         if i==k:
#             dic4[i]=j+l
            
# print(dic4)
# dic1.update(dic3)
# print(dic1)
# dic1.update(dic4)
# dic1.update(dic2)
# print(dic1)



from collections import Counter
dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
d = Counter(dic3) + Counter(dic2) + Counter(dic1)
print(d)


# # Iterating through a Dictionary
# # key = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# # for i in key:
# #        print(key[i])
         