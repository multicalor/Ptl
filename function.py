import random

def c2n():
    A = input('Введите число 1: ')
    if len(A) == 0:
        rangeA = 100
    else:
        rangeA = int(A)

    
    B = input('Введите число 2: ')
    if len(B) == 0:
        rangeB = 100
    else:
        rangeB = int(B)


    resalt = True
    h = 0

    while resalt:
        h+=1
        print('Счетчик', h)

        c = random.randrange(1,9)
        d = random.randrange(1,9)

        f = c + d
        g = d + random.randrange(1,9)

        print(f)
        print(g)

        a = random.randrange(1, rangeA, f)
        b = random.randrange(1, rangeB, g)

        print(a,b)

        if a == b:
            resalt = False
            print('Поздравлю, случайные числа сошлись!')
        else:    

            q = input("'q'  для выхода:  ")
            

            if  q == 'q':
                resalt = False
                print('Вы отказались от игры!')

#c2n()            

#def printMax(a,b):
#    if a > b:
#        print(a, 'первое число максимально')
#    elif a == b:
#        print(a, 'оба числа ронвы', b)
#    else :
#        print(b, 'второе число максимально')        


    


