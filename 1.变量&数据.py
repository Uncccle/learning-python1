# 变量名 = 值


# 每一个值就是数据，也就是说每一个值对应的就是一个数据类型

# 数据分为数据类型

# 数据类型分为：
#               1.字符串(string)       A="啦啦" / "hhhh"
#               2.整型(int)            A=2 / 10
#               3.浮点数(float)        A=1.1 / 0.2
#               4.列表(list)           A=[1, 2, 3, 4, 5]
#               5.元组(tuple)          A=(1, 2, 3, 4, 5)
#               6.集合(set)            A={1, 2, 3, 4, 5}
#               7.字典(dict)           A={"Name":"Tony", "Age": 12, "Gender":"male"}
#               8.布尔(bool)           A= True or False
def tea(a, b):
    print(a+b)
    return a * b

print(type(tea(3, 4)))

def tea(a, b):
    print(a+b)
    # return a * b

print(type(tea(3, 4)))

def select_func():
     print('-----请选择功能-----')
     print('查询余额')
     print('存款')
     print('取款')

     return print('-----请选择功能-----')
print(type(select_func()))



