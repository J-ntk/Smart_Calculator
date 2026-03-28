import math

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mult(num1,num2):
    return num1*num2

def div(num1,num2):

    if num2==0:
        return "Error: Can't devide by 0."
    elif num1==0:
        return "Error: Can't devide 0."
    else:
        return num1/num2
    
def pow(num1,num2):
    return num1 ** num2

def mod(num1,num2):
    return num1 % num2

def sqrt(num1):
    return math.sqrt(num1)