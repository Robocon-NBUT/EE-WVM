import random
import numpy as np

#生成n个随机数
def generate_random_numbers(n):
    numbers = [random.uniform(1, 1000) for _ in range(n)]
    return numbers

#将随机数写入文件
def write_numbers_to_file(file_path, numbers):
    with open(file_path, 'w') as file:
        for num in numbers:
            file.write(f"{num}\n")

#从文件中读取随机数，并存入数组numbers
def read_numbers_from_file(file_path):
    numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            numbers.append(float(line.strip()))
    return numbers

#计算个数、均值与方差
def calculate_statistics(numbers):
    n = len(numbers)
    mean = np.mean(numbers)
    variance = np.var(numbers, ddof=1)
    return n, mean, variance

#将结果写入文件
def write_statistics_to_file(file_path, n, mean, variance):
    with open(file_path, 'w') as file:
        file.write(f"count: {n}\n")
        file.write(f"mean: {round(mean,2)}\n")
        file.write(f"variance: {round(variance,2)}\n")


def main():
    #生成随机数 n
    n = random.randint(1, 100)
    #生成n个随机数
    numbers = generate_random_numbers(n)
    #将随机数写入文件nums.txt
    write_numbers_to_file('nums.txt', numbers)
    #从文件nums.txt读取数据
    numbers = read_numbers_from_file('nums.txt')
    #计算数据
    n, mean, variance = calculate_statistics(numbers)
    #将计算结果写入文件outputs.txt
    write_statistics_to_file('outputs.txt', n, mean, variance)


if __name__ == "__main__":
    main()





