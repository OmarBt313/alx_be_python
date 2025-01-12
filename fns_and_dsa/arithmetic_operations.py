



def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    if operation == 'subtract':
        return num1 - num2
    if operation == 'divide':
        if num1 and num2 != 0:
            return num1 / num2
        elif num2 == 0:
            print('invalid input')
    if operation == 'multiply':
        return num1 * num2

print (perform_operation(15,255,'subtract'))