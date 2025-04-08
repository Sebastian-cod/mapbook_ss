


users=[
    {"name":"Sebastian","location":"Pisz","posts":500},
    {"name":"Michal","location":"Krasnystaw","posts":200},
    {"name":"Krzysztof","location":"Poznań","posts":100},
    {"name":"Bartosz","location":"Ostroleka","posts":300},




]




def get_user_info(users_data: list)->None:
    for user in users:
        print(f"Twój znajomy {user['name']}, z miejscowości: {user['location']} opublikowal {user['posts']} postów)")

        get_user_info(users)