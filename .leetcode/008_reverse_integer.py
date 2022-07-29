'''
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit 
integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 
64-bit integers (signed or unsigned).


Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
'''

class Solution:
    def reverse(self, x: int) -> int:
        '''
        . listen to carefully
        I. clarification questions
        II. speak your solution logic out load
        III. code
        IV. runtime analysis
        V. desk test
        '''
        
        n = len(str(x))
        negative = 1
        
        if n == 1:
            return x
            
        if x < 0:
            negative = -1
            n -= 1
            
        x_reversed = ''
        for i in range(n):
            x_reversed += str(negative * x % 10**(i+1) // 10**i)
        
        if not abs(negative * int(x_reversed)) < 2**31 and negative * int(x_reversed) != 2**31 - 1:
            return 0
        
        return negative * int(x_reversed)