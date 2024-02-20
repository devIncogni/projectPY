# Match Case Statements
# A Voting Program using match case

x = int(input("Who do you want to vote? "))

match x:

    case 0: 
        print("Voted None")
    case 1:
        print("Voted Candidate 1")
    case 2:
        print("Voted Candidate 2")
    case 3:
        print("Voted Candidate 3")
    case 4:
        print("Voted Candidate 4")
    case _ if x != 0:
        print("Invalid Choice") 