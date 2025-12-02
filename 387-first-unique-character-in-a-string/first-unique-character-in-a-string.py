class Solution(object):
    def firstUniqChar(self, s):
        # Create a dictionary to store the frequency of each character
        char_freq = {}

        # Iterate through the string to count character frequencies
        for char in s:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

        # Iterate through the string again to find the first non-repeating character
        for i in range(len(s)):
            if char_freq[s[i]] == 1:
                return i

        # If no non-repeating character is found, return -1
        return -1