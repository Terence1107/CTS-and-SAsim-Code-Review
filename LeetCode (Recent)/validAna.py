def isAnagram(s,t):
    
    hashS = {}
    hashT = {}

    if len(s) != len(t):
        return False
    
    else:
        for i in range(len(s)):
            hashS[s[i]] = hashS.get(s[i], 0) + 1
            hashT[t[i]] = hashT.get(t[i], 0) + 1
    print(hashS, hashT)
    
    return hashS == hashT



s="bbcc"
t="ccbc"
print(isAnagram(s,t))