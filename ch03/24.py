# -*- coding: utf-8 -*-

import json
import re

f = open("./jawiki-country.json")

text = json.loads(list(filter(lambda x:json.loads(x)['title'] == 'イギリス', f.readlines()))[0])['text']

media = re.findall('(ファイル|File):(.+(jpg|png|bmp|svg))', text)
for x in media:
    print(x[1])
