
users_data = []

def create_user(data):
    users_data.append(data)
    print('user data added successfully!')


def write_user():
    for user in users_data:
        print(user)



create_user({'id':1,'name':'Ali Haider','age':22})

write_user()
    