### 求一个数的最大约数

## else与while语句搭配
## while循环中途被break中断，那么就不会执行else
## 否则，会执行else分支
def showMaxFactor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print('%d 的最大约数是： %d' % (num, count))
            break;
        count -= 1
    else:
        print('%d是素数' % num)

num = int(input("Please input a num:"))
showMaxFactor(num)




## try和else搭配
## try捕获到异常时，就不执行else分支
## 否则，就会执行else分支
num = int(input("Please input a num:"))
try:
    int(num)
except ValueError as reason:
    print('Error' + str(reason))
else:
    print('OK')


## with关键字   自动进行垃圾回收或者异常清理
## with打开文件，不用再显示调用close了
with open('test.txt', 'r') as f:
    print(f.read())




