gym1 = set()
gym2 = set()

while True:
    gym_number = int(input("What's gym details do you need "))
    if gym_number > 2:
        try:
            raise TypeError("Only integers are allowed")
        except Exception as e:
            print(str(e))

        break

    is_gym1 = gym_number == 1

    options = ('\n',
               '1. Add member.',
               '2. Remove member.',
               '3. Display common members in Gym1 & Gym2.',
               '4. Check if the gym is a subset of the other gym.',
               '5. Check if the gym is a superset of the other gym.',
               '6. Display all members of both Gyms.',
               '7. Exclusive members of the Gyms.',
               '8. (or any other number). Quit')
    for option in options:
        print(option)

    option = int(input("\nSelect an option: "))

    if option == 1:
        member_name = input("What's your full name? ").capitalize()
        if is_gym1:
            gym1.add(member_name)
        else:
            gym2.add(member_name)
    elif option == 2:
        member_name = input("What's your full name? ").capitalize()
        if is_gym1:
            gym1.remove(member_name)
        else:
            gym2.remove(member_name)
    elif option == 3:
        common_members = gym1.intersection(gym2)
        print('Common members: ')
        for member in common_members:
            print(member)
    elif option == 4:
        if is_gym1:
            if gym1.issubset(gym2):
                print('Gym1 is a subset of gym2.')
            else:
                print('it is not a subset of the other gym')
        else:
            if gym2.issubset(gym1):
                print('Gym2 is a subset of gym1.')
            else:
                print('it is not a subset of the other gym')
    elif option == 5:
        if is_gym1:
            if gym1.issuperset(gym2):
                print('Gym1 is a superset of gym2.')
            else:
                print('it is not a superset of the other gym')
        else:
            if gym2.issuperset(gym1):
                print('Gym2 is a superset of gym1.')
            else:
                print('it is not a superset of the other gym')
    elif option == 6:
        members = gym1.union(gym2)
        print('All members:')
        for member in members:
            print(member)
    elif option == 7:
        if is_gym1:
            exclusive_members = gym1.difference(gym2)
            print('Exclusive Members:')
            for member in exclusive_members:
                print(member)
        else:
            exclusive_members = gym2.difference(gym1)
            print('Exclusive Members:')
            for member in exclusive_members:
                print(member)
    else:
        break
