thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
del thislist[5]
print(thislist)
thislist.clear()
print("This is what the clear will do:",thislist)