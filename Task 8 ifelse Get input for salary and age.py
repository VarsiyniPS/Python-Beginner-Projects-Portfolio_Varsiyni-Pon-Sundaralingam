salary=int(input("Enter your salary:"))
age=int(input("Enter your age:"))
if(salary>=20000 or age<=25):
    loanamount=int(input("Enter your loan amount:"))
    if(loanamount<=50000):
        print("You Are Eligible for Loan")
    else:
        print("Maximum Loan Amount is $50,000")       
else:
    print("not eligible for loan")
        
