"""
The function collection for solo and/or sokudo
"""

def copyList(inList):
    outList = []
    for i in inList:
        outList.append(i)
    return outList


def excludedGroupFunc(group, workingList):
    doneList = []
    for item in group:
        if (len(workingList[item]) == 1 ):
            doneList.append(workingList[item])
    for item in group:
        if (len(workingList[item]) != 1 ):
            for doneItem in doneList:
                workingList[item] = workingList[item].replace(doneItem,"")
    return workingList


def uniqueGroupFunc(group, workingList):
    notDoneList = allMemberList(group)
    notDoneString = ""
    for item in group:
        if (len(workingList[item]) == 1 ):
            if (workingList[item] in notDoneList):
                notDoneList.remove(workingList[item])
        else:
            notDoneString = notDoneString + workingList[item]
    for numString in notDoneList:
        if (notDoneString.count(numString) == 1):
            for item in group:
                if (workingList[item].count(numString) == 1):
                    workingList[item] = numString
    return workingList


def excludedAllGroupsFunc(workingList, groups):
    for i in range(0, len(groups)):
        excludedGroupFunc(groups[i], workingList)
    return workingList


def uniqueAllGroupsFunc(workingList, groups):
    for i in range(0, len(groups)):            
        uniqueGroupFunc(groups[i], workingList)
    return workingList


def allGroupsFunc(workingList, groups, maxLoop = 30, printStepsFlag = False):
    i = 1
    while (i < maxLoop):
        lastList = copyList(workingList)
        excludedAllGroupsFunc(workingList, groups)
        uniqueAllGroupsFunc(workingList, groups)
        if (printStepsFlag):
            for m in range(len(workingList)):
                if (len(workingList[m]) == 1 and len(lastList[m]) != 1):
                    print(str(m) + ":" + workingList[m] + " " , end = '')        
        if(workingList == lastList):
           print ("  Run " + str(i) + " loops")
           return workingList
        i = i + 1
    print ("Reach the set max loop: " + str(maxLoop))
    return workingList


def checkAllGroupsFunc(workingList, groups):
    for i in range(0, len(groups)):
        if (not checkGroupFunc(groups[i], workingList)):
            return False
    return True


def checkGroupFunc(singleGroup, workingList):
    for item in singleGroup:
        if (len(workingList[item]) != 1 ):
            return False
    return True


def allMemberList(group):
    tempList = []
    allMemberString = ""
    if (len(group) == 9):
        allMemberString = "123456789"
    if (len(group) == 16):
        allMemberString = "123456789abcdefg"
    for i in allMemberString:
        tempList.append(i)
    return tempList


def loopPlusFunc(workingList, groups, maxLoop = 30):
    for i in range(0, len(groups)):
        for item in groups[i]:
            if (len(workingList[item]) == 2):
                tempList = copyList(workingList)
                tempList[item] = workingList[item][0]
                allGroupsFunc(tempList, groups, maxLoop)
                if checkAllGroupsFunc(tempList, groups):
                    return tempList
                else:
                    tempList[item] = workingList[item][1]
                    allGroupsFunc(tempList, groups, maxLoop)
                    if checkAllGroupsFunc(tempList, groups):
                        return tempList
    return workingList


def printListIndex(n = 4):
    m = len(str(n**4))
    partLine = n * (m + 1) * "-" + "-+"
    print (n * partLine)
    number = 0
    gapList = []
    for k in range(1, n):
        gapList.append(k * n - 1)
    for i in range(0, n**2):
        for j in range(0, n**2):
            s = str(number)
            print(" " + (m-len(s)) * "0" + s, end = '')
            if ( j in gapList):
                print(" |", end = '')
            number = number + 1
        print(" |")
        if ( i in gapList):
                print (n * partLine)
    print (n * partLine)


def groupsGenerator(n = 2):
    totalGroups = []
    n2 = n ** 2
    for i in range(0, n2):
        group_row = []
        group_col = []
        for j in range(0, n2):
            group_row.append(i * n2 + j)
            group_col.append(j * n2 + i)
        totalGroups.append(group_row)
        totalGroups.append(group_col)
    for i in range(0, n):
        for j in range(0, n):
            m = i * n2 * n  + j * n
            group_box = []
            for k in range(0, n):
                for l in range(0, n):
                    group_box.append(m + k * n2 + l)
            totalGroups.append(group_box)
    return totalGroups


def displayFunc(message, dataList):
    maxNumber = len(dataList)
    n = int(maxNumber ** (1 / 4))
    n2 = n ** 2
    displayIndent = "          "
    displayLine = "+" + n* ( n * 2 * "-" + "-+")
    print ("       " + message + " \n")
    print (displayIndent + displayLine)
    for i in range(0, n2):
        print(displayIndent + "| ", end = '')
        for j in range(0, n2):
            v = dataList[n2 * i + j]
            if ( v != 0 and len(v) == 1):
                print(v + " ", end = '')
            else:
                print(". ", end = '')
            if ((j + 1) % n == 0):
                print("| ", end = '')
        print("")
        if ((i + 1) % n == 0):
                print (displayIndent + displayLine)
    print("\n")


def readFile(infile, level):
    n = level + 1
    m = level * n
    allMemberString = ""
    if (level == 3):
        allMemberString = "123456789"
    if (level == 4):
        allMemberString = "123456789abcdefg"
    with open(infile) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    workingList = []
    for i in range(0, m):
        if (i % n != 0):
            line = content[i]
            tempList = line.split(" ")
            for j in range(0, m - 1):
                if ((j + 1 ) % n != 0):
                    if (tempList[j] == "."):
                        workingList.append(allMemberString)
                    else:
                        workingList.append(tempList[j])
    return workingList



