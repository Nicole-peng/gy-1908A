# 整数
# 变量名是什么
# = 赋值符
# type是方法名
# 需要一个变量作为参数
# type()方法的作用是查看变量类型

# 整数
a = 1
print(type (a))
# 小数
a = 1.1
print(type(a))
# 字符串
c = 's'
print(type(c))
d = "222"
print(type(d))
e = '''333'''
print(type(e))
f = """4444"""
print(type(f))

# 列表[开始 ]结束，中间多个值用英文逗号隔开
# list列表
l = [2,4,5]
print(l)
print(type(l))
# tuple 元组
# 列表（开始）结束，中间多个值用英文逗号隔开，如果元组中只有单个值，用逗号结尾
t = (1,)
print(t)
print(type(t))
# dict 字典 哈希
# 字典（开始 ）结束，存成对的值，key:value多对值用逗号隔开
d = {'name':'呜呜呜呜','年龄':24}
print(d)
print(type(d))

'''
while(判断条件):
    循环体
    i=i+1
'''
for i in range(1.101,1):
    print(i)

i = 1
while(i < 101):
    print(i)
    i+=1
