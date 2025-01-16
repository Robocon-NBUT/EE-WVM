def readf(rfile):
    with open(rfile,'r') as file:
        d=[]
        for l in file:
            d.extend(map(float,l.split()))
    return d
def writef(wfile,n,p,f):
    with open(wfile,'w') as file:
        file.write(f"num:{n}\n")
        file.write(f"average:{p}\n")
        file.write(f"variance:{f}")
def ps(d):
    add=0
    c=0
    add=float(add)
    c=int(c)
    for n in d:
        add+=n
        c+=1
    return add/c if c!=0 else 0
def fc(d,p):
    fm=0
    fz=0.0
    fz=float(fz)
    fm=int(fm)
    for n in d:
        fz+=(n-p)*(n-p)
        fm+=1
    return fz/fm if fm!=0 else 0
def main():
    rfile='resource.txt'
    wfile='result.txt'
    d=readf(rfile)
    if d:
        n=len(d)
        p=ps(d)
        f=fc(d,p)
        writef(wfile,n,p,f)
    else:
        print("error!")
if __name__=="__main__":
    main()