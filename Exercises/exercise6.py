names = ['Rivan', 'ranan', 'habib', 'John', 'rufus', 'God']

for name in names:
    for letter in name:
        if letter == 'r' or letter == 'R':
            print(name)
            continue

# names_with_r = []
#
# for name in names:
#     if 'r' in name.lower():
#         names_r.append(name)
#
# print(names_r)
