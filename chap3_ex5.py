def test(n):
    x=(n * m) + 1
    for i in range(x):
        if i%m==0:
            for i in range(x):
                if i== n*m:
                    print('+')
                else:
                    if i%m == 0:
                        print('+',end=' ')
                    else:
                        print('-',end=' ' )
        else:
            for i in range (x):
                if i==n*m:
                    print ('|')
                else:
                    if i%m==0:
                        print('|',end=' ')
                    else:
                        print(' ',end=' ')

import pyinputplus as pyip
n= pyip.inputInt('how many rows and column?\n')
m=pyip.inputInt('how frequently di you want to see a +?\n')
test(n)
