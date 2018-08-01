#-*- encoding:utf-8 -*-

str = "A\tB"
print(str.split("\t"))


str = "%s\t%d" % ("hello" , 1)
print(str)

str = "hello the world!"
key_value = str.split(' ',1)
print(key_value)

str = "hello"
print(str[-1])