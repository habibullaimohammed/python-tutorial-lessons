names = ['John', 'Smith', 'Habib', 'God']
print(names[1])

# Unpacking a list
name1, name2, name3, name4 = names
print(name1, name2, name3, name4)

name5, *name6, name7 = names
print(name5, name6, name7)
