#导入随机数数据库
import random
#在创建的文本文件中插入100个数
with open("123.txt",'w') as file_w:
    for i in range(0,20):
        a=random.randint(0,100)
        file_w.write(f'{a}\n')

#创建一个数组
files=[]
#读文件
with open("123.txt",'r') as file_r:
    a=file_r.readlines()
    for i in a:
        i = i.strip()
        files.append(int(i))
    print(files)

#统计数据个数
num=len(files)
print(num)

#求均值
avg=sum(files)/num
print(avg)

#求数字平方的函数
def square(x):
    return x*x
#求方差
Variance=0
for i in range(0,num):
    mid=files[i]-avg
    Variance += square(mid)
print(Variance)

#写入新的文本
with open("new file.txt",'w',encoding='UTF-8') as file_new_w:
    file_new_w.write(f'原文本有{str(num)}个数据\n')
    file_new_w.write(f'原文中数据平均值为:{str(avg)}\n')
    file_new_w.write(f'原文中方差为:{str(Variance)}')
