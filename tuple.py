'''#tuple

my_list = [1,2,3,4]
print(my_list)
my_list[0]=10     #update or change
print(my_list)
print(type(my_list))

my_list = [1244,2456,3234,4234]
print(my_list)
my_list[0]=2345     #update or change
print(my_list)
print(type(my_list))

my_list = (1244,2456,3234,4234) # not change any time
print(my_list)
my_list[0]=2345
print(my_list)
print(type(my_list))

my_tuple1 = (1244,2456,3234,4234)
my_tuple2 = tuple((1,2,3,4))
print(my_tuple1)
print(type(my_tuple1))
print(len(my_tuple1))

my_tuple = (1244, "sneha", True, [4234])
print(my_tuple[0])
print(type(my_tuple))
print(len(my_tuple))'''



'''#sets
set{1,2,3,4}
print(set[0])'''

#dictionary
uniqota = { "subscriber" : 10000 ,
            "views" : 500000 }
print(uniqota["subscriber"])
print(uniqota["views"])
print(f"uniquota channel has {uniqota['subscriber']} subscriber and {uniqota['views']} views")
