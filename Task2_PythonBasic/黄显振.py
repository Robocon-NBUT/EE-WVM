def average(data,count):
    sum=0
    for element in data:
        sum+=int(element)
    return sum/count

def variance(data, count, average):
    sum=0
    for element in data:
        element=int(element)
        sum+=(element-average)**2
    return sum/count

in_file=open("data.txt", "r", encoding="UTF-8")

data=[]
for line in in_file:
    line=line.strip()
    temp=line.split(" ")
    data.extend(temp)

count=len(data)
average=average(data, count)
variance=variance(data, count, average)

in_file.close()

out_file=open("result.txt","w", encoding="UTF-8")

out_file.write(f"数据个数：{count}\n")
out_file.write(f"均值：{average}\n")
out_file.write(f"方差：{variance}\n")

out_file.close()
