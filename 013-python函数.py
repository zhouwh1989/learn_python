##函数
def MyFirstFun():
    print('First Func')
    print('So happy')

MyFirstFun()

#加个参数
def MySecondFun(name):
    print(name + "World")

MySecondFun('Hello ')


##函数的返回值
#return


##形参和实参


##函数文档
def MyThirdFun():
    '第一个函数文档'
    #第一个函数文档
    print('First Func')
    print('So happy')
MyThirdFun()

print(MyThirdFun.__doc__)

print('help(MyThirdFun)')
help(MyThirdFun)


##关键字参数
print('\n关键字参数\n')
def fun4(name, words):
    print(name + '->' + words)

fun4('Vanora', 'I Love you')
fun4(words='I love you', name='aery')



##默认值参数
print('\n默认值参数\n')
def fun5(name='YiYi', words='So noisy'):
    print(name + '->' + words)

fun5()
fun5('Vanora', 'I Love you')
fun5(words='I love you', name='aery')



## 收集参数，可变参数
print('\n可变参数\n')
def test(*parm):
    print('可变len=', len(parm))
    print('first param: ', parm[0])
test(1,2,3,4,5)


##可变参数和参数结合
print('\n可变参数和参数结合\n')
def test1(*parm, exp=7):
    print('可变len=', len(parm), 'exp=', exp)
    print('first param: ', parm[0])
test1(1,2,3,4,5,'hello', exp=234.5678)

