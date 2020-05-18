#----------------------*查找*(三大类)-----------------------------


#   字符串序列.find(子串， 开始位置下标， 结束位置下标)
C="This is your computer and your table"
print(C.find("your", 15, 30))
#返回给你的是这个变量值的下标(索引)
print(C.find("ddn"))
# 查找不存在的子串时，会返回-1 就表示没有


#   字符串序列.index(子串， 开始位置下标， 结束位置下标)
#   其作用跟find()一样
print(C.index("your", 15, 30))
#   print(C.index("de"))
#   只不过跟find不同的是，在查找不存在的子串时，会报错


#   字符串序列.count(子串， 开始位置下标， 结束位置下标)
#   他返回出来的是子串的个数
print(C.count("your"))
print(C.count("your", 4, 6))
print(C.count("ddhh"))
#   如果找不存在的子串个数，返回出来的就是0

#  rfind()
#   功能和find()一样，只不过方向是从右边开始
#  rindex()
#   功能和index()一样，只不过方向是从右边开始
