score=int(input("What's your score?"))
if(score<35):
    print("Poor Student")
elif(35<score and score<70):
    print("average student")
elif(score >70 and score<100):
    print("Good Student")
else:
    print("Invalid Score")
