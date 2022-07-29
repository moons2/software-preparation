'''
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.


Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
'''


from collections import Counter 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        .   listen to carefully
        I.  clarification questions
        II. speak your logic solution out load
        III. code
        IV. runtime analysis
        V. desk test
        '''
        
        if len(s) == 1:
            return 0
        
        charCounter = Counter(s)
        
        if not 1 in charCounter.values():
            return -1
        
        # mais uma vez um arr que poderia ser em uma linha
        for i, v in enumerate(s):
            if charCounter[v] == 1:
                return i