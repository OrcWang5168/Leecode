class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")


class Class3(Class1):
    def m(self):
        print("In Class3")


class Class4(Class2, Class3):
    def __init__(self):

        super(Class3,self).m()

a = Class4()
print(Class4.__mro__)
#调用的mro决定执行的顺序

aa = [1,2,5,6]
b=aa.pop()
print(b)

c = [None]
# while c:
#     print(a)


g = None

print(bool(None))
print(bool([]))

print(id(g))
print(id(None))
if None != []:
    print("是的")
if g is None:
    print("好")


def minArray(numbers) -> int:
    low, high = 0, len(numbers) - 1
    mid = low + (high - low) // 2
    if high==low:
        return numbers[low]
    if numbers[mid] > numbers[high]:
        low = mid + 1
    elif numbers[mid] < numbers[high]:
        high = mid
    else:
        high -= 1
    if low == high:
        return numbers[low]
    else:
        return minArray(numbers[low:high + 1])

a = minArray([1])
print(a)