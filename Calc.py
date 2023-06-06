def add(n1, n2):                                  #creating functions
    return n1+n2
def subtract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2

operations = {'+':add, '-':subtract, '*':multiply, '/':divide}          #storing functions in dictionary
num1=int(input("Enter num1 :"))
for sign in operations:
    print(sign)
op=input("Select operation :")
actualop=operations[op]                                                 #retrieving functions
num2=int(input("Enter num2"))
print("Result is", actualop(num1, num2))

