def getKthMagicNumber(k):
    get_k = 0
    num = 1
    b = []



    while get_k < k:
        a = []
        i=1
        while i <= num:
            if num % i == 0:
                a.append(i)
            i += 1
        i -=1
        if num==1:
            pass
        elif 1<num<=7:
            a.remove(1)
        else:
            a.remove(1)
            a.remove(num)
        if len(a) > 3 or len(a) == 0:
            num += 1
            continue
        if len(a) == 3:
            aa = list(set(a))

            if aa != [3, 5, 7]:
                num += 1
                continue
            else:
                b.append(i)
                get_k += 1
        if len(a) == 2:
            bb = list(set(a))

            if bb == [3, 5] or bb == [3, 7] or bb == [5, 7]:
                b.append(i)
                get_k += 1
            else:
                num += 1
                continue
        if len(a) == 1:
            if num==1:
                b.append(num)
                num += 1
                get_k += 1
                continue
            cc = list(set(a))
            if cc[0] == 3 or cc[0] == 5 or cc[0] == 7:
                b.append(i)
                get_k += 1
            else:
                num += 1
                continue
        num += 1
    return b

a = getKthMagicNumber(1)
print(a)