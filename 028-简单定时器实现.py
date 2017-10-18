### 简单利用time模块定制Timer定时器
### 无借位，不考虑闰年和闰月

import time as t

class MyTimer():
    # 开始计时
    def start(self):
        self.begin = t.localtime()
        print("开始计时")

    def stop(self):
        if not self.begin:
            print('提示：请先调用start()进行计时')
        else:
            self.end = t.localtime()
            self.__calc()
            print("结束计时")
            print(self.prompt)

    #内部方法，计算时间
    def __calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + self.unit[index]

        #print(self.prompt)

        # 重新初始化
        self.begin = 0
        self.end = 0


    def __str__(self):
        return self.prompt

    def __repr__(self):
        return self.pompt

    def __init__(self):
        self.prompt = "未开始计时,请先调用start开始计时"
        self.lasted = []
        self.begin = 0
        self.end = 0
        self.unit = ['year', 'month', 'day', 'hour', 'min', 'sec']

    def __add__(self, other):
        prompt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index]+other.lasted[index])
            if result[index]:
                prompt += str(result[index]) + self.unit[index]
        return prompt
t1 = MyTimer()
print(t1)   #未开始计时
t1.start()
t.sleep(2)  #sleep 5 seconds
t1.stop()


t2 = MyTimer()
print(t2)   #未开始计时
t2.start()
t.sleep(3)  #sleep 5 seconds
t2.stop()

print(t1 + t2)
        
