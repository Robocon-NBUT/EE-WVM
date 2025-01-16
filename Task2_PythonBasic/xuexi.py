def read(input_path):
    path = input_path
    with open(path, 'r') as file:
        data = []
        for line in file :
            for item in line.split():
                try:
                    num = float(int(item,16))
                except ValueError:
                    num = float(item)
                data.append(num)
            return data

def pinjun(data,n):
    total = sum(data)
    average = total / n
    return average

def fangcha(data, average, n):
    total = 0
    for num in data :
        cha = (num - average) ** 2
        total += cha
    fc = total / n
    return fc

def write(put_path, n, average, fc):
    path = put_path
    with open(path ,'w') as file:
        file.write(f"num: {n}\n")
        file.write(f"average: {average}\n")
        file.write(f"fc: {fc}\n")

def main():
    input_path = "D:\\PlateRecognition\\PlateRecognition\\ok.txt"
    output_path_name = 'bb.txt'

    data = read(input_path)

    n = len(data)
    average = pinjun(data,n)
    fangchanum = fangcha(data, average, n)

    write(output_path_name, n, average, fangchanum)

    print("ok")

if __name__ == "__main__":
    main()
