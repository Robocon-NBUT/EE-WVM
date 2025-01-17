def r_file (file_name):
    with open(file_name,'r') as file:
        data=[]
        for line in file:
            data.extend(map(float,line.split()))
    return data

def averange_JK (data):
    total =0;
    num=0;
    for i in data :
        total =total+i
        num+=1
    averange =total/num
    return averange

def fangcha_JK (data,averange):
    total =0
    num=0
    for i in data :
        total=total+(i-averange)**2
        num+=1
    fangcha=total/num
    return fangcha

def w_file(O_file_name, n, averange,fangcha):
    with open(O_file_name,'w') as file:
        file.write(f"num:{n}\n")
        file.write(f"averange:{averange}\n")
        file.write(f"fangcha:{fangcha}\n")
    return

def main():
  
    I_file_name = 'datas.txt'  
    O_file_name = 'result_data.txt'  
    data = r_file(I_file_name)
    n = len(data) 
    average =averange_JK(data)  
    fangcha=fangcha_JK(data, average)  
    w_file(O_file_name, n, average,fangcha)

    print(f"处理完成，结果已保存到 {O_file_name}")

if __name__ == "__main__":
    main()