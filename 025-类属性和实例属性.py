##
class C:
        num = 0     #类属性
        def __init__(self):
                self.x = 4  #实例属性
                self.y = 5  #实例属性
                C.count = 6     #类属性

## 区分类属性与实例属性
class BB:
        def printBB():
                print("no zuo no die")

BB.printBB()    #可以正常执行
##>>> bb = BB()
##>>> bb.printBB()
##Traceback (most recent call last):
##  File "<pyshell#8>", line 1, in <module>
##    bb.printBB()
##TypeError: printBB() takes 0 positional arguments but 1 was given


## 绑定
class BB:
        def printBB(self):
                print("no zuo no die")

##>>> bb = BB()
##>>> bb.printBB()    # 等价于bb.printBB(bb)
##no zuo no die
