global valid_num
valid_num = 0
def readfile(file_name):
    with open(file_name,'r',encoding = 'utf-8') as f:
        temp_1 = f.read()
    return temp_1

def static_num_func(file_content):
    return len(file_content.split())

def static_ave_func(file_content):
    global valid_num
    sum_1 = 0
    list_1 = file_content.split()
    for i in list_1:
        try:
            sum_1 += int(i)
            valid_num += 1
        except ValueError:
            print("跳过无法转换为整数的元素")
    if valid_num == 0:
        return 0
    return sum_1 / valid_num

def static_var_func(file_content,statistic_ave):
    global valid_num
    sum_1 = 0
    list_1 = file_content.split()
    for i in list_1:
        try:
            sum_1 += (int(i) - statistic_ave) ** 2
        except ValueError:
            print("跳过无法转换为整数的元素")
    if valid_num == 0:
        return 0
    return sum_1 / valid_num

def outfile(file_name,statistic_num,statistic_ave,statistic_var):
    with open(file_name,'w',encoding = 'utf-8') as f:
        f.write(f'数据个数{statistic_num}\n')
        f.write(f'数据均值{statistic_ave}\n')
        f.write(f'数据方差{statistic_var}\n')
        
file_content = readfile('作业.txt')
statistic_num = static_num_func(file_content)
statistic_ave = static_ave_func(file_content)
statistic_var = static_var_func(file_content,statistic_ave)
outfile('处理作业.txt',statistic_num,statistic_ave,statistic_var)