###匿名函数
#普通的函数
def ds(x):
    return 2*x+1

#lambda
#lambda x:2*x+1
g = lambda x:2*x+1
print(g)    #返回函数
print(g(5))

#多参数
add = lambda x,y:x+y
print(add(4,5))



##filter()  去伪存真
filter(None, [1, 0, False, True])  #返回filter对象 
print(list(filter(None, [1, 0, False, True])))  #过滤true的那部分

#过滤奇数[利用lambda表达式做匿名函数]
tmp = range(50)
print(list(filter(lambda x:x%2, tmp)))



#map()  
print(list(map(lambda x:x+2, range(10))))
