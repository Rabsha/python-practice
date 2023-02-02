# 45 * 3 = 555 , 56 + 9 = 77 , 56/6 = 4
operator = input()
firstInput = input()
secondInput = input()
if operator == '+':
    if int(firstInput) == 56 and int(secondInput) == 9:
        print("77")
    else:
        total = int(firstInput) + int(secondInput)
        print(total)
elif operator == '-':
    total = int(firstInput) - int(secondInput)
    print(total)
elif operator == '*':
    if int(firstInput) == 45 and int(secondInput) == 3:
        print("555")
    else:
        total = int(firstInput) * int(secondInput)
        print(total)
elif operator == '/':
    if int(firstInput) == 56 and int(secondInput) == 6:
        print("4")
    else:
        total = int(firstInput) / int(secondInput)
        print(total)
