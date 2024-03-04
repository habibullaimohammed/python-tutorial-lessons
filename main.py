# for i in sequence:
#     statement

# range(start, stop, step_size)

names = ['John', 'Smith', 'joe', 'deo']

for i, name in enumerate(names):
    print(i, name)
else:
    print('For loop is done\n')

i = 0
while i < len(names):
    print(i, names[i])
    i += 1