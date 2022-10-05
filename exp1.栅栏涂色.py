def numWays(n,k):
    if (n<=0 or k<=0):
        return -1
    elif (n>1 and k==1):
        return -1
    elif (n==1 ):
        return k
    elif (n==2):
        return k*k
    else:
        pre = k*k
        ppre  = k
        current = k*k
        for i in range(3,n+1):
            current = ppre*(k-1)+pre*(k-1)
            ppre = pre
            pre = current
        return current
a = numWays(3,2)
print(a)



