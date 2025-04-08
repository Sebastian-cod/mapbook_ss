


users=[
    {"name":"Sebastian","location":"Pisz","posts":500},
    {"name":"Michal","location":"Krasnystaw","posts":200},
    {"name":"Krzysztof","location":"Poznań","posts":100},
    {"name":"Bartosz","location":"Ostroleka","posts":300},




]


for user in users:
    print(f"Twój znajomy {user['name']}, z {user['location']} opublikowal {user['posts']} postów)")
