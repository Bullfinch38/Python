from itertools import zip_longest
import json

with open('user.csv', 'r', encoding='utf-8') as name, open('hobby.csv', 'r', encoding='utf-8') as hobby:
    names = name.read().splitlines()
    hobbys = hobby.read().splitlines()

users_hobby = dict(zip_longest(names, hobbys, fillvalue=None))
# print(users_hobby)
with open('name_hobby.txt', 'w', encoding='utf-8') as f:
    json.dump(users_hobby, f, ensure_ascii=False)
        # f.write(str(users_hobby))
