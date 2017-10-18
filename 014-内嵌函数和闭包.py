###global关键字   可以用于在函数中修改全局变量的值
count = 5
print(count)
def MyFun():
    global count
    count = 10
    print(count)
    
MyFun()
print(count)


##内嵌函数
def fun1():
    print("call fun1")
    def fun2():
        print("call fun2")
    fun2()

fun1()


## 闭包 Closure
def FunX(x):
    def FunY(y):
        return x*y   # 这里注意同样只能访问x，不能修改x的值
    return FunY
i = FunX(8)
print(i)    #是个函数
j = i(5)
print(j)


##def test(x):
##    def FunY(y):
##        x *= x
##        return x*y   # 这里注意同样只能访问x，不能修改x的值
##    return FunY
##print(test(6))
##print(test(6)(7))   #因为修改了x的值，直接报错了【可以使用nonlocal关键字来避免】


def test(x):
    def FunY(y):
        nonlocal x
        x *= x
        return x*y   # 这里注意同样只能访问x，不能修改x的值
    return FunY
print(test(6))
print(test(6)(7))   #闭包中可以使用nonlocal关键字来修改全局作用域的值x

