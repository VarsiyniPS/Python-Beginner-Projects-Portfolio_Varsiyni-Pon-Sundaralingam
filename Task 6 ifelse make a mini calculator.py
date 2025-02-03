a=int(input("a:"))
b=int(input("b:"))
operation=input("do you want to add/sub/mul/div?")
add=(a+b)
sub=(a-b)
mul=(a*b)
div=(a/b)
if(operation == "add"):
    print(add)
elif(operation == "sub"):
    print(sub)
elif(operation == "mul"):
    print(mul)
elif(operation == "div"):
    print(div)
else:
    print("Invalid Operation")

    
