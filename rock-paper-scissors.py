print('Rock–paper–scissors\n')
print('management in the game:')
print(' "1" - show rock')
print(' "2" - show scissors')
print(' "3" - show paper')
print()
np = input('enter your name: ')
import random
o = 'y'
dz = {0: 'rock', 1: 'scissors', 2: 'paper'}
pz = [[2, 1, 0], [0, 2, 1], [1, 0, 2]]
while (o == 'y')or(o == 'yes'):
    print()
    print(np, ', play three rounds', sep='')
    res = [[0, 0, 0, 0], [0, 0, 0, 0]]
    resr = [0, 0, 0]
    k = 3
    i = 0
    while (i < k)and(res[0][3] < 6)and(res[1][3] < 6):
        input()
        print('раунд ', i+1, sep='')
        print('Rock… Scissors… Paper… One… Two… Three!')
        print('rather, select the "sign" (1/2/3): ', end='')
        z = input()
        if (z == '1')or(z == 'rock'):
            res[0][i] = (0)
        elif (z == '2')or(z == 'scissors'):
            res[0][i] = (1)
        elif (z == '3')or(z == 'paper'):
            res[0][i] = (2)
        print(' you showed -', dz[(res[0][i])])
        res[1][i] = random.randint(0, 2)
        print(' computer showed -', dz[(res[1][i])])
        resr[i] = pz[(res[1][i])][(res[0][i])]
        if (resr[i] == 0):
            res[0][3] += 3
        elif (resr[i] == 1):
            res[1][3] += 3
        elif (resr[i] == 2):
            res[0][3] += 1
            res[1][3] += 1
        i += 1

    k = i
    input()
    print('Results of the game:')
    print('{:<8}'.format(''), end='')
    print('{:^15}'.format(np), end='')
    print('{:^15}'.format('computer'))
    for j in range(0, k):
        print('{:<2}'.format(j+1), '{:<6}'.format('round'), sep='', end='')
        for i in range(0, 2):
            print('{:^15}'.format(dz[res[i][j]]), end='')
        print()
    print()
    if (res[0][3]) > (res[1][3]):
        print('       ', np, 'won!')
    elif (res[0][3]) < (res[1][3]):
        print('        computer win')
    elif (res[0][3]) == (res[1][3]):
        print('        dead heat!')

    o = input('\nto start the game again? (y/n) ' )