def quick_sort(alist,first,last):


    low = first
    high = last
    if first == last:
         return
    if first> last:
        return
    mid_value = alist[first]
    while low<high:


        while low<high and alist[high]>mid_value:
            high-=1

        while low<high and alist[low]<=mid_value:
            low+=1
        alist[low],alist[high] = alist[high],alist[low]
    alist[first],alist[low] = alist[low],alist[first]

    quick_sort(alist,first,low-1)
    quick_sort(alist,low+1,last)

if __name__ == '__main__':
    list1 = [32,2,9,6,17,44,56,39,58,22]
    quick_sort(list1,0,len(list1)-1)
    print(list1)

a = [1,2,3]
b = [2,1,3]
print(a==b)
print(set(b))
print(list(set(b)))