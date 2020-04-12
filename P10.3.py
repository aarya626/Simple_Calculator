# program to make a calculator of just four operators.

print(" ----------------------------------Welcome to A_calculator---------------------------")
def calculator():
    """ This function work as a calculator
         but it only work in 2 numbers and in + - / * only """
    choice = input(" Enter your choice(+,-,/,*):- ")

    num1 = int(input(" Enter first number:- "))

    num2 = int(input(" Enter second number:- "))

    def add2num(num1,num2):
        sum = num1+num2
        return sum

    add = add2num(num1,num2)


    def sub2num(num1,num2):
        sub = num1-num2
        return sub

    minus = sub2num(num1,num2)
    #print(minus)

    def mul2num(num1,num2):
        multi = num1*num2
        return multi

    mul = mul2num(num1,num2)
    #print(mul)

    def div2num(num1,num2):
        divide = num1/num2
        return divide

    div = div2num(num1,num2)
    #print(div)

    if choice == '+':
        print(" Sum of given number is ",add)

    if choice == '-':
        print(" Substraction of given number is ",minus)

    if choice == '*':
        print(" Multiplication of given number is ",mul)

    if choice  == '/':
        print(" Division of given number is ",div)
while(1):

    calculator()

    run = input(" Do you want to continue?(y/n):- ")

    if run == 'y' or run == 'Y':
        calculator()

    elif run == 'n' or run == 'N':
        exit()


#print(calculator .__doc__)