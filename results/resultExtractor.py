import re
import numpy as np
import csv

def printResult(n):
    sample_size = n

    filename = "mnist_" + str(sample_size)

    with open(filename) as f:
        lines = f.readlines()

    resultArray = []
    for i,j in enumerate(lines):
        temp0 = re.findall('test accuracy.*', j)
        if len(temp0) != 0:
            temp1 = re.findall('([^test accuracy].*)', str(temp0[0]))
            temp2 = float(temp1[0])
            resultArray.append(temp2)

    text = "r_" + str(sample_size) + "<-c("
    for i,j in enumerate(resultArray):
        if i != (len(resultArray)-1):
            text += str(j) + ","
        else:
            text += str(j)
    text += ")"

    #return(text)
    return(str(np.mean(resultArray)))

a = [5000, 10000, 15000, 20000, 25000, 30000, 40000, 50000]

printText = ""
for i in a:
    printText += printResult(i)
    printText += "\n"

#printText += "boxplot(r_5000, r_10000, r_15000, r_20000, r_25000, r_30000, r_40000, r_50000, names=c('5000', '10000', '15000', '20000', '25000', '30000','40000', '50000'))"

f = open('workfile.txt', 'w+')
f.write(printText)
