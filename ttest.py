# b = 10
# a = b
# b = 20
# print(a)
# c = [5,6,7,8,9]
# d = c.pop(0)
# print(d)
for i in range(1,10):
    print(i)
n = 10
n>>=1
print(n)
n = 5
cc = [1,2,3,4]
if n  not in cc :
    print("error")


def rotatedDigits(n):
    if not n:
        return 0
    right_1 = [2, 5, 6, 9]
    right_2 = [2,5,6,9,1,0,8]
    sum = 0
    nn = []

    def juge_a(uu):
        num = uu
        while num > 0:
            num1 = num % 10
            if num1 not in right_1:
                return 0
            else:
                num = num // 10
        nn.append(uu)
        return 1

    def juge_b(uu):
        num = uu
        while num > 0:
            num1 = num % 10
            if num1 not in right_2:
                return 0
            else:
                num = num // 10
        nn.append(uu)
        return 1

    for i in range(1, n + 1):
        if i<10:
            c = juge_a(i)
        else:
            c = juge_b(i)

        sum = sum + c
    print(nn)
    return sum

cc = rotatedDigits(857)
print(cc)