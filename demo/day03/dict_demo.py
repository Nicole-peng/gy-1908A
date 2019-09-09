'''
key:value

key唯一
key必须是不可变的，数字，字符，元组，列表（不可以），字典（不可以）
'''


# 增
# 初次创建
d = {}
dl = {'name':'小明同学','sex':'女'}
#新增一对数据
dl['age'] = 18
print(dl)

y = {}
yl = {'name':'小伦同学','sex':'女'}
# 新增一堆数据
yl['age'] ,yl['eduction'] = 15,'高中'
print(yl)

# 删
# 删除key
print(yl.pop("age"))
print(yl)

del yl["sex"]
print(yl)

# 删除整个字典

# del yl
# print(yl)

# 清空
# yl.clear()
# yl = {}
# 改

yl["name"] = '小伦同学'
print(yl)

# 查
print(yl["name"])

# 获取字典长度
print(len(dl))

# 成员判断，只能用key做判断

print(15 in yl)

# 字典拼接
# 在某个字典末尾加上另一个字典

y2 = {1:'234',2:'345'}

y3 = {3:'456',4:'567'}

# 在某个字典末尾加上另一个字典
# 拿着y3修改y2，y2中key有则改value,武者网新增
y2.update(y3)
print(y2)

# 生成一个新的字典
c = dict(y2,**y3)
print(c)
print("234 5")