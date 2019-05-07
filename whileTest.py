number = 23
runing = True

while runing:
    guess = int(input('Ведите целое число:'))

    if guess == number:
        print('Поздравляю вы угадали!')
        runing = False
    elif guess < number:
        print('Загадочное число выше введенного!')
    else:
        print('Загаданное число меньше введенного!')

else:
    print('Цыкл while закончен!')