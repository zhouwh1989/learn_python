# 可以用dir来查看list的方法

# list 列表可以存放任何类型的数据
member=[1, '1234', 3.14, [1234, 56], 1]
print(member)
print(len(member))

#append 
member.append('dad')
member.append(['dad', 'eee'])
print(member)
print(len(member))

#extend
member.extend(['hello', 3456])
print(member)
print(len(member))

#insert
member.insert(0,['hello', 3456])
print(member)
print(len(member))

##删除
#remove 找到第一个符合的删除
member.remove(1)
print(member)
print(len(member))

#del
del member[0]   #删除具体的元素
print(member)
print(len(member))

#pop
member.pop()    # 出最后一个
print(member)
print(len(member))

member.pop(0)   #加下标参数
print(member)
print(len(member))



#slice
member[1:3] #不包含后面的值
member[:3]  #从0--2
member[:]   #列表的拷贝


#reverse
#sort   默认从小到大排列
#sort(reverse=True) 从大到小排列
