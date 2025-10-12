'''#list

item1 = "bru"
item2 = "sugar"
item3 = "milk"
print(item1, item2, item3)

items = ["bru", "sugar", "milk", "bru2"]
l = [1 , "bru", True, [1,2,3]]
print(l)
print(items)
print(items[0])
print(items[-1])

items.pop()
print(items)

items.pop(0)#remove
print(items)

items.append("mom's magic")#add
print(items)

items.remove("sugar")#remove
print(items)

items.append("mom's magic")#add
print(items)

items.insert(1, "spoon")#add central
print(items)

items[0] = "coffee powder" #change
print(items)                                    #index = position - 1

print(len(items))

items =[1, 23 , 22, 43, 11]

print(sorted(items))

sorted_items = sorted(items)
print(sorted_items) 

print(sum(items))

#common methods

fruits = ["apple", "banana", "cherry", "Mango"]
print(fruits.index("banana")) #index place position

numbers = [1, 2, 3, 1, 1]
print(numbers.count(1))   #count '''

items =[1, 23 , 22, 43, 11]
sorted_items = sorted(items)
rev = sorted_items.reverse() #reverse
print(sorted_items) 

items1 =[1, 23 , 22, 43, 11]
items1.sort()
print(items1)

#Nested list
m = [[1,2], [3,4]]
print(m)
print(m[0][1])