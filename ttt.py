


def getLeastNumbers(arr,k):
    def quick_sort(arr, l, r):
        if l >= r: return  # 子数组长度为1时终止递归
        i, j = l, r
        while i < j:
            while arr[j] >= arr[l] and i < j: j -= 1       #快排从右边开始，且每次大循环执行后肯定要前进一步，9，10行至少执行一次
            while arr[i] <= arr[l] and i < j: i += 1
            arr[i], arr[j] = arr[j], arr[i]
        arr[l], arr[i] = arr[i], arr[l]
        quick_sort(arr, l, i - 1)
        quick_sort(arr, i+1, r)

    quick_sort(arr, 0, len(arr) - 1)
    return arr[:k]

getLeastNumbers([0,0,1,2,4,2,2,3,1,4],8)