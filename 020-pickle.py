import pickle

## 将列表保存为二进制文件
my_list = [1, 1234.234, 'hello', ['test', 123]]
f = open('my_list.pkl', 'wb')
pickle.dump(my_list, f)
f.close()


## 从文件中读取到列表
f = open('my_list.pkl', 'rb')
print(type(pickle.load(f)))
f.close()

