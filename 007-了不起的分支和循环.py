## 三元操作符
## x if x < y else y

x=10
y=100
print(x if x < y else y)
print(x if x > y else y)

## assert 程序中置入检查点，为假的时候崩溃
#assert 3 > 4


## for循环
## for 目标 in 表达式:
##      循环体
string = "123456789"
for i in string:
    print(i)


## 元组
member = ['你好', 'world!', 'I ', 'love ', 'you']
for each in member:
    print(each, len(each))


## range   BIT  不包含最后的值
print(range(5)) # range(0,5)
print(list(range(5)))   # [0, 1, 2, 3, 4]

for i in range(10):
    print(i)

for i in range(1,5):
    print(i)

for i in range(0,10,3):
    print(i)
