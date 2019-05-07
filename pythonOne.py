#msg = input('Введите сообщение:') 
#print('Ваше сообщение: ', msg)
#vodka = {'name': 'Smirnoff', 'volume': 0.7, 'price': 1000}
#print(vodka['name'])
#bayList = []
#bayList.append(vodka)
#print(vodka['price'])
#print(bayList)
#vodka.pop('volume')
#print(bayList)
#vodka['volume'] = 0.7
#print(bayList)

#if 5<3:
#    print('5 is indeed greater than 2')
#else:
#    print('5 is not greater than 2')

#name = 'Vedim'

#if name == 'Ola!':
#    print('Hey Ola')
#elif name == 'Vedim!':
#   print('Hey Vedim')
#else:
#    print('Hey Ananimus!')
#def volTest(volume):

#    if volume == 20:
#        print('It\'s kinda queit.')
#    elif 20 <= volume < 40:
#        print('It\'s nice for background music')
#    elif 40 <= volume < 60: # Программа выполнит это условие 
#        print('Perfect, I can hear all the details')
#    elif 60 <= volume < 80:
#        print('Nice for parties')
#    elif 80 <= volume < 100:
#        print('My ears are hurting!')    

#def volSet(volume):

#   if 20 < volume or volume < 80:
#       volume = 50
#       print("That's batter!")

#def hiTest():
#    print('Hi there!')
#    print('How are you!')



#def hi(name):
#    if name == 'Ola':
#        print("Hi " + name + '!')
#    elif name == 'Vedim':
#        print("Hi " + name + '!')    
#    else:
#        print('Hi ananymus')
        


#hi('huy')

#volTest(30)
#volSet(10)



def hi(name):
    print("Hi " + name + '!')

girls = ['Rachel', 'Monica', 'Phoebo', 'Ola', 'You']

for name in girls:
    hi(name)
    print('Next girl: ')

for i in range(1, 10):
    print(i)
