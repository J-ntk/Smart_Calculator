"""SRT CALCULATOR v1.0"""


from operations import add,sub,mult,div,pow,mod,sqrt
import re

HISTORY_FILE = "history.txt"


def save_history(entry):
    with open("history.txt","a", encoding="utf-8") as file:
        file.write(entry+"\n")

def read_history():
    print("\n===== CALCULATION HISTORY =====")
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if not lines:
                print("No history yet.")
            else:
                for line in lines:
                    print(line.strip())
    except FileNotFoundError:
        print("No history file found.")
    print("===============================\n")

"""
        ===== v1.0 Code =====

def get_number(prompt): 
    while True:
        value = input(prompt)
        if value.lower() == "q":
            return "quit"
        if value.lower() == "h":
            read_history()
            continue
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Try again.")

"""

def root_func(match):
    num = float(match.group(1))
    return str(sqrt(num))



"""
            ===== v1.0 Code =====


def get_operation():
    while True:
        op = input("Choose (+, -, *, /, **, %, root) or 'h' to read History or 'q' to quit: ").lower()
        if op == "q":
            return "quit"
        if op in ["+", "-", "*", "/", "**", "%", "root" , "q" , "h"]:
            return op
        print("Invalid operation. Try again.")

"""

def safe_eval(expression):

    expression = re.sub(r'root\(([^)]+)\)' , root_func, expression)

    if not re.match(r'^[0-9+\-*/%.() ]+$', expression):
        raise ValueError("Invalid Characters.")
    
    return eval(expression)

def calculator():       
    
    print ("===== SMRT CLTR =====")

    print("You can type full expressions like: 5 + 3 * 2 - 4")
    print("Use root(number) for square root, e.g., root(9)")
    print("Type 'q' to quit or 'h' to view history.")


    while True:

        """

                    ===== v1.0 Code =====


        num1 = get_number("Enter first number (or 'h' to read History or 'q' to quit): ")
        if num1 == "quit":
            print("Thank you for using me... shutting down...")
            break

        operation = get_operation()
        if operation == "quit":
            print("Thank you for using me... shutting down...")
            break


        if operation != "root":
            num2 = get_number("Enter second number (or 'h' to read History or 'q' to quit): ")
            if num2 == "quit":
                print("Thank you for using me... shutting down...")
                break
        else:
            num2 = None
                          

        if operation == "+":
            result = add(num1,num2)
        elif operation == "-":
            result = sub(num1,num2)
        elif operation == "*":
            result = mult(num1,num2)
        elif operation == "/":
            result = div(num1,num2)
        elif operation == "**":
            result = pow(num1,num2)
        elif operation == "%":
            result = mod(num1,num2)
        elif operation == "root":
            result = sqrt(num1)
        else:
            print("Invalid Operation")
            continue
        
        if operation == "root":
            output = f"√({num1}) = {result}"

        else:
            output = f"{num1}{operation}{num2} = {result}"

        print("Result:", result)


        save_history(output)

        
        """


        expr = input("Enter expression: ").lower()
        
        if expr == "q":
            print("Thank you for using me... shutting down...")
            break
        elif expr == "h":
            read_history()
            continue

        try:
            result = safe_eval(expr)
            print("Result:", result)
            save_history(f"{expr} = {result}")
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    calculator()