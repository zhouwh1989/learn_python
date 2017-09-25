print("----------------I love python--------------")
temp = input("input a number:")     # input返回的是string
guess = int(temp)       # int强转
if guess == 8:
    print("you guess what i think")
    print("but no use")
else:
    print("you guess wrong")
print("game over")
        
## BIF = built in functions


## dir(__builtins__)    # 查看内置函数

## help(int)       # 帮助


## python 大小写敏感
if "FishC" == "fishc":
    print("They are the same.")
else:
    print("They are not the same.")        



## hello
tmp = input("Please input your name:")
print("Hello, " + tmp)



## 判断
tmp = input("Please input a number:")
int_tmp = int(tmp)
if int_tmp >= 1 and int_tmp <= 100:
    print("yes")
else:
    print("no")
