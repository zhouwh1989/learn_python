### 魔法方法  被__包围   例如 __init__

## __new__(cls, ...)    第一个被调用的方法
## 一般继承一个不可改变的方法是调用
## exp 将参数全部转换为大写
class CapStr(str):
    def __new__(cls, string):
        Mystring = string.upper()
        return str.__new__(cls, Mystring)

s = CapStr('I Love Aery!!!')
print(s)

## __init__(self, ...)  需要传递参数的需要重写
## 返回值为None

## __del__(self)     类似于析构
