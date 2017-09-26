#slice 切片
str1 = '121123214'
str2 = str1[1:3]
print(str2)

#capitalize() 把字符串的第一个字符改为大写
#casefold() 把整个字符串的所有字符改为小写
#center(width) 将字符串居中，并使用空格填充至长度 width 的新字符串
#count(sub[, start[, end]]) 返回 sub 在字符串里边出现的次数，start 和 end 参数表示范围，可选。
#encode(encoding='utf-8', errors='strict') 以 encoding 指定的编码格式对字符串进行编码。
#endswith(sub[, start[, end]]) 检查字符串是否以 sub 子字符串结束，如果是返回 True，否则返回 False。start 和 end 参数表示范围，可选。
#expandtabs([tabsize=8]) 把字符串中的 tab 符号（\t）转换为空格，如不指定参数，默认的空格数是 tabsize=8。
#find(sub[, start[, end]]) 检测 sub 是否包含在字符串中，如果有则返回索引值，否则返回 -1，start 和 end 参数表示范围，可选。
#index(sub[, start[, end]]) 跟 find 方法一样，不过如果 sub 不在 string 中会产生一个异常。
#isalnum() 如果字符串至少有一个字符并且所有字符都是字母或数字则返回 True，否则返回 False。
#isalpha() 如果字符串至少有一个字符并且所有字符都是字母则返回 True，否则返回 False。
#isdecimal() 如果字符串只包含十进制数字则返回 True，否则返回 False。
#isdigit() 如果字符串只包含数字则返回 True，否则返回 False。
#islower() 如果字符串中至少包含一个区分大小写的字符，并且这些字符都是小写，则返回 True，否则返回 False。
#isnumeric() 如果字符串中只包含数字字符，则返回 True，否则返回 False。
#isspace() 如果字符串中只包含空格，则返回 True，否则返回 False。
#istitle() 如果字符串是标题化（所有的单词都是以大写开始，其余字母均小写），则返回 True，否则返回 False。
#isupper() 如果字符串中至少包含一个区分大小写的字符，并且这些字符都是大写，则返回 True，否则返回 False。
#join(sub) 以字符串作为分隔符，插入到 sub 中所有的字符之间。
#ljust(width) 返回一个左对齐的字符串，并使用空格填充至长度为 width 的新字符串。
#lower() 转换字符串中所有大写字符为小写。
#lstrip() 去掉字符串左边的所有空格
#partition(sub) 找到子字符串 sub，把字符串分成一个 3 元组 (pre_sub, sub, fol_sub)，如果字符串中不包含 sub 则返回 ('原字符串', '', '')
#replace(old, new[, count]) 把字符串中的 old 子字符串替换成 new 子字符串，如果 count 指定，则替换不超过 count 次。
#rfind(sub[, start[, end]]) 类似于 find() 方法，不过是从右边开始查找。
#rindex(sub[, start[, end]]) 类似于 index() 方法，不过是从右边开始。
#rjust(width) 返回一个右对齐的字符串，并使用空格填充至长度为 width 的新字符串。
#rpartition(sub) 类似于 partition() 方法，不过是从右边开始查找。
#rstrip() 删除字符串末尾的空格。
#split(sep=None, maxsplit=-1) 不带参数默认是以空格为分隔符切片字符串，如果 maxsplit 参数有设置，则仅分隔 maxsplit 个子字符串，返回切片后的子字符串拼接的列表。
#splitlines(([keepends])) 按照 '\n' 分隔，返回一个包含各行作为元素的列表，如果 keepends 参数指定，则返回前 keepends 行。
#startswith(prefix[, start[, end]]) 检查字符串是否以 prefix 开头，是则返回 True，否则返回 False。start 和 end 参数可以指定范围检查，可选。
#strip([chars]) 删除字符串前边和后边所有的空格，chars 参数可以定制删除的字符，可选。
#swapcase() 翻转字符串中的大小写。
#title() 返回标题化（所有的单词都是以大写开始，其余字母均小写）的字符串。
#translate(table) 根据 table 的规则（可以由 str.maketrans('a', 'b') 定制）转换字符串中的字符。
#upper() 转换字符串中的所有小写字符为大写。
#zfill(width) 返回长度为 width 的字符串，原字符串右对齐，前边用 0 填充。

