# assainent operators
a = 10
a = a + 100
a += 100 #short from 
print(a)

# coparision  operators
a = 10
b = 100
 
print(a == b) #equal to 
print(a >= b)
print(a <= b)
print(a != b) #not equal to

#logic operators
print(True and True)
print(True and False)
print(True or False)
print(False or False)
print(not(True))  #ulta ans
print(not(False))

print(1>2 or 2>1)
print(1>2 and 2>1)
print(not(1>2)) #ulta ans

#membership operatur
s = "Adarsha"
s2 = "Ranjiha"

print(("c" in s))
print(("a" in s) and ("a" in s2))
print(("n" in s) or ("n" in s2))
print(not("c" in s))

#Bitwise operator
a = 5 # in binary :101
b = 3 # in binary :011

print(a & b)
print(a | b) #or
print(a ^ b) #xor
print(~a)#Not
print(a << 1) #left shift
print(a >> 1) #right shift
