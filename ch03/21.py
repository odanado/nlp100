# -*- coding: utf-8 -*-

import json

f = open("./jawiki-country.json")

text = json.loads(list(filter(lambda x:json.loads(x)['title'] == 'イギリス', f.readlines()))[0])['text']

for x in text.split('\n'):
    if 'Category' in x:
        print(x)

