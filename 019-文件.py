#读写文件示例
f = open('test.txt', 'a+')
#print(f)
f.write("hello world!!!\n")
f.seek(0,0)
print(f.read())
f.close()

##注意：如果使用了b模式打开文件，
##      3.5以上版本的python中write的参数类型是bytes，带有编码格式了

#文件逐行遍历[高效方式]
f = open('test.txt', 'r')
for each_line in f:
    print(each_line)
    print(type(each_line))


## import os
## import os.path
