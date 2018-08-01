# -*- encoding:utf-8 -*-

import sys

for line in sys.stdin:      # 将给出的txt文件逐行读入
    list_person = line.split()  # 针对每一行，将空格切开
    host = list_person[0]       # 记录每一行的第一个人(即关系主人)
    for person in list_person:  # 对于这一行中切割好的所有人
        if person == host:  # 如果是'A' 'A'这种情况
            pass    # 忽略
        else:   # 如果不是'A' 'A'这种情况，比如 'A' 'B'
            print(host + "\t" + person)  # 输出