import calculator_art

print(calculator_art.logo)

def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def exponent(num1,num2):
    return num1**num2

operations={"+":add,
            "-":subtract,
            "/":divide,
            "*":multiply,
            "^":exponent}

def calc():
    num1=float(input("What's the fist number? "))
    for symbol in operations:
        print(symbol)

    cont=True
    while cont==True:
        operation_symbol=input("Pick an operation: ")
        num2=float(input("What's the next number? "))

        if operation_symbol=="/" and num2==0:
            print("Error")
            break

        result=operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")=="y":
            num1=result
        else:
            cont==False
            calc()

calc()



