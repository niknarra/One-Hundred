# Day 10 - Jun 18 '24
# Calculator Program

logo=r''' 
_____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /       | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   _|  | || |    / /     | || |    | |       | || |  / .'   _|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____    | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |   '.___.'  | || | _/ /     _ | || |   _| |__/ |  | || |   '.___.'  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|'''
ops = '''+
-
*
/'''

def calculate(num1,num2,op):
    if op=='+':
        res = num1+num2
        return res
    elif op=='-':
        res = num1-num2
        return res
    elif op=='*':
        res = num1*num2
        return res
    elif op=='/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Unsupported operation."

calculating = True

print(logo)
num1 = float(input("What's the first number?: "))

while calculating:
    op = input(f"{ops}\nPick an operation: ")
    num2 = float(input("What's the next number?: "))
    res = calculate(num1,num2,op)
    print(f"{num1:.1f} {op} {num2:.1f} = {res:.1f}")
    toContinue = input(f"Type 'y' to continue calculating with {res:.1f}, or type 'n' to start a new calculation: ")
    
    if toContinue=='y':
        calculating = True
        num1 = res
    elif toContinue=='n':
        num1 = round(int(input("What's the first number?: ")),1)
    else:
        break
