def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

print("Welcome to Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

try:
    choice = int(input("Enter choice (1-4):"))
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(num1, num2))
    elif choice == 2:
        print("Result:", subtract(num1, num2))
    elif choice == 3:
        print("Result:", multiply(num1, num2))
    elif choice == 4:
        print("Result:", divide(num1, num2))
    else:
        print("Invalid Choice")

except ValueError:
    print("Error: Please enter numbers only.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print("Unexpected Error:",e)




