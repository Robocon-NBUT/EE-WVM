cnt = 0
lst = []

def Statistics_data():
    global cnt
    file_path = input('Enter file path: ')
    with open(file_path, 'r', encoding='utf-8') as infile:
        d = infile.read()
        lst.extend([int(item) for item in d.split(' ') if item])
        cnt = len(lst)

def avg_data():
    if cnt == 0:
        return 0
    total = sum(lst)
    avg = total / cnt
    return avg


def variance_data(a):
    if not lst:
        return 0
    variance = sum((x - a) ** 2 for x in lst) / cnt
    return variance


Statistics_data()
avg = avg_data()
print(f'数据的平均值是: {avg}')
var = variance_data(avg)
print(f'数据的方差是: {var}')