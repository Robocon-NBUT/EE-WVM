import os
import random

file_path = "G:\\desktop\\test.txt"
output_path = "G:\\desktop\\ans.txt"

def get_mydata(Start,End,nums):
    """
    随机生成50个1-100之间的随机数，返回一个数组，
    """
    want_return = {}

    for i in range(nums):
        want_return[f"第{i}个数据"] = random.randint(Start,End)
        print(f"第{i+1}个随机数是：{want_return[f'第{i}个数据']}")

    return want_return


mydata = get_mydata(1,100,50)

#写入数据
with open(file_path, "w") as file:
    for key,value in mydata.items():
        file.write(f"{key} {value}\n")


with open(file_path, "r") as file:
    cnt = 0
    Read = {}
    ans = {}
    sum = 0
    avg = 0
    var = 0

    for i in file:

        i=i.strip()
        now_line = i.split(" ")
        Read[f"第{cnt}个数据"] = now_line[1]
        cnt += 1
        sum += int(now_line[1])
    print(f"一共有{cnt}个数据")

    avg = sum/cnt
    print(f"平均数是{avg}")

    for key,value in Read.items():
        var += (int(value) - avg)**2

    var = var/(cnt-1)

    print(f"方差是{var}")

    with open(output_path, "w") as file:
        file.write(f"一共有{cnt}个数据\n")
        file.write(f"平均数是{avg}\n")
        file.write(f"方差是{var}\n")



















