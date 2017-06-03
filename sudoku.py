#!\Python33 python
#!\Pythin 3.4.3 Aug, 2015
"""Sudoku.py
Purpose: Python script for play sudoku game
Developed by Robin Li robinli@live.

Release Note:
V0: No module
"""


def main():

# initialize dataList
    dataList=[]
    dataList = readFile("board.txt")
    display(dataList)
    tempList = toTempList(dataList)
    data =loop(tempList)
    data =loop(data)
    data =loop(data)
    data =loop(data)
    data =loop(data)
    data =loop(data)
    data =loop(data)
    data =loop(data)
    display(data)

def display(dataList):
    menuIndent = "          "
    print ("       Welcome to play the Sudoku Games ! \n")
    print (menuIndent + "+-------+-------+-------+")
    for i in range(0,9):
        print(menuIndent + "| ", end='')
        for j in range(0,9):
            v = dataList[9*i+j]
            if ( v != 0):
                print(v+" ", end='')
            else:
                print(". ", end='')
            if (j==2 or j==5):
                print("| ", end='')
        print("| ")
        if (i==2 or i==5):
                print (menuIndent + "+-------+-------+-------+")
    print (menuIndent + "+-------+-------+-------+")


def readFile(infile):
    with open(infile) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    data = []
    for i in range(0,12):
        if (i % 4 != 0):
            line = content[i]
            data1 = line.split(" ")
            for j in range(0,11):
                if (j !=3 and j!=7):
                    data.append(data1[j])
    return data


def nineNumberList():
    tempList = []
    for i in range(1,10):
        tempList.append(str(i))
    return tempList


def toTempList(inList):
    outList = []
    for x in inList:
        if (x=="."):
            outList.append("123456789")
        else:
            outList.append(str(x))
    return outList
    

def excludedFunction(groupList,data):
    if (len(groupList) == 9):
        doneList = []
        for item in groupList:
            if (len(data[item]) ==1 ):
                doneList.append(data[item])
        for item in groupList:
            if (len(data[item]) !=1 ):
                for doneItem in doneList:
                    data[item] = data[item].replace(doneItem,"")
    return data


def uniqueFunction(groupList,data):
    if (len(groupList) == 9):
        notDoneList = nineNumberList()
        notDoneString = ""
        for item in groupList:
            if (len(data[item]) ==1 ):
                notDoneList.remove(str(data[item]))
            else:
                notDoneString = notDoneString + data[item]
        for numString in notDoneList:
            if (notDoneString.count(numString) ==1):
                for item in groupList:
                    if (data[item].count(numString)==1):
                        data[item]=numString                
    return data


def excludedLoop(data):
    for i in range(0,9):
        group = []
        for j in range(0,9):
            group.append(i*9+j)
        data = excludedFunction(group,data)

    for i in range(0,9):
        group = []
        for j in range(0,9):
            group.append(j*9+i)
        data = excludedFunction(group,data)

    for i in range(0,3):
        for j in range(0,3):
            m = i*27+j*3
            group = []
            for k in range(0,3):
                for l in range(0,3):
                    group.append(m+k*9+l)
            data = excludedFunction(group,data)
    return data

def uniqueLloop(data):
    for i in range(0,9):
        group = []
        for j in range(0,9):
            group.append(i*9+j)
        data = uniqueFunction(group,data)

    for i in range(0,9):
        group = []
        for j in range(0,9):
            group.append(j*9+i)
        data = uniqueFunction(group,data)

    for i in range(0,3):
        for j in range(0,3):
            m = i*27+j*3
            group = []
            for k in range(0,3):
                for l in range(0,3):
                    group.append(m+k*9+l)
            data = uniqueFunction(group,data)
    return data

def loop(data):
    data = excludedLoop(data)
    data = uniqueLloop(data)
    return data


if __name__ == "__main__":
    main()
