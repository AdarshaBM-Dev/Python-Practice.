'''products = ['bat','ball']
price = [5000,600]
print(type(products))
print(products)
print(price)
isAvailable = [True,False]
print(isAvailable)'''


'''mixed=[1,'Virat',True,70.343,[12,34,56,32]]
print(mixed)
print(len(mixed))
print(mixed[0])
print(mixed[3])
print(mixed[-1])
print(mixed[4][0])
print(mixed[4][2])

names  = list(('Adarsha','Ranjitha'))
print(names)
print(type(names))

print(mixed)
mixed[0] = 18
print(mixed)
'''

products  = ["mask","shield","covidkit"]
print(products[0])

products  = ["mask","shield","covidkit","energydrink"]
'''products[1] = "faceshield"
print(products[1:])
print(products[1:2])
print(products[1:3])
products[1:3]=["faceshield","kit"]'''
#remove element .pop()
products.pop()
#products.pop(2)
#products.remove("mask")
products.insert(1, "spray")
products.insert(-1,"python")
#insert element-  .insert(index, "vaue")
products.insert(len(products),'python')
print(products)

