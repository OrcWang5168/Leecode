def exchange(nums):
    if not nums:
        return None
    start = 0
    end = len(nums) - 1
    total = end - start
    sigg = None
    dbll = None

    def change(total_temp, nums, sig, dbl):
        # print("执行一次")
        sig = sigg
        dbl = dbll
        j = total_temp
        i = end - total_temp
        # print(i)
        # print(j)
        while i <= j:
            if nums[i]%2 == 1:
                sig = nums[i]
                break
            else:
                i += 1
        if not sig:
            return
        else:
            temp = nums[end - total_temp]
            nums[end - total_temp] = sig
            nums[i] = temp

        while j > end - total_temp:
            if nums[j]%2 == 0:
                dbl = nums[j]
                break
            else:
                j -= 1
        if not dbl:
            return
        else:


            temp = nums[total_temp]
            nums[total_temp] = dbl
            nums[j] = temp
            change(total_temp - 1, nums, sigg, dbll)

    change(total, nums, sigg, dbll)
    return nums

c = exchange([1,3,7,4,5])
print(c)
