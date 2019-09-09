# # 新增单个数据
# l = [1,2,3,4,5,6,7,8,9]
# l.append(97)
# print(l)
#
# # 在列表中的某个位置新增单个数据
# l.insert(3,97)
# print(l)
#
# # 在列表最后新增多个数据
# y = [9,9,7,7]
# l.extend(y)
# print(l)
# print(y)

# 新增数据
# 在列表最后新增单个数据
l = [1,2,3,4,5,6]
l.append(11)
print(l)
# 在列表的某个位置新增单个数据
l.insert(1,11)
print(l)
# 在列表最后新增多个数据
s = [1,2,3,4]
l.extend(s)
print(l)
print(s)


# 删除数据
# 根据下标删除数据
l = [1,2,3,4,5,6]
print(l.pop(1))
print(l)
