### 使用easyGUI进行简单的图形界面开发
import easygui as g
import sys


## msgbox

g.msgbox('Hello world', "I am title")

## ccbox
if g.ccbox():
    print('ccbox continue')
else:
    print('ccbox exit')


## choicebox
choice = ['A', 'B', 123]
replay = g.choicebox('请输入你的选择', choices=choice)
print(replay)


####
##easygui的全部示例用法
#g.egdemo()


### 一个简单示例
##import sys
##
##while 1:
##        g.msgbox("嗨，欢迎进入第一个界面小游戏^_^")
##
##        msg ="请问你希望在鱼C工作室学习到什么知识呢？"
##        title = "小游戏互动"
##        choices = ["谈恋爱", "编程", "OOXX", "琴棋书画"]
##        
##        choice = g.choicebox(msg, title, choices)
##
##        # note that we convert choice to string, in case
##        # the user cancelled the choice, and we got None.
##        g.msgbox("你的选择是: " + str(choice), "结果")
##
##        msg = "你希望重新开始小游戏吗？"
##        title = "请选择"
##        
##        if g.ccbox(msg, title):     # show a Continue/Cancel dialog
##                pass  # user chose Continue
##        else:
##                sys.exit(0)     # user chose Cancel
