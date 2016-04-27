# -*- coding: utf-8 -*-

import json
import re

f = open("./jawiki-country.json")

text = json.loads(list(filter(lambda x:json.loads(x)['title'] == 'イギリス', f.readlines()))[0])['text']

print("\n".join(re.findall("\[\[Category:(.*)\]\]", text)))

