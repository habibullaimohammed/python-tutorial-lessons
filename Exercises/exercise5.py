budget = float(input('What is your budget? '))
vegetarian = input('Are you vegetarian? (yes/no)').lower()

grocery_list = []

if vegetarian == 'yes':
    grocery_list.append('Tofu')
else:
    grocery_list.append('Chicken breast')

if budget >= 5:
    grocery_list.append('Broccoli')
    budget -= 5

if budget >= 10:
    grocery_list.append('Carrots')
    budget -= 10

if budget >= 15:
    grocery_list.append('Bell pepper')
    budget -= 15

print('Grocery List:', grocery_list)
print('Budget:', budget)