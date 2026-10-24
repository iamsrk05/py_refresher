num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if (num1 > num2 and num1 > num3):
    print("Number 1 ")
elif(num2 > num1 and num2 > num3):
    print("Number 2")
elif(num1 == num2 and num2 == num3):
    print("no largest number")
elif(num1 == num2):
    if(num2 > num3):
        print("number 1&2 are largest.")
    else:
        print("Number 3")
elif(num2 == num3):
    if(num3 > num1):
            print("number 2&3 are largest.")
    else:
            print("Number 1")
elif(num1 == num3):
    if(num1 > num2):
            print("number 1&3 are largest.")
    else:
            print("Number 2")
else:
    print("Number 3")


    