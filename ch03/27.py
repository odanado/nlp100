# -*- coding: utf-8 -*-

import json
import re

f = open("./jawiki-country.json")

text = json.loads(list(filter(lambda x:json.loads(x)['title'] == 'イギリス', f.readlines()))[0])['text']

base_info = {}
for x, y in re.findall("\|(.+) = (.+)", text):


    for quote in re.findall("'+", y):
        if len(quote) % 2 == 1:
            y = re.sub(quote, '', y)

    # 内部リンクを抽出する
    # 正規表現わからない．つらい
    for z in re.findall("(\[\[([^\]]+)\]\])", y):
        y = y.replace(z[0], z[1].split('|')[-1])

    base_info[x] = y

print(base_info)

