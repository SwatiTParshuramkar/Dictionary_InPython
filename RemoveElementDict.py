# Removing perticular item from Dictionary.using pop().

# CAR_DETAILS={
#     "brand": "Ford",
#     "model": "jason",
#     "year": 1964
# }
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS)

# Removing last item from the Dictionary. using popitem().
# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }
# person.popitem()
# print(person) 


# Deleting perticular item from the dictionary using del().
person={
    'name':'jack',
    'id':22,
    'place':'dharamsala'
}

del person['place']
print(person) 