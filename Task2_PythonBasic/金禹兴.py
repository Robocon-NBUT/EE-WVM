import numpy as np
def file_data(filePath):
    with open(filePath,'r') as file:
        data = []
        for line in file:
            parts = line.split()
            for part in  parts:
                data.append(float(part))
        return data
def calc(data):
    length = len(data)
    avger = np.average(data)
    var = np.var(data)
    return length,avger,var
def writeFile(filePath,len,avger,var):
    with open(filePath,'w')as file:
        file.write(f"DataCount:{len}\n")
        file.write(f"DataAverge:{avger}\n")
        file.write(f"DataVar:{var}\n")

inputfile = "notebook.txt"
outputfile = "newbook.txt"
data = file_data(inputfile)
length,avger,var = calc(data)
writeFile(outputfile,length,avger,var)
  

    

