## Mylist继承list
class Mylist(list):
    pass  # 仅仅作为占位符

l = Mylist()
l.append(1)
l.append(3)
print(l)


### 什么是self  类似于C++的this
##class Ball:
##    def setName(self, name):
##        self.name = name
##    def kick(self):
##        print('My name is %s, who kick me...' % self.name)
##
##a = Ball()
##a.setName('ball A')
##a.kick()
##
##b = Ball()
##b.setName('ball B')
##b.kick()


### 构造方法 __init__(self, par1, ...)
##class Ball:
##    def __init__(self, name):
##        self.name=name
##    def setName(self, name):
##        self.name = name
##    def kick(self):
##        print('My name is %s, who kick me...' % self.name)
##
##a = Ball('Ball B')
##a.setName('ball A')
##a.kick()


### 公有和 私有
### 默认都是公有  __表示私有
class Person():
    __name = 'Vanora'
    def getName(self):
        return self.__name
a = Person()
#print(a.name)      # 错误
print(a.getName())



### super方法
import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print("我的位置是：", self.x, self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        super().__init__()      # super自动调用所有基类的方法，否则move方法调用会报错
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("吃货的梦想就是天天有的吃^_^")
            self.hungry = False
        else:
            print("太撑了，吃不下了！")

a = Goldfish()
a.move()

b = Shark()
b.move()
b.eat()




###### 一些常用的重要的BIF
## issubclass(class, classinfo)     # classinfo可以是元组
## isinstance(object, classinfo)     # 第一个参数如果是类，则返回False
## hasattr  测试对象是否有指定属性
## getattr  返回对象的属性值
## setattr  设定对象的属性
## delattr  属性不存在要抛出异常
## property 利用属性来设置属性，第一个参数是getattr，第二个是setattr，第三个是deldttr

