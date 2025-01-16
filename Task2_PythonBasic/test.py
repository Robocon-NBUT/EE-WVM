arr=[]
f=open("data.txt",'r',encoding="UTF-8")
for line in f:
    line=line.strip("\n")
    brr=line.split(" ")
    arr.extend(brr)
length=len(arr)
print(length)
count=0
for i in arr:
    count=int(i)+count
    print(int(i))
average=count/length
fangcha=0
for i in arr:
    fangcha=fangcha+(average-int(i))**2
fangcha=fangcha/length
f.close()
f1=open("datawrite.txt",'w',encoding="UTF-8")
f1.write(str(average)+'\n')
f1.write(str(fangcha))
f1.close()
print(f"平均数为:{average} 方差为：{fangcha}")



