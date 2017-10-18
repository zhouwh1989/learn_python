### __getsttr__(self, name)
### 试图获取一个不存在的属性时的行为

### __getattribute__(self, name)
### 属性被访问时的行为

### __setattr__(self, name, value)
### 属性被设置时的行为

### __delattr__(self, name)
### 属性被删除时的行为

class C:
    def __getattribute__(self, name):
        print("getsttribute")
        return super().__getattribute__(name)

    def __getattr__(self, name):
        print("getattr")

    def __setattr__(self, name, value):
        print("setattr")
        super().__setattr__(name, value)
        
    def __delattr__(self, name):
        print("delAttr")
        super().__delattr__(name)

c = C()
c.x
c.x=1
del c.x


#### 一个矩形类
class recTangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        if name == "square":
            self.width = value
            self.height = value
        else:
            ## 推荐使用super的方式
            super().__setattr__(name, value)
            ##或者使用__dict__属性
            ## slef.__dict__[name] = value

    def getArea(self):
        return self.width * self.height

r = recTangle(4, 5)
print(r.getArea())

r.square = 20
print(r.getArea())
