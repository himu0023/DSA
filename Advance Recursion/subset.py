def subset(nums):
    n = len(nums)
    total_subset = 1 << n  
    result = []
    
    for num in range(total_subset):  
        lst = []
        for i in range(n):
            if num & (1 << i) != 0:
                lst.append(nums[i])  
        result.append(lst)
    
    return result

nums = [1, 2, 3]
print("All subsets: ")
print(subset(nums))