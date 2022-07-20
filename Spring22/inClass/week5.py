[4, 5, 10, 3, 9]
[2, 5, 1, 3, 5, 8]

n = [0, 6, 3, 2, 3]
'''
    get two tallest walls, w1, w2
    sum up the difference between all walls and min(w1, w2)


    a2:
    find the index of the first element smaller than its preceding element
    get the index of the next element >= lwall or end of list
    loop while rwall < len(list)
        start lwall from the next element smaller than the preceding element

    add to sum once we have min(rwall, lwall)
'''

def rainwater(nums):
    lwall, rwall = 1
    sum = 0
    while rwall <= len(nums):
        while nums[lwall] < nums[lwall-1]:
            lwall += 1
        rwall = lwall + 1
        rtemp = lwall + 1
        while nums[lwall] < nums[rwall] and rwall <= len(nums):
            if nums[rwall-1] < nums[rwall]:
                rtemp = rwall
            rwall += 1
        if rwall > len(nums):
            rwall = rtemp
        lower = min(nums[rwall], nums[lwall])
        for i in range(lwall+1, rwall):
            sum += lower - nums[i]
        lwall = rwall
    return sum

print(rainwater(n))

