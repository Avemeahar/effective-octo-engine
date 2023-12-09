number1 = int(input('Введите первое число: '))
operator = input('Введите действие: ')
number2 = int(input('Введите второе число: '))

if operator == '+':
    print(number1 + number2)
elif operator == '-':
    print(number1 - number2)
elif operator == '*':
    print(number1 * number2)
elif operator == '/':
    print(number1 / number2)
elif operator == '//':
    print(number1 // number2)
elif operator == '**':
    print(number1 ** number2)
elif operator == '%':
    print(number1 % number2)
else:
    print("Ошибка! Доступные действия: +,-,*,/,//,**,%")
