# KBC game in python
import random, time
# print(quesAns)

def patternKBC(m=4):
    for i in range(1,m):
        print ("KK", end="")
        for j in range (m,0,-1):
            if j==i: print(' KK', end='')
            else: print(" ", end='')
        time.sleep(0.25)
        print()

    for i in range(1,m+1):
        print ("KK", end="")
        for j in range (1,m+2):
            if j==i: print(' KK', end='')
            else: print(" ", end='')
        time.sleep(0.25)
        print()

def randoQuesAnsSeriesGenerator(quesDataSet):
    qusOptSeries = []
    for i in quesDataSet:
        qusOptSeries.append(i[1])
    random.shuffle(qusOptSeries)

    return qusOptSeries

def askQues(quesDataSet, quesID): # Returns the Question string with given question ID from the dataset
    for quesGrp in quesDataSet:
        if quesID in quesGrp:
            return quesGrp[0]
    return

def accessOptionsList(quesDataSet, quesID): # Returns the Sub List containing Options within a specific question group,
    for quesGrp in quesDataSet:             # identifiable by the Question ID
        if quesID in quesGrp:
            return quesGrp[2]
    return

def provideOpt(optList, optID): # Returns the option string for provided option ID
    for i in optList:
        if optID in i:
            return i[0]
    return

def obtainRightAnswerID(quesDataSet, quesID):
    for quesGrp in quesDataSet:
        if quesID in quesGrp:
            return quesGrp[-1]
    return

def checkAnswer(userChoice, randomOptionList, quesDataSet, quesID):
    optIDfrmUserChoice = randomOptionList["ABCD".index(userChoice)]
    if optIDfrmUserChoice == obtainRightAnswerID(quesDataSet, quesID):
        return True
    return False
    

def main():
    print(("welcome to kaun banega crorepati for chemistry\n").title())
    patternKBC()
    print()


    userName = input("What's your name Player? ").title()
    userBal = 0
    print("\nwelcome".title(), userName, end="")
    time.sleep(2)

    print('\n\nThere will be 5 questions from chemistry.')
    time.sleep(2)
    print('You will win INR 500 times the number of questions answered correctly.')
    time.sleep(4)
    print('All the best player.\n''')

    time.sleep(2)
    confirmation = input("\nPress Enter to Continue\n")
    

    quesAns = [
        [
            "What is the first atom in the periodic table?", 100023,
            [
                ["Neon", 100023.1],
                ["Lithium", 100023.2],
                ["Rutherfordium", 100023.3],
                ["Hydrogen", 100023.4]
            ],
            100023.4
        ],
        [
            "Which is the most abundant element in the earth's atmosphere?", 100024,
            [
                ["Oxygen", 100024.1],
                ["Hydrogen", 100024.2],
                ["Nitrogen", 100024.3],
                ["Water Vapour", 100024.4]
            ],
            100024.3
        ],
        [
            "What is the formula for Benzene?", 100025,
            [
                ["CH4", 100025.1],
                ["C2H2", 100025.2],
                ["C6H6", 100025.3],
                ["CO2", 100025.4]
            ],
            100025.3
        ],
        [
            "Which acid is found in our stomachs?", 100026,
            [
                ["H2SO4", 100026.1],
                ["HCl", 100026.2],
                ["HNO3", 100026.3],
                ["H2S2O8", 100026.4]
            ],
            100026.2
        ],
        [
            "What element is found in our bones?", 100027,
            [
                ["Clacium", 100027.1],
                ["Sodium", 100027.2],
                ["Rubidium", 100028.3],
                ["Carbon", 100029.4]
            ],
            100027.1
        ]
    ]
    
    askSeries = (randoQuesAnsSeriesGenerator(quesAns))
    # print (askSeries)
    # a=randoQuesAnsSeriesGenerator(accessOptionsList(quesAns, askSeries[1]))
    # print(a)
    # print (provideOpt(accessOptionsList(quesAns, askSeries[1]), a[0]))
    

    for quesID in askSeries:

        print(askQues(quesAns, quesID), "\n")
        time.sleep(1)

        #options = accessOptionsList(quesAns, quesID) # Gets the list containing Option String and Option ID
        randomOptionList = randoQuesAnsSeriesGenerator(accessOptionsList(quesAns, quesID))
        # print(randomOptionList)
        # print (options, "\n\n")
        
        opt = 'ABCD'
        j=0

        for i in randomOptionList:
            print(opt[j]+")", provideOpt(accessOptionsList(quesAns, quesID), i)) # Option Sub List's element at index 1 contains the option ID.
            j=j+1
            time.sleep(0.25)


        while(True):
            userChoice = (input("\nChoose the Option: A, B, C or D? ")).upper()
            confirmation = (input("ARE YOU SURE? SHALL WE LOCK OPTION "+userChoice+" Y/N? ")).upper()
            # print (confirmation)
            if confirmation == "Y": break
            else: continue

        print()
        patternKBC()

        if checkAnswer(userChoice, randomOptionList, quesAns, quesID):
            userBal += 500
            print("\nCorrect Answer!!\nYou Have Won INR 500 for this Question\nYour Balance is:", userBal, "\n\n")
        else:
            print("\nIncorrect Answer!\nYour Balance remains", userBal, "\n\n")

        confirmation = input("Press Enter to Continue\n")
        patternKBC()
        print("============================\n\n")

    print("Your Game has ended", userName)
    print("You Won INR", userBal)
    time.sleep(2)
    patternKBC()

main()