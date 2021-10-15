#!\Python37 python
#!\Pythin 3.7.6 Oct, 2021
"""Solo.py
Purpose: Python script for play solo game from Simon Tatham's Portable Puzzle Collection
Developed by Robin Li robinli@live.ca
v1.0 Initial version
v2.0 Print out the steps
v3.0 Merge solo and sudoku
"""
import soloLib as solo 

def main():
    messageWelcome = "Welcome to play the Solo Games !"
    option = ""
    print ("       " + messageWelcome + " \n")
    while (True):
        dataList = []
        option = input("Please choose one options: 3(sukudo 3X3), 4(solo 4X4) or e(Exit)\n")
        if (option == " " or option == "0" or option.lower() == "e"):
            break
        else:
            if (option == ""):
                playGame(3)
            if (option == "3" or option == "4"):
                playGame(int(option))
    print ("\n Thank you !!! \n")
    

def playGame(n = 3):
    messageStart = " Let's start ...... "
    messageDone = "Congratulation! This Solo is solved !"
    messagePlus = "\nOh..., hard game, let's try more smarter algorithms!"
    messageFail = "\nNo..., too hard game! Need improve the algorithms"
    inputFile = input("Please enter Return to use the demo file or your file name: \n")
    if (inputFile == ""):
        if (n == 3) :
            inputFile = "sudoku.txt"
        else:
            inputFile = "solo4.txt"
    groups = solo.groupsGenerator(n)
    dataList = solo.readFile(inputFile, n)
    solo.displayFunc(messageStart, dataList)
    solo.allGroupsFunc(dataList, groups, 30, True)
    if (not solo.checkAllGroupsFunc(dataList, groups)):
        solo.displayFunc(messagePlus, dataList)
        dataList = solo.loopPlusFunc(dataList, groups)
    if (solo.checkAllGroupsFunc(dataList, groups)):
        solo.displayFunc(messageDone, dataList)
    else:
        solo.displayFunc(messageFail, dataList)
    return

    
if __name__ == "__main__":
    main()
