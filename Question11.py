from collections import Counter
# Dictionary
my_dict = {'T': 23, 'U': 22, 'T': 21,'O': 20, 'R': 32, 'S': 99}
k = Counter(my_dict)
# 3 highest values
high = k.most_common(3)
print("Dictionary with 3 highest values:")
print("Keys : Values")
for i in high:
   print(i[0]," : ",i[1]," ")
   