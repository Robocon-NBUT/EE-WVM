import random

# 生成随机数 写入txt文本中
def rd():
    with open('data.txt','w') as f:
        num = [random.randint(1,10) for _ in range(10)]
        for i in num:
            f.write(f'{i}\n') #一个数据占据一行

class number:
    def __init__(self ,inFile ,outFile):
        self.inFile = inFile # 入口文件
        self.outFile = outFile # 出口文件
        self.data = [] # 文件中的数据
        self.read() # 读取入口文件

    # 读取文件的数据
    def read(self):
        with open(self.inFile,'r') as f:
            for line in f:
                line = line.strip() # 去除空格和换行符
                if line.isdigit(): # 判断是否为数字
                    self.data.append(int(line))

    # 数据的个数
    def cnt(self):
        return (len(self.data))

    # 数据的平均值
    def average(self):
        return (sum(self.data) / len(self.data))

    # 数据的方差
    def dataVar(self):
        avg = self.average() # 获取平均值
        sum = 0 # 数据 平均 - 数据的平方和
        for i in range(len(self.data)):
            sum += (self.data[i] - avg) ** 2 # 方差
        return sum / len(self.data)

    # 将所有结果写入文件
    def write(self):
        print(self.cnt())
        print(self.average())
        print(self.dataVar())
        with open(self.outFile,'w') as f:
            f.write(f'{self.cnt()}\n') # 数据个数
            f.write(f'{self.average()}\n') # 数据平均值
            f.write(f'{self.dataVar()}\n') # 数据方差

if __name__ == '__main__':
    rd() # 随机数写入文件

    # 类初始化
    num = number('data.txt','result.txt')
    num.write() # 写入文件
