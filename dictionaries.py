# thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# # x = thisdict["model"]
# # x=thisdict.get("model")
# x=thisdict.keys()
# print(x)

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.keys()

# print(x)  # before the change


car["color"] = "white"

# print(x)  # after the change

x = car.get("color")
# print(x)

# x=car.values()
# print(x)

y = car["brand"] = "Mercedes"
y2 =car.values()
# print(y2)

x2 = car.items()
print(x2)