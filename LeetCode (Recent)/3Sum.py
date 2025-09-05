def sum (nums):
    '''
    Notes and initial thoughts: 
    Use 2 pointers to traverse the list, both starting from the left side at 0,1
    evaluate the numbers as we traverse
    Use hashmap to keep track of indexes used for current triplets 
    reset the pointers whenever we find 
    '''
    result = []
    triplet = {}
    l=0
    r=len(nums) - 1

    nums.sort()
    
    for i, a in enumerate(nums):
        print(i, a, nums[i-1])
        if i>0 and a == nums[i-1]:
            continue

        head = nums[i]
        l = i+1
        
        while l<r:

            if (head + nums[l] + nums[r]) == 0:
                result.append([head, nums[l], nums[r]])
                
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l+=1
            elif (head + nums[l] + nums[r]) < 0:
                l += 1

            else:
                r -= 1  
            
    return result

nums = [-1,0,1,2,-1,-4]

print(sum(nums))