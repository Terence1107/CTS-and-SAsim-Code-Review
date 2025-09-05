def length(s):
    '''
    approach with 2 pointers probably
    hashmap to keep track of the index of the last character in the substring
    '''

    newString = ''
    max_length = 0

    for c in range(len(s)):
        if s[c] not in newString:
            print("add", s[c])
            newString += s[c]
        else:
            print("remove", s[c])
            dup_index = newString.index(s[c])
            newString = newString[dup_index + 1:]
            newString += s[c]

        max_length = max(max_length, len(newString))
        print("length", max_length, newString)
    return max_length
    


def optimal(s):
    h = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in h and h[s[right]] >= left:
            left = h[s[right]] + 1

        #new+=s[right]
        h[s[right]] = right
        
        #print(new)
        if right - left + 1 > max_length:
            max_length = right - left + 1
    return max_length

s="dvdf"
print(optimal(s))