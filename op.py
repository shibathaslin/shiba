num = int(input("Enter any number: "))
if num<0:
    print("Error, Invalid input")
elif num%2==0:
    print(num, "is an even number")
elif num%2==1:
    print(num, "is an odd number")
