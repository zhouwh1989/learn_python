# 元组  内部的元素不可以修改
member = (1, 2, 3)
print(member)

member1 = member[1:2]
print(member1)

#只有一个元素的元组，要加，
member2 = (1,)
print(member2)

#空元组
member3 = ()
print(member3)

#元组的插入,将原始的元组拆开，重新生成一个新的元组
member = member[:1] + (345,) + member[1:]
print(member)

