#!\Python33 python
#!\Python 3.6.0
"""Sudoku.py Ver 2.0.3
# Remove check group size
Developed by Robin Li robinli@live.ca
"""

def main():
    global groups
    dataList = []
    groups = groupGenerator()
    dataList = readFile("board")
    messageWelcome = "Welcome to play the Sudoku Games !"
    messageDone = "Congratulation! This Sudoku is solved !"
    messagePlus = "Oh.. Hard game, and we need more smarter algorithms!"
    display(messageWelcome,dataList)
    dataList = loop(dataList)
    if (doneLoop(dataList)):
        display(messageDone,dataList)
    else:
        display(messagePlus,dataList)
        dataList = loopPlus(dataList)
        if (okLoop(dataList)):
            display(messageDone,dataList)


def display(message,dataList):
    displayIndent = "          "
    print ("       " + message + " \n")
    print (displayIndent + "+-------+-------+-------+")
    for i in range(0,9):
        print(displayIndent + "| ", end = '')
        for j in range(0,9):
            v = dataList[9*i+j]
            if ( v != 0 and len(v) == 1):
                print(v + " ", end = '')
            else:
                print(". ", end = '')
            if (j == 2 or j == 5):
                print("| ", end = '')
        print("|")
        if (i == 2 or i == 5):
                print (displayIndent + "+-------+-------+-------+")
    print (displayIndent + "+-------+-------+-------+\n\n")


def readFile(infile):
    with open(infile) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    data = []
    for i in range(0,12):
        if (i % 4 != 0):
            line = content[i]
            lineList = line.split(" ")
            for j in range(0,11):
                if (j != 3 and j != 7):
                    if (lineList[j] == "."):
                        data.append("123456789")
                    else:
                        data.append(lineList[j])
    return data


def nineNumberList():
    numbersList = []
    for i in range(1,10):
        numbersList.append(str(i))
    return numbersList


def groupGenerator():
    totalGroups = []
    for i in range(0,9):
        group = []
        for j in range(0,9):
            group.append(i*9+j)
        totalGroups.append(group)
    for i in range(0,9):
        group = []
        for j in range(0,9):
            group.append(j*9+i)
        totalGroups.append(group)
    for i in range(0,3):
        for j in range(0,3):
            m = i*27+j*3
            group = []
            for k in range(0,3):
                for l in range(0,3):
                    group.append(m+k*9+l)
            totalGroups.append(group)
    return totalGroups

def excludedFunction(group,data):
    doneList = []
    for i in group:
        if (len(data[i]) == 1):
            doneList.append(data[i])
    for i in group:
        if (len(data[i]) != 1):
            for doneItem in doneList:
                data[i] = data[i].replace(doneItem,"")
    return data


def uniqueFunction(group,data):
    notDoneList = nineNumberList()
    notDoneString = ""
    for i in group:
        if (len(data[i]) == 1):
            if (data[i] in notDoneList):
                notDoneList.remove(data[i])
        else:
            notDoneString = notDoneString + data[i]
    for numString in notDoneList:
        if (notDoneString.count(numString) == 1):
            for i in group:
                if (data[i].count(numString) == 1):
                    data[i] = numString                
    return data


def groupDone(group,data):
    doneFlag = True
    for i in group:
        if (len(data[i]) != 1):
            doneFlag = False                
    return doneFlag


def excludedLoop(data):
    for i in range(0,27):
        data = excludedFunction(groups[i],data)
    return data


def uniqueLoop(data):
    for i in range(0,27):            
        data = uniqueFunction(groups[i],data)
    return data


def doneLoop(data):
    doneFlag = True
    for i in range(0,27):
        groupFlag = groupDone(groups[i],data)
        if (groupFlag == False):
            doneFlag = False
    return doneFlag


def loop(data):
    i = 1
    while (doneLoop(data) == False and i < 10):
        data = excludedLoop(data)
        data = uniqueLoop(data)
        i = i + 1
    return data


def loopPlus(data):
    okFlag = False
    for i in range(0,27):
        group = groups[i]
        for item in group:
            if (len(data[item]) == 2):
                tempData = copyList(data)
                tempData[item] = data[item][0]
                tempData=loop(tempData)
                if okLoop(tempData):
                    data = tempData
                    okFlag = True
                    break
                else:
                    tempData[item] = data[item][1]
                    tempData=loop(tempData)
                    if okLoop(tempData):
                        data = tempData
                        okFlag = True
                        break
        if (okFlag):
            break
    return data

def copyList(inList):
    outList = []
    for i in inList:
        outList.append(i)
    return outList
    

def groupOK(group,data):
    okFlag = True
    numberList = nineNumberList()
    for i in group:
        if (len(data[i]) != 1):
            okFlag = False
        else:
            if (data[i] in numberList):
                numberList.remove(data[i])
    if (len(numberList) != 0):
        okFlag = False
    return okFlag


def okLoop(data):
    okFlag = True
    for i in range(0,27):
        groupFlag = groupOK(groups[i],data)
        if (groupFlag == False):
            okFlag = False
    return okFlag


if __name__ == "__main__":
    main()
