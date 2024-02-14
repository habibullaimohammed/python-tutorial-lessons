# A program to validate user's age for accessing a restricted content

usr_age = int(input('Enter your current age: '))

access_condition = usr_age >= 18
access_condition_2 = usr_age > 0 and usr_age <= 17

is_allowed_age = access_condition and usr_age != 0

parental_control_mesg = 'You must have parental consent to access the content.'

print('Access granted!' * is_allowed_age, 'Access denied!' * (not access_condition), sep='')
print(parental_control_mesg * access_condition_2)
