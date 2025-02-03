s1=int(input("Enter the your mark for your 1st subject:"))
s2=int(input("Enter the your mark for your 2nd subject:"))
s3=int(input("Enter the your mark for your 3rd subject:"))
s4=int(input("Enter the your mark for your 4th subject:"))
s5=int(input("Enter the your mark for your 5th subject;"))

subjectsum=(s1+s2+s3+s4+s5)
average=(subjectsum/5)
print(average)
if(average<35):
    print("Additional class is required")
else:
    print("You're good to go")
    


