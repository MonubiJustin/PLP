# simple calculator program

value_a = int(input("Enter operand a: "))
operator = input("Enter the operator (+, -, /, *): ")
value_b = int(input("Enter operand b:"))

if operator == "+":
    print(f"{value_a} + {value_b} = {value_a + value_a}")
elif operator == "-":
    print(f"{value_a} - {value_b} = {value_a - value_b}")
elif operator == "*":
    print(f"{value_a} * {value_b} = {value_a * value_b}")
elif operator == "/":
    if value_b == 0:
        print("Zero Division Error")
    else:
        print(f"{value_a} / {value_b} = {value_a / value_b}")
else:
    print("Pick only the operators specified (+, -, /, *)...")