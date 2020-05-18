#-------------*删*-----------


#   集合.remove()
#   删除集合中的指定数据，如果不存在，则报错
A={1, 2, 3, 4}
A.remove(3)
print(A)


#   集合.discard()
#   删除集合中的指定数据，如果不存在，则不报错
B={1, 2, 3, 4}
B.discard(4)
print(B)



#   集合.pop()
#   随机删除集合中的指定数据，然后并返回这个被删除的数据
C={1, 2, 3, 4, "sdf"}
del_hh=C.pop()
print(del_hh)
print(C)