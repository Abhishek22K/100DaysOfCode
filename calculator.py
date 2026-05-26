a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Choose Operation\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division")
n = int(input("Enter choice: "))

if n==1:
    print(a+b)
    
elif n==2:
    print(a-b)

elif n==3:
    print(a*b)

elif n==4:
    print(a/b)

else:
    print("wrong choise")
