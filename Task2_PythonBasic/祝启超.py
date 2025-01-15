#读取文件
def readfile(filepath):
    with open(filepath, 'r') as f:
        nums=[]
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(' ')
            for num in line:
                nums.append(float(num))
    return nums

#计算均值
def calculate_average(nums):
    sum=0
    for i in nums:
        sum+=i
    return sum/len(nums)

# 计算方差
def calculate_variance(nums, average):
    sum=0
    for i in nums:
        sum+=(i-average)**2
    return sum/len(nums)

def writefile(filepath, n, average, variance):
    with open(filepath, 'w') as f:
        f.write(f"num_count: {n}\n")
        f.write(f"average: {average}\n")
        f.write(f"variance: {variance}\n")
  
ifile=r'D:\PycharmProjects\pythonProject\test1.txt'  
ofile = r'D:\PycharmProjects\pythonProject\test2.txt' 
nums=readfile(ifile)
average = calculate_average(nums)  
variance = calculate_variance(nums, average)  
writefile(ofile, len(nums), average, variance)
print(f"处理完成，结果已保存到 {ofile}")