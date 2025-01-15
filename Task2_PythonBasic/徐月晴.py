def read_data(file_path):
    with open(file_path, 'r') as file:
        data = []
        for line in file:
            data.extend(map(float, line.split()))  
        return data

# 计算均值
def calculate_average(data):
    total = 0  
    count = 0  
    for num in data:
        total += num  
        count += 1  
    average = total / count  
    return average

# 计算方差
def calculate_variance(data, average):
    total = 0 
    count = 0  
    for num in data:
        total += (num - average) ** 2  
        count += 1  
    variance = total / count  
    return variance


def write_results(file_path, n, average, variance):
    with open(file_path, 'w') as file:
        file.write(f"data_nums: {n}\n")
        file.write(f"average: {average}\n")
        file.write(f"variance: {variance}\n")


def main():
  
    input_file = 'E:\\xyq\\卓越_任务\\datas.txt'  
    output_file = 'result_data.txt'  

    data = read_data(input_file)

    n = len(data) 
    average = calculate_average(data)  
    variance = calculate_variance(data, average)  

    write_results(output_file, n, average, variance)

    print(f"处理完成，结果已保存到 {output_file}")

if __name__ == "__main__":
    main()
