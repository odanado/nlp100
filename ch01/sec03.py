# -*- coding: utf-8 -*-
import re

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

for x in re.split('\W+',s):
    print(len(x))

