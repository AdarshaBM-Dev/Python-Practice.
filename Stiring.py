'''#concatination 
frist_name = "Aadrsha"
Middle_Name = "B"
last_name = "M"
Full_name = frist_name+" "+Middle_Name+" "+last_name
print(Full_name) 

message = "Wornig!"
print(message*100) #repitatin 
print(message.upper()) #big latter
print(message.lower()) #small letter
print(message.strip()*3) #value joint
print(message.replace("Wornig","Error")) #replace value
print(len(message))#length of value
print(type(message))#type of value

#nduction 
name = "Adarsha"
print(name[1]) 
print(name[3:6])
print(name[:6])
print(name[3:])
print(name[-1])
#[start : end : Step or skip]
print(name[::3])
print(name[1:2:3])

S1 = "Adarsha \n its good boy"
S2 = "Adarsha \t its good boy"
print(S1)
print(S2)

#works
name = input("Enter your name : ")
age = int(input("enter your age : "))
print(f"Hello,  {name}! you are {age} years old.")

s = "hello \n \t world \n This a backslck : \ "
print(s)'''

message = input("enter a sentence : ")
print(message.upper())
print(message.lower())
print(message.strip())
print(message.replace("" , ""))
