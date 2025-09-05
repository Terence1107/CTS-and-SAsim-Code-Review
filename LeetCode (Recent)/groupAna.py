def groupAnagrams(strs):
    '''
    Use a hashmap to keep track of which strings are anagrams to eachother
    Track the occurences of the character based off of their alphabet
    Have a constant array with the same number of elements as the number of alphabets
    Use a tuple to store the alphabet array since it is immutable
    '''
    grouped_anagrams = {}
    for string in strs:     
        alpha_count = [0] * 26
        for char in string:
            alpha_count[ord(char) - ord('a')] += 1

        key = tuple(alpha_count)

        if key not in grouped_anagrams:
            grouped_anagrams[key] = []
        
        grouped_anagrams[key].append(string)
        
    print(list(grouped_anagrams.values()))
    
        




strs = ["act","pots","tops","cat","stop","hat"]

groupAnagrams(strs)
