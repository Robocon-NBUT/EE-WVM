import statistics
def read(file):
    with open(file,'r') as file:
        data=[]
        for line in file:
            data.extend(map(float,line.split()))
    return data

def calculate(data):
    count=len(data)
    mean=statistics.mean(data) if count>0 else 0
    variance=statistics.pvariance(data) if count>1 else 0
    return count,mean,variance

def write(file,count,mean,variance):
    with open(file,'w') as file:
        file.write(f"数据个数：{count}\n")
        file.write(f"均值：{mean}\n")
        file.write(f"方差：{variance}\n")

input_file='C:/Users/Shadow/Desktop/python_test/data.txt'
output_file='C:/Users/Shadow/Desktop/python_test/output.txt'
data=read(input_file)
count,mean,variance=calculate(data)
write(output_file,count,mean,variance)
print("处理完成")