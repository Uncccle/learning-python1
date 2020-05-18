#   需求： 三个办公室，八个老师。
#         将八个老师随机分配到三个办公室里面

import random

teachers = ["王老师", "李老师", "张老师", "周老师", "黄老师", "苏老师", "吴老师", "汪老师"]
officers = [[], [], []]

for name in teachers:
    num = random.randint(0, 2)
    officers[num].append(teachers)
print(officers)

i=1
for office in officers:
    print(f'办公室{i}的人数{len(office)}')
    for name in teachers:
        print(name)
    i += 1