def add(x, y):

    return x + y

def subtract(x, y):

    return x - y

def multiply(x, y):

    return x * y

def divide(x, y):

    return x / y

def square(x,y=0):

    return x*x 

    

def sqr_root(x,y=0):

    return x**0.5

print("Select operation.")

print("1.Add")

print("2.Subtract")

print("3.Multiply")

print("4.Divide")

print("5.square")

print("6.sqr_root")

while True:

    choice = input("Enter choice(1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4','5','6'):

        num1 = float(input("Enter first number: "))

        num2 = float(input("Enter second number: "))

        if choice == '1':

            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':

            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':

            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':

            print(num1, "/", num2, "=", divide(num1, num2))

            

        elif choice == '5':

            print(num1,"*",num1,"=",

                 square(num1,num1))

                 

        elif choice =='6':

            print(num1,"*","*",0.5,"=",

                 sqr_root(num1))

            

        break

    else:

        print("Invalid Input")
