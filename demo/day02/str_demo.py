# 截取
a = 'aaaaagfjfghxfgsdhgf'
# 截取其中一段
print(a[1:5])
print(a[5:])
print(a[:7])
print(a[:-2])

# 字符串倒叙排列
print (a[::-1])

# 重复字符串

print(a * 10)

# + 字符串拼接

# in 成员判断

# 字符串切片
d ='用例名，充值金额，断言'
print(d.split("，"))

y ='苹果，草莓，车厘子'
print(y.split("，"))

# 去空格

e ='   efhfhdhdjdfhsf'
print(e.strip())
e ='   xfgdfjfgd   '
print(e.strip())
e ='  yhthsd sgdh gdfh gedh   '
print(e.replace(' ',''))

# 替换

f ='gfdhgsh"fghfgjfgs'

print(f.replace('"','"'))

a ='dfgdfhd"gdhdfgsgd'
print(f.replace('"','"'))

# 查找

g ='guoyasoft'
print(g.find("ya"))

# 长度
print(len(g))


'''
GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1
# 拿到请求方法，协议版本，协议名，域名或者ip如果有端口拿到端口，请求地址，请求数

'''