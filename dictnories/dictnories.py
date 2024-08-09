dictnory = {
    "name": "Ram",
    "age": 23,
    "gender": 'Male'
}

print(dictnory)

print(len(dictnory))


print(dictnory["name"])

print(dictnory.get("age"))

for key in dictnory.keys():
    print(key + ' ' + 'Value is ' + str(dictnory[key]))


dictnory["height"] = "5.10"

print(dictnory)
dictnory.update({"fmovie": "Harry Porter", "factor": "X actor"})

print(dictnory)

dict1 = {}
# dict2=dict1

dict1 = dict1.copy()

dict1['color'] = 'black'

print(dict2)