'''#tuple
gender = ("male", "femle", "others")
print(type(gender))
print(gender[0]) #index
print("male" in gender) #membership operator
print(gender.count("male")) #count
print(gender.index("male")) #index

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)

repeated_tuple = (1, 2) * 3
print(repeated_tuple)

#Sets
s = {20 ,2, 12} #sex is uniq ,no index ,no unordered
s2 = set((1,2,3))
print(type(s2))
print(s2)
print(s)
'''
#set operation 
s1 = {1, 2, 3}
s2 = {3 ,4, 5}

print(s1 | s2) #pipe =  | #union
print(s1 & s2) #intesection
print(s1 - s2) #difference
print(s1 ^ s2) #symetrc difference

#Set methos
s = {1, 2, 3}
s.add(4)
#s.remove(10)
s.discard(10)
#s.pop()
a = s.pop()
print(a)
#s.clear() #clear all set