# o(n) solution for LeetCode 
nums = [1,2,1,1,3,3]

n = len(nums)
d = dict() 

# // o(n)
for i in nums:
    # print(i)
    if i not in d:
        d[i] = 1 
    else:
        d[i] = d[i] +  1 



print(d)
m = len(d)
count = 0 
for i in d:

    value = d[i]
    # print(value)
    # print( (value*(value-1)) // 2)
    if value == 1:
        continue 
    else:
        count   += (value*(value-1)) // 2

print(count)
    