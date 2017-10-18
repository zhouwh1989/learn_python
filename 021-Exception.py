### try-except语句  try-finally
file_name = input('请输入要打开的文件名：')
fs = []     #借列表来保存文件句柄
try:
    f = open(file_name, 'r')
    fs.append(f)
    sum = 1 + '1'
    for each in f:
        print(each)
    
except OSError as reason:
    print('文件出错了: ' +  str(reason))
except TypeError as reason:
    print('Type error: ' + str(reason))
finally:
    ##无论如何都会执行的代码
    if len(fs)!= 0:
        fs[0].close()
        print('Close the file')
    else:
        print('open Error')




##raise 抛出一个异常
raise ZeroDivisionError('除数为0异常')
