from random import*
for j in range(4,10):
    v = 0
    for i in range(10000):
        m = 10
        while m > 0:
            k = randint(0, 6) + randint(0, 6)
            if (k == 7):
                m += j
            else:
                m -= 1
            if (m >= 20):
                v += 1
                break
    if(v/10000>0.5):
        print('用户赢钱额度为{}时，保证总体赢钱'.format(j))
        break
