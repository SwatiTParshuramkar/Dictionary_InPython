list1=[1,2,3,1,2,3,4,1,2,3,4,5,6]
d={}
for key in list1:
    if key not in d :
        d[key]=0
    d[key]+=1
print(d)



# name = input("enter your name")
# next1=""
# char=name.split()
# for i in char:
#     if len(next1)>0:
#         next1=next1+" "+i.capitalize()
#     else:
#         next1=i.capitalize()
# print(next1)
