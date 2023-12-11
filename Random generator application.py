import random

a = random.randint(0,10)
print('Компьютер загадал число от 0 до 10.')
b = int(input('Попробуйте угадать это число: '))
while b != a:
    a = random.randint(0, 10)
    print('Вы ошиблись. Попробуйте еще раз: ','\n',int(input('Повторите ввод: ')))
if a == b:
    print('Congratulations!!!')