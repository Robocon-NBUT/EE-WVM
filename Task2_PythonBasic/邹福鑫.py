def Read_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
             data.extend( map(float,line.split()))
    return data

def Avarage_fun(data):
    sum1 = 0
    num = 0
    for temp in data:
        sum1 += temp
        num += 1
    avarage = sum1 / num
    return avarage

def Fc_fun(data,avarage):
    sum2 = 0
    num = 0
    for temp in data:
        sum2 += (temp - avarage)**2
        num += 1
    fc = sum2 / num
    return fc

def Write_data(file_path, n, average, variance):
        with open(file_path,'w') as file:
            file.write(f"data_len:{n}\n")
            file.write(f"data_average:{average}\n")
            file.write(f"data_variance:{variance}\n")

def main():
    input_file = "D:\\python\\py\\data.txt"
    output_file = "result_data.txt"

    data = Read_data(input_file)
    l_n = len(data)
    avarage = Avarage_fun(data)
    fc = Fc_fun(data,avarage)
    Write_data(output_file,l_n,avarage,fc)
    print(f"保持成功：地点:{output_file}")
    print (data)

#只有直接运行这个代码的时候才能执行main()函数后面的程序
if __name__ == "__main__":
    main()