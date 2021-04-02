name=input("Enter the name")
next1=" "
next_char=True
for char in name:
    if next_char:
        next1 += char.upper()
    else:
        next1+=char
print(next1)


# name = input("Enter a name")
# next1=  " "
# for char in name :
#     if len(next1)>0 :
#         next1+= char.capitalize()
# print(next1)
