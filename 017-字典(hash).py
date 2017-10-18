brand = ['lining', 'nake', 'Fishc']
slogan = ['一切皆有可能', 'Jus do it', '让编程改变世界']

print('Fishc的口号是：', slogan[brand.index("Fishc")])

#字典  key->>value
dict1 = {'lining':'一切皆有可能', 'nake':'Jus do it', 'Fishc':'让编程改变世界'}
print('Fishc的口号是：', dict1["Fishc"])

# 利用dict函数
dict2 = dict(((1,"1234"), (2, 12345)))
print(dict2)

dict3 = dict(hhh='hhh', jjj=678)
print(dict3)

dict4 = dict({(1,"1234"), (2, 12345)})
print(dict4)


##字典的内置方法
#fromkeys 重新创建一个新的字典
dict1 = {}
dict2 = dict1.fromkeys([1,2,3])     # 默认赋值None
print(dict2)

dict3 = dict1.fromkeys([1,2,3], ('one','two','three'))  #注意是整体赋值
print(dict3)


#keys和values
for eachK in dict3.keys():
    print(eachK)

for eachV in dict3.values():
    print(eachV)

#items 以元组的形式展示
for eachItem in dict3.items():
    print(eachItem)


#get方法 找不到键的时候会返回None
print(dict3.get(32, '木有'))


#copy 浅拷贝

#pop

#update
dict4 = {1:"1"}
dict3.update(dict4)
print(dict3)

dict5 = {4:"four"}
dict3.update(dict5)
print(dict3)
