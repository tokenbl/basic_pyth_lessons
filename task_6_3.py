with open('users.csv', 'r', encoding='utf-8') as user_names:
    with open('hobby.csv', 'r', encoding='utf-8') as users_hobby:

        user_list = []
        for item in user_names:
            user_list.append(item.replace(',', ' ').replace('\n', ''))
        hobby_list = []
        for item in users_hobby:
            hobby_list.append(item.replace('\n', ''))

        names_hobbies = dict(zip(user_list, hobby_list))

        with open('names_hobbies.txt', 'w', encoding='utf-8') as f:
            for key, val in names_hobbies.items():
                f.write('{}: {}\n'.format(key, val))
