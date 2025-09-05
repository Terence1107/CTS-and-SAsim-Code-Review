def isPalindrome(string):
    l, r = 0, len(string)-1

    while l < r:
        while l<r and not string[l].isalnum():
            l +=1

        while r>l and not string[r].isalnum():
            r -=1

        if string[l].lower() != string[r].lower():
            return False
        
        l, r = l + 1, r - 1
    return True





def isPalindrome2(string):
    new = ''
    for c in string:
        if c.isalnum():
            new += c.lower()
    return new == new[::-1]




s = "!Was it a car or a cat I saw?"
print(isPalindrome2(s))