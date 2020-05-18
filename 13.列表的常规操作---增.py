#--------------*列表的常规操作---增*-------------


#   append()
#   列表结果追加数据

#   列表序列.append(数据)
#   作用：增加指定数据到列表中

Name=["hhh", "lll", "kakak"]
Name.append("uuu")
print(Name)



#   extend()
#   列表结果追加数据

#   列表序列.extend(数据)
#   作用：增加指定数据到列表中

Name.extend("uuu")
print(Name)
#如果追加一个字符串，则会将字符串逐字拆开


Name.extend(["uuu", 777])
print(Name)
#所以如果想加入一个字符串，又不想字符串被拆开，就得用列表的形式
# 因为列表形式拆开  就是一整个字符串



#  insert()
#   指定位置新增数据

#   列表.insert(下标， 数据)
Name1=["hhh", "lll", "kakak"]
Name1.insert(1, "sdhf")
print(Name1)

num = 10


def my_func():
    num = 20
    print("my_func: %d" % num)


print("start: %d" % num)
II=my_func()
print(II)



