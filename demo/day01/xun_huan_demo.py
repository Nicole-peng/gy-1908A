# # for循环
# '''
# for i in range(100):
#     代码块
# '''
#
# for i in range(10):
#     print("重要的事情说n遍")
#
# # 打印出100以内的奇数
# for i in range(1,100,2):
#     print(i)
#
# for i in range(1,100):
#     if(i%2 == 1):
#         print(1)
# # 求出1+2+3...+100和
s = 0
for i in range(1,101):
    s = i + 1
print(s)
# # 求出100! 1*2*3*4...*100
# s = 1
# for i in range(1,101):
#     s *= i
# print(s)
# # 求出100以内的质数
#
# for i in range(100):
#     f = False # 标记i是否被整除
#     for j in range(2,i):
#         if(i%j==0):
#             f = True #如果i被整除，把f值改成True
#             break
#     if(not f):
#        peint(i)
#
# # 打印出九九乘法表（循环嵌套）
# # 冒泡排序
#
# a = 0
# a += 1
# a = a + 1
# # 终止循环 break
#
# # 打印出100以内的数，遇到5就终止
# for i in range(100):
#     if(i == 5):
#         break
#     print(i)
#
# # 跳过本次循环 continue
# # # 打印出100以内的数，如果可被5整除则跳过
# for i in range(100):
#     if(i%5 == 0):
#         continue
#     print(i)
#
#
# # 打印出100以内的数，遇到10就终止
# for i in range(100):
#     if(i == 10):
#         break
#     print(i)
#
# # 打印出100以内的数，如果可被8整除就跳过
# for i in range(100):
#     if(i%8 == 0):
#         continue
#     print(i)
#
#
# # while

# while 循环



'''
i = 0
while(判断条件):
    循环体
    i=i+1
'''

# 显示1-100
def xian_shi():
    i = 1
    while(i < 101):
        print(i)
        i += 1 #  i = i + 1

# 监听(进入死循环一直监听)
def si_xun_huan():
    while(True):
        pass



if __name__ == '__main__':
    xian_shi()