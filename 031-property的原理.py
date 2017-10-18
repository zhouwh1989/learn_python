### 描述符
### 将某种特殊类型的类的实例指派给另一个类的属性
### __get__(self, instance, owner)      访问属性，返回属性的值
### __set__(self, instance, value)      属性分配中调用，不返回值
### __delete__(self, instance)      控制删除操作，不返回任何内容

class Mydesc:
    def __get__(self, instance, owner):
        print("get: ", self, instance, owner)

    def __set__(self, instance, value):
        print("set: ", self, instance, value)

    def __delete__(self, instance):
        print("del: ", self, instance)

class Test:
    x = Mydesc()

test = Test()
test.x
print(test)
print(Test)
test.x = "X-man"
del test.x




#### 温度类
class Celsius:
    def __init__(self, value=26.0):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)

    def __delete__(self, instance):
        print("del: ", self, instance)

class Fahrenheit:
    def __init__(self, value=26.0):
        self.value = value

    def __get__(self, instance, owner):
        return instance.cel * 1.8 +32

    def __set__(self, instance, value):
        instance.cel = ( float(value) - 32 ) / 1.8

    def __delete__(self, instance):
        print("del: ", self, instance)
    

# 描述符类
class Temperature:
    cel = Celsius()
    fah = Fahrenheit()

t = Temperature()
print("默认cel: ", t.cel)
print("默认的Fah: ", t.fah)
t.cel = 20
print("设置后cel: ", t.cel)
print("设置后Fah: ", t.fah)
t.fah = 200
print("设置后cel: ", t.cel)
print("设置后Fah: ", t.fah)


