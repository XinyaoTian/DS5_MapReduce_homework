# -*- encoding:utf-8 -*-
# 载入需要用的库
from operator import itemgetter
import sys

# 由于mapper阶段人际关机已经是 A\tB 这种格式
# 比如 A\tB 和 A\tC 这两组关系
# 只需要判断：当前主关系是否仍为A；若是，则 B和C 都认识A
# 这是一个典型的reduce应用，即判定和记录相邻的键值对。

# 用于记录当前判定的用户
current_host = ""
# 用于记录用户朋友们的列表
current_host_friends = []

# 按行读入
for line in sys.stdin:
    line = line.strip() # 切分
    host_friend = line.split('\t') # 切分字符串中的\t，使之变为类似['A','B']这样的格式，并使用host_friend记录
    if current_host == host_friend[0]:  # 若现在判定的还是同一个人的朋友们
        if len(current_host_friends) is not 0:  #若朋友list不为空(其实根据下面的逻辑这个list一定不为空)
            for person in current_host_friends: # 对于list中host的所有朋友们
                print(host_friend[1] + ',' + person + '\t' + current_host) # 输出list中host的朋友与当前朋友都认识A
        current_host_friends.append(host_friend[1]) #把当前朋友加入到list中，为下次判定做准备
    else:   # 如果当前主人不再是上一个host了，比如由A变为B了
        current_host = host_friend[0]   # 将当前判定主人置换为新的(比如置换为B)
        current_host_friends.clear()    # 清空上一个人的人际关系网
        current_host_friends.append(host_friend[1])     # 把这个人的第一个朋友加入list


