#GUESS NUM
import random
guess = random.randrange(1,100)
i = 0
x = 0
while guess != i:
    if x >= 3:
        print('YOU LOSE!')
        break 
    else:
            i = int(input('輸入數字1-100\n'))
            if i < guess:
                print('太小')
            elif i > guess:
                print('太大')
            else:
                print('bingo!')
            x += 1

    
