annual_revenue = float(input('Enter your business annual revenue: '))
no_of_employees = int(input('Enter number of employees: '))
operation_inp = input('Has your business been in operation for at least 2 year? ').capitalize()

if annual_revenue >= 50_000 and no_of_employees >= 3 and operation_inp == 'Yes':
    print('Congrats! You are eligible for a business loan')
else:
    print('Sorry your are not eligible for a business loan. Reason:',)
    if annual_revenue < 50_000:
        print('\tAnnual revenue is less than 50 000')
    if no_of_employees < 3:
        print('\tNo of employees is less than 3')
    if operation_inp != 'Yes':
        print('\tYour business has not been in operation for at least 2 year')

