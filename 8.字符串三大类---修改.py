#-----------------*修改*-------------------

#   字符串序列.replace(旧子串， 新子串， 替换次数)

C="This is your computer and your table"
#   将"your"换成"my"
print(C.replace("your", "my"))



#   split()
#   分割，然后返回一个列表里面的，丢失分割字符
#   字符串序列.split(分割字符， num)
print(C.split("and"))


#---加入的字符或者字符串.join()---
#---合并列表里面的字符串数据为一个大字符串

mylist=["aa", "bbcc"]
print("===".join(mylist))