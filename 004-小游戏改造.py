## 条件分支
print(1 < 3)    # true
print(1 > 3)    # false
print(1 == 1)   # true


# 循环
print("----------------I love python--------------")
import random
secret = random.randint(1, 100)

temp = input("input a number:")     # input返回的是string
guess = int(temp)       # int强转

if guess == secret:
    print("you guess what i think")
    print("but no use")
else:
    while guess != secret:
        if guess > secret:
            print("bigger")
        else:
            print("smaller")
        temp = input("input a number:")     # input返回的是string
        guess = int(temp)       # int强转
        if guess == secret:
            print("you guess what i think")
            print("but no use")
            break

print("game over")


## and操作符
print(3>2 and 7<6)
