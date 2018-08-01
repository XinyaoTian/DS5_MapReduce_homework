# -*- encoding:utf-8 -*-

import sys

for line in sys.stdin:      # 将给出的txt文件逐行读入
   key_value = line.split(' ',1)
   # 将 key-value 对设计成 用户名-日志信息 这种格式
   # 由于日志这种应用场景，其时间本身就是符合先后顺序的
   # 故只需在shell中调用sort命令对每个用户的分类即可，时间本身就符合先后顺序
   print("%s\t%s"%(key_value[0],key_value[1]))
