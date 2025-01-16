def read_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
                data.extend(map(float,line.strip()))
    return data

def calculate_variance(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    return n, mean, variance

def write_data(file_path, n, mean, variance):
    with open(file_path, 'w') as file:
        file.write(f"个数: {n}\n")
        file.write(f"均值: {mean}\n")
        file.write(f"方差: {variance}\n")

def main(input_file, output_file):
    data = read_data(input_file)
    if data:
        n, mean, variance = calculate_variance(data)
        write_data(output_file, n, mean, variance)
        print(f"结果已写入 {output_file}")
    else:
        print("没有有效数据")

if __name__ == "__main__":
    input_file = 'input.txt'  # 输入文件路径
    output_file = 'output.txt'  # 输出文件路径
    main(input_file, output_file)
