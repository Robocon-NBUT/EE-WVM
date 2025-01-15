def read(file_path):
    numbers=[]
    with open(file_path,'r')as file:
        for line in file:
            nums=[]
            nums=line.split(' ')
            for num in nums:
                numbers.append(num)
    return numbers

def hecha (numbers):
    sum1=0
    sum2=0
    for i in numbers:
        sum1+=float(i)
        sum2+=float(i)**2
    return sum1,sum2
def write(file_path,lens,aval,fangcha):
    with open(file_path,'w')as file:
        file.write(f"数据个数{lens}\n")
        file.write(f"平均数为{aval}\n")
        file.write(f"数据个数{fangcha}\n")
file_path="D:\Desktop\新建 文本文档 (2).txt"
write_path="D:\Desktop\新建 文本文档.txt"
numbers=read(file_path)
sum1,sum2=hecha(numbers)    
aval=float(sum1/len(numbers))
fangcha=(sum2+len(numbers)*aval**2)/len(numbers)
lens=len(numbers)
print(f"数据个数{lens}")
print(f"平均数为{aval}")
print(f"数据个数{lens}")
write(write_path,lens,aval,fangcha)