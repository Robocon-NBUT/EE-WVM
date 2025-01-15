def Read_data():
    list_data = []
    with open('data.txt', 'r', encoding = 'utf-8')as f:
        data = f.read()
    for i in data.split():
        list_data.append(float(i))
    return list_data

def Count(List):
    cnt = 0
    for i in List:
        cnt += 1
    return cnt

def Avg(List, count):
    sum = 0
    for i in List:
        sum += i
    return sum / count

def variance(List, count):
    sum = 1
    for i in List:
        sum *= i
    return sum / count

def save(t1, t2 ,t3):
    with open('ans.txt', 'w', encoding = 'utf-8')as f:
        f.write(f'数据个数：{t1}   均值：{t2}    方差{t3}')


List_data = Read_data()

cnt = Count(List_data)

avg = Avg(List_data, cnt)

var = variance(List_data, cnt)

save(cnt ,avg, var)