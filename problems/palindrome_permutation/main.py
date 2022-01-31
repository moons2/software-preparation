'''
Given a string, write a func to check if it is a permutation of
a palindrome. A palindrome is a word of phrase that is the same
fowards and backwards. A permutation is a rearrangement of
letters. The palindrome does not need to be limited to just dictionary words.

IN: Tact Coa
OUT: True {'taco cat', 'atco cta'}
'''

import math


def palindrome(n, k):
    i = 0
    j = n-1

    word = list([0] * n)

    for l in range(math.ceil(n/2)):
        word[i] = chr(97 + (l % k))
        word[j] = chr(97 + (l % k))
        i += 1
        j -= 1

    print(''.join(word))
    return ''.join(word)


def IsPalindromePermutation(str):
    str = str.replace(' ', '')
    str = str.lower()

    if(len(str) < 2):
        return True

    lFH = {}

    for char in str:
        if(lFH.get(char)):
            lFH[char] += 1
        else:
            lFH[char] = 1

    oddAlreadyFound = False

    for value in lFH.values():
        if(value % 2 != 0):
            if(oddAlreadyFound):
                return False
            oddAlreadyFound = True
    return True


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    print(IsPalindromePermutation(palindrome(n, k)))
