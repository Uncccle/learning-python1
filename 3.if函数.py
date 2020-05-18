#------if函数------

# 第一种：(if语句语法)
a=int(input("请输入号码"))
if a < 10:
    print("哈哈哈")

# 第二种: (if...else...)
b=int(input("请输入号码"))
if b < 7:
    print("嘎嘎嘎")
else:
    print("啊啊啊")

# 第三种: (多重判断)

c=int(input("请输入号码"))
if c < 10:
    print("咔咔咔")

elif c < 20:
    print("啦啦啦")

else:
    print("嘻嘻嘻")

# 第四种： (if的嵌套)
# 需求: 当你上公交车后，付钱就上车，不付钱就下车；上车后有座位就坐，没座位就站着。

A=int(input("请投币"))
if A == 1:
    print("请上车")
    B=int(input("是否有座位"))
    if B == 1:
        print("请坐")
    else:
        print("站着")
else:
    print("下车")


# 第五种：(三目运算符)
# 条件成立的表达式 if 条件 else 与条件相反的表达式
D=int(input("请输入号码"))
E="啪啪啪"if D < 5 else "呀呀呀"
print(E)










