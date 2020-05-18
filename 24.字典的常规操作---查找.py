#------------*查找*------------


dict1={"name":"Tom", "age":12, "gender":"male"}
print(dict1["age"])




#   字典.get(键， 默认值)
dict2={"name":"Tom", "age":12, "gender":"male"}
print(dict2.get("gender", 100))
#如果键不存在，则返回的是默认值




#   字典.keys()
#   返回的是字典里面的键
dict3={"name":"Tom", "age":12, "gender":"male"}
print(dict3.keys())


#   字典.values()
#   返回的是字典里面键所对应的值
dict4={"name":"Tom", "age":12, "gender":"male"}
print(dict4.values())

#   字典.items()
#   返回的是一整个以列表形式的字典键值组合而成的元组
dict5={"name":"Tom", "age":12, "gender":"male"}
print(dict5.items())
#   返回的：dict_items([('name', 'Tom'), ('age', 12), ('gender', 'male')])
