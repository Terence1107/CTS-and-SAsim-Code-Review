import heapq 

def topK(nums, k):
    '''
    Use a hashmap to store the elements of the array with their number of occurences
    Return the k value(s) with the most occurences
    Sort them by the most occurences 
    '''

    occurences = {}

    for num in nums:
        occurences[num] = occurences.get(num, 0) + 1

    arr = []
    for num, count in occurences.items():
        arr.append([count,num])

    arr.sort()
    res = []
    for i in range(k):
        res.append(arr.pop()[1])


    return res

def heapK(nums, k):
    '''
    Use a hashmap to get the occurences of each integer
    use a max-heap to store and keep track of the highest occuring integers
    '''

    occurences = {}
    for number in nums: 
        occurences[number] = occurences.get(number, 0) + 1

    heap = []

    for number, count in occurences.items():
        heapq.heappush(heap, (count, number))
        if len(heap) > k:
            heapq.heappop(heap)

    result = []
    for i in range(k):
        result.append(heap[i][1])
    
    return result



nums = [1,2,2,3,3,3]
k = 2

print(heapK(nums, k))