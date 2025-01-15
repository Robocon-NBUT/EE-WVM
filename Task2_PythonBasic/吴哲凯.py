import numpy as np
# 读取文件中的数据
def read_d1(filename):#当文件内数据为每行一个的情况
    with open(filename, 'r') as f:
        data1 = [float(line.strip()) for line in f.readlines()]
    return data1

def read_d2(filename):#当文件内数据有多行且数据有多个的情况
    with open(filename,'r') as f:
        data2=[];
        for line in f.readlines():
            data2.extend([float(x)for x in line.strip().split(' ')])
    return data2

def calculate(data2):
    aver = np.mean(data2)#计算数据的均值
    vari = np.var(data2)#计算数据的方差
    return aver, vari

# 将结果写入新文件
def write_r(filename, aver, vari):
    with open(filename, 'w',encoding="UTF-8") as f:
        f.write(f"均值: {aver}\n")
        f.write(f"方差: {vari}\n")

input_file = 'input.txt'  # 输入文件路径
output_file = 'output.txt'  # 输出文件路径
# 读取数据
#data = read_d1(input_file)
data=read_d2(input_file)
#统计数据个数
count=len(data)
# 计算均值和方差
mean, var = calculate(data)
# 将结果写入新文件
write_r(output_file, mean, var)
print(f"结果已保存到 {output_file} 数据的个数为 :{count}")