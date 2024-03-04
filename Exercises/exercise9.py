print("Social media")

social_media_posts = []

while True:
    username = input("Enter your username: ").lower()
    options = ('\n1. Create Post.',
               '2. Display All Posts.',
               '3. Display a User\'s Posts.',
               '4. (or any other number): Quit')

    for option in options:
        print(option)

    try:
        option = int(input("\nSelect your option: "))
    except ValueError:
        print("Not a number")

    if option == 1:
        title = input("Enter your title: ")
        description = input("Enter your description: ")

        post = {'title': title, 'description': description, 'username': username}
        social_media_posts.append(post)
        print(social_media_posts)
        print('Post created.')
    elif option == 2:
        print('Posts:')
        for post in social_media_posts:
            print('------------------------------------------')
            print(post['username'], post['title'], post['description'])
            print('------------------------------------------')
    elif option == 3:
        username = input("Enter your username: ").lower()

        print('User\'s post:')
        for post in social_media_posts:
            if post['username'] == username:
                print(post['username'], post['title'], post['description'])

    else:
        break
