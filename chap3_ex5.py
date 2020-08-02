def test(n):
    x=(n * 5) + 1
    for i in range(x):
        if i%5==0:
            for i in range(x):
                if i== n*5:
                    print('+')
                else:
                    if i%5 == 0:
                        print('+',end=' ')
                    else:
                        print('-',end=' ' )
        else:
            for i in range (x):
                if i==n*5:
                    print ('|')
                else:
                    if i%5==0:
                        print('|',end=' ')
                    else:
                        print(' ',end=' ')

import pyinputplus as pyip
n= pyip.inputNum('how many rows and column?\n')
test(n)
