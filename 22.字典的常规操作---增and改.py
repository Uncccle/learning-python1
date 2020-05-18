#------------*增*-------------

#   写法：字典序列[key]= 值

dict1={"name":"Tom", "age":12, "gender":"male"}
dict1["name"]="sd"  #在修改字典键值对时，如果键有则修改
print(dict1)

dict1["address"]="The Earth" #没有就把新的键值对加入
print(dict1)
