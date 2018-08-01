# -*- encoding:utf-8 -*-
import sys

for line in sys.stdin:      # 将给出的txt文件逐行读入
    # 注意strip()函数排除空格，要不然就会有一堆空格干扰输出结果
    last_letter = line.strip()[-1]
    # 标准输出
    print("%s\t%d"%(last_letter,1))

# import sys
# i = 0
# for line in sys.stdin:
#     i = i + 1
#     line = line.strip().split(',')
#     for item in line:
#         word = str(i) + item[-1]
#         print('%s\t%s' %(word,str(1)))