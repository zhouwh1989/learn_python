#hanoi
def hanoi(n, x,y,z):    # 中间的那个参数只是借用的柱子，真正操作的时候无需关心，只要切换首尾的柱子就行
    if n == 1:
        print(x ,"-->", z)
    else:
        hanoi(n-1, x,z,y)   #将前n-1个盘子从x移动到y上
        print(x, '-->', z)  #将最底下的盘子从x移到z上
        hanoi(n-1, y,x,z)   #将y上的n-1个盘子移到z上

print(hanoi(4, 'x', 'y', 'z'))
