
inputFilename ="E:\ACLOS\python文件集\data.txt"
outPutFileName = "result.txt"

def getAverage(List,num):
     ans = 0
     for item in List :     ans +=item
     return ans/num

def getVariance(List,avg,num):
    ans = 0
    for item in List:  ans+=(item-avg)**2
    return ans/(num-1)

def writeToFile(num,avg,variance):
    with open(outPutFileName,'w') as writeFile:
        writeFile.write("数据总数: " + str(num) + " " +"平均值: " + str(avg) + " " + "方差: " + str(variance) )    
    print("数据写入已完成!")    

try:        
    with open(inputFilename,'r') as readFile:
        lines = readFile.readlines()
except IOError:
    print("文件不存在")  
else: 
    #print("数据总数为: " + str(numOfData(lines) ) + " " + "平均值为: " + str(getAverage(lines)) + " " + "方差为: " + str(getVariance(lines)) ) 
    num = len(lines)

    floatList = [float(item.strip()) for item in lines] #将文本文件中的字符数据转换为浮点数

    avg = getAverage(floatList,num)
    variance = getVariance(floatList,avg,num)
    print("数据总数为: " + str(num) + " " +"平均值: " + str(avg) + " " + "方差: " + str(variance) )

    #写入文件
    writeToFile(num,avg,variance)

        


