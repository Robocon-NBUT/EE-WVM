


def get_data(input_path):
    with open(input_path,'r') as file:
        data = []
        for x in file:
            data.extend(map(float,x.split()))
    return data

def average_data(data):
    tot = count = 0
    for i in data:
        tot+=i
        count+=1
    return tot/ count

def calculate_data(data,average):
    tot = count= 0
    for i in data:
        count+=1
        tot+=(average-i)**2
    tot/=count
    return tot
def main():
    input_path = r"C:\Users\江鸟\Desktop\赵鸿波\作业二\simple.txt"
    output_path = r"C:\Users\江鸟\Desktop\赵鸿波\作业二\result.txt"
    a = get_data(input_path)
    average = average_data(a)
    cal = calculate_data(a,average)

    fo = open(output_path,'w')
    fo.write(f"count: {a.__len__()}\n")
    fo.write(f"average: {average}\n")
    fo.write(f"calculate:{cal}\n")

if __name__ =="__main__":
    main()