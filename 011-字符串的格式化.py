## format方法
# replacement
# 位置参数
tmp = "{0} love {1} {2}".format("I", "Yi", "Yi")
print(tmp)

#关键字参数
tmp = "{a} love {b} {c}".format(a="I", b="Yi", c="Yi")
print(tmp)

#综合位置参数和关键字参数
###注意：位置参数必须在关键字参数之前

# {}转义
tmp = "{{0}}".format("不打印")
print(tmp)  # {0}

#格式化符号
#:表示格式化符号的开始
tmp= "{0:.1f}{1}".format(27.658, "GB")
print(tmp)

#%c
tmp = "%c" % 97
print(tmp)

tmp = "%c %c %c" % (97, 98, 99)
print(tmp)

#%s
tmp = "%s" % 97
print(tmp)

#%d
tmp = "%d + %d = %d" % (4, 5, 4+5)
print(tmp)
