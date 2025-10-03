uniquota = { "subscribe" : 10000,
              "views" : 500000,
              "likes" : 10001}
print(uniquota["views"])    #view items
uniquota["subscribe"] = 11000 #change value
print(uniquota["subscribe"])

print(uniquota.values())
print(uniquota.keys())

uniquota.pop("likes")
print(uniquota)

uniquota.update({"comment" : 200000})  #updae data
uniquota.update({"dislkes" : 20000})
print(uniquota)
