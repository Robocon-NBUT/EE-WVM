import random
import numpy as np


# 1. 生成随机数，并存入数组 nums
def generate_random_numbers(n):
    random_numbers = [random.randint(1, 1000) for _ in range(n)]
    return random_numbers


# 2. 将数组 nums 以字符串形式写入文件 nums.txt
def write_random_numbers(file_name, random_numbers):
    # 使用空格分隔数字
    with open(file_name, "w") as f:
        f.write(" ".join(str(i) for i in random_numbers))


# 3. 从文件中读取数据，并存入数组 nums
def read_numbers(file_name):
    numbers = []
    with open(file_name, "r") as f:
        line = f.readline()
        # 使用列表推导式将分割后的字符串元素转换为整数添加到列表
        numbers = [int(num) for num in line.split()]
    return numbers


# 4. 从数组中读取数据，并计算个数、均值、方差
def calculate_numbers(numbers):
    cnt = len(numbers)
    mean = np.mean(numbers)
    # 使用 numpy 的 var 函数计算样本方差
    variance = np.var(numbers, ddof=1)
    return cnt, mean, variance


# 5. 将计算结果写入文件 outputs.txt
def write_result(file_name, cnt, mean, variance):
    with open(file_name, "w") as f:
        f.write(f"number of numbers:{cnt}\n")
        f.write(f"mean:{round(mean,2)}\n")
        f.write(f"variance:{round(variance,2)}\n")


def main():
    # 随机生成一个数 n
    n = random.randint(1, 100)
    # 生成 n 个随机数
    random_numbers = generate_random_numbers(n)
    # 将随机数写入文件 nums.txt
    write_random_numbers("nums.txt", random_numbers)
    # 从文件 nums.txt 中读取数据
    numbers = read_numbers("nums.txt")
    # 计算数据
    cnt, mean, variance = calculate_numbers(numbers)
    # 将结果写入文件 outputs.txt
    write_result("outputs.txt", cnt, mean, variance)


if __name__ == "__main__":
    main()
