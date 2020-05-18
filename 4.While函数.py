#-------While循环--------
#其作用：控制代码重复执行


#---While语法---
a=0
while a <= 9:
    print(a)
    a += 1


#---While循环嵌套语法---
#-----九九乘法表-----
b=1
while b <= 9:
    c=1
    while c <= b:
        print(f'{b}*{c}={b*c}', end="\t")
        c += 1
    print()
    b += 1

# break ----退出整个循环
# continue----退出本次循环，继续执行下一个重复执行的代码



#---else---(在while函数当中也可以使用)-----------
# 当正常循环结束后，执行的代码。
c=0
while c <= 8:
    print(c)
    c += 1
else:
    print("系统结束")
