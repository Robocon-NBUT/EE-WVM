def a1(file_du):
    data = []
    with open(file_du, 'r') as file:
        for line in file:
            # 将每一行中的数字添加到 data 列表中，先将其转换为浮点数
            for num in line.split():
                data.append(float(num))
    return data


def a2(data):
    lib1 = 0
    lib2 = len(data)
    for line in data:
        lib1 += line
    # 计算平均值
    junzhi = lib1 / lib2
    return junzhi


def a3(data, junzhi):
    lib1 = 0
    lib2 = len(data)
    for line in data:
        lib1 += (line - junzhi) ** 2
    # 计算方差
    fangcha = lib1 / lib2
    return fangcha


def a4(file_du, n, junzhi, fangcha):
    with open(file_du, 'w') as file:
        # 写入数据并添加换行符
        file.write(f"{n}\n")
        file.write(f"{junzhi}\n")
        file.write(f"{fangcha}\n")


file1 = 'data.txt'
file2 = 'put.txt'
data = a1(file1)
n = len(data)
junzhi = a2(data)
fangcha = a3(data, junzhi)
a4(file2, n, junzhi, fangcha)