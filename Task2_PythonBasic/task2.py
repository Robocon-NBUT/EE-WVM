def ave(data,n):
    sum=0
    for value in data:
        sum+=value
    return sum/n
def var(data,n):
    vsum=0
    for value in data:
        vsum+=(value-ave(data,n))**2
    return vsum/n
def main():
    rfile='resource.txt'
    wfile='result.txt'
    values=[4,5,3,7,4,8,3]
    data=[]
    with open(rfile,"w") as file1:
        for i in range(len(values)):
            s=str(values[i])   
            file1.write(s+" ") 
    with open(rfile,"r") as file1:
        for l in file1:
            data.extend(map(int,l.split()))
    n=len(data)
    with open(wfile,"w") as file2:
        file2.write(f"num:{n}\n")
        file2.write(f"average:{ave(data,n)}\n")
        file2.write(f"variance:{var(data,n)}\n")
if __name__ =="__main__":
    main()

            