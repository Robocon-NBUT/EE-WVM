def a1(inPut):
    data = []
    with open(inPut, 'r') as file:
        for line in file:
            # 将每一行中的数字添加到 data 列表中，先将其转换为浮点数
            for num in line.split():
                data.append(float(num))
    return data


def a2(data):
    b1 = 0
    b2 = len(data)
    for line in data:
        b1 += line
    # 计算平均值
    average = b1 / b2
    return average


def a3(data, average):
    b1 = 0
    b2 = len(data)
    for line in data:
        b1 += (line - average) ** 2
    # 计算方差
    variance = b1 / b2
    return variance


def a4(inPut, n, average, variance):
    with open(inPut, 'w') as file:
        # 写入数据并添加换行符
        file.write(f"{n}\n")
        file.write(f"{average}\n")
        file.write(f"{variance}\n")


file1 = 'data.txt'
file2 = 'put.txt'
data = a1(file1)
n = len(data)
average = a2(data)
variance = a3(data, average)
a4(file2, n, average, variance)