## list
#用help(list)的方式查看
a = list()

#字符串初始化list
b = 'I love YiYi'
b = list(b)
print(b)

#元组初始化list
c = (1,1,2,3,5,8,13,21,34)
c= list(c)
print(c)


##tuple

##len max
print(len(a))
print(max(b))
nu = [1,18,13,0,-58]
# 序列中的所有元素都是同一种数据类型的时候才可以相互比较
print(max(nu))


##sum
##所有元素都是同一种数据类型的时候才可以相加
##sum只支持整数和浮点数
tuple1 = (3.1, 2.3, 3.4)
print(sum(tuple1))


##sorted 默认从小到大排列
print(sorted(nu))


##reversed 反转
##返回结果是一个迭代器
print(reversed(nu))
#可以使用list强制转换为列表
print(list(reversed(nu)))


#enumerate 枚举  返回迭代器
print(list(enumerate(nu)))


##zip 返回迭代器
a = [1,2,3,4,5,6,7,8]
b = [4,5,6,7,8]
print(list(zip(a, b)))
