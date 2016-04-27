# -*- coding: utf-8 -*-

import json
import re

f = open("./jawiki-country.json")

text = json.loads(list(filter(lambda x:json.loads(x)['title'] == 'イギリス', f.readlines()))[0])['text']

sections = re.findall('={2}.*={2}', text)
for section in sections:
    print("%d %s" % (section.count('=') / 2 - 1, section))
