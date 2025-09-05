def twoSumII(list, target):
    '''
    use 2 pointers to traverse the list
    evaluate the numbers as we traverse
    decrement or increment the pointers based on the sum of the 2 numbers
    '''

    l, r = 0, len(list) - 1
    while list[l] < list[r]:
        if (list[l] + list[r]) == target:
            return [l+1, r+1] 
        
        elif (list[l] + list[r]) > target:
            r -= 1    

        else:
            l += 1

    return False  




numbers = [1,2,3,4]
target = 3

print(twoSumII(numbers, target))