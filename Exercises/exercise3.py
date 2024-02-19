# A program to validate user's age for accessing a restricted content

usr_age = int(input('Enter your current age: ')) # Converted User value from string to integer.

access_condition = usr_age >= 18
access_condition_2 = usr_age <= 17

parental_control_mesg = 'You must have parental consent to access the content.'

print('Access granted!' * access_condition, 'Access denied!' * (not access_condition), sep='')
print(parental_control_mesg * access_condition_2)
