print("Enter your numbers")
while True:
        try:
            result =int(input())
            result=float(result)
            break
        except ValueError:
            print("Invalid Number try again")
while True:
    ch=str(input())
    if(ch=='='):
        break
    if ch not in('+','-','*','/'):
        print("Invalid input \n try again from entering the operator")
        continue
    while True:
        try:
            a=int(input())
            result=float(result)
            break
        except ValueError:
            print("Invalid Number try again")
    if(ch=='+'):
        result= result+a
    elif(ch=='-'):
        result=result-a
    elif(ch=='*'):
        result=result*a
    elif(ch=='/'):
        if(a==0):
            print("Cant devide by 0")
        else:
            result=result/a

print(result)