# -*- coding: utf-8 -*-

f = open("./hightemp.txt")
lines = list(f)
col1 = open("col1.txt", "w")
col2 = open("col2.txt", "w")

# \nを付けない方法はあるのか
col1.writelines([x.split()[0] + '\n' for x in lines])
col2.writelines([x.split()[1] + '\n' for x in lines])

