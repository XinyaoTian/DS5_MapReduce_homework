# -*- encoding:utf-8 -*-
# 载入需要用的库
from operator import itemgetter
import sys

current_letter = ""
count = 0

for line in sys.stdin:
    letter_count = line.strip().split("\t")
    letter = letter_count[0]
    count = int(letter_count[1])

    try:
        count = int(count)
    except ValueError:
        continue
    # 避免输出 "" 1
    if current_letter != letter:
        if current_letter is "":
            current_letter = letter
            count = 1
            pass
        else:
            # 该换current_letter前，先输出上一个letter
            print("%s\t%d"%(current_letter,count))
            current_letter = letter
            count = 1
    else :
        count += 1

# 别忘记最后一个letter
print('%s\t%d' % (current_letter, count))