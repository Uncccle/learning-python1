#---------------*删除*------------

#
# #  remove()
# #   移除列表中某个数据
#
# #   列表.remove(数据)
#
# Name=["hhh", "lll", "kakak"]
# Name.remove("hhh")
# print(Name)
#
#
# #   clear()
# #   删除列表中的所有数据
#
# NameA=["hhh", "lll", "kakak"]
# NameA.clear()
# print(NameA)





# #-------------*del*------------
#
# #---del.变量---
# #   删除整个列表
#
# NameB = ["hhh", "lll", "kakak"]
# del NameB
#print(NameB)
#
#
#
# #----del.变量[下标]
# #   删除指定下标的数据
#
# NameC = ["hhh", "lll", "kakak"]
# del NameC[1]
# print(NameC)
#
#
#
# #   变量.pop(下标)
# #   删除指定下标数据，如果删除不指定数据，则删除最后一个数据
# #   无论是删除指定下标数据，还是删除最后一个，他都会返回这个数据
#
NameD = ["hhh", "lll", "kakak"]
del_NameD = NameD.pop()
print(del_NameD)
print(NameD)

NameE = ["hhh", "lll", "kakak"]
del_NameE = NameE.pop(1)
print(del_NameE)
print(NameE)
# #



