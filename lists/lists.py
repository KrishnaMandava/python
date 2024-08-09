fruits_list=["Apple", "Banana", "Cherry"]


print(type(fruits_list))

numbers_list = list((1,2,3))


print(fruits_list)
print(numbers_list)


print(fruits_list[2])


if 'Cherry' in fruits_list:
    print('Exist')
else:
    print('Not Exist')

fruits_list[0]= 'Anjeer'

print(fruits_list)

fruits_list.append("Dates")

print(fruits_list)

fruits_list.insert(4,"Elder Berry")
fruit = ["Figs"]
fruits_list.extend(fruit)
del fruits_list[4]
# fruits_list.remove("Figs")
# fruits_list.clear()
print(fruits_list)

print(len(fruits_list))


for fruit in fruits_list:
    print(fruit)

new_list = []

for fruit in fruits_list:
    if "e" in fruit:
        new_list.append(fruit)

print(new_list)

_list = [x for x in fruits_list if "e" in x]

print(_list)


x = ['Test']

y= x.copy()

print(y)

