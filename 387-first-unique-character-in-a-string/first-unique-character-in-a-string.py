class Solution(object):
    def firstUniqChar(self, s):
      
        char_freq = {}

        
        for char in s:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

        for i in range(len(s)):
            if char_freq[s[i]] == 1:
                return i

        return -1