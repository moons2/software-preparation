'''
Given two integers N, K. Write an algorithm
that return and palindrome of length N with
K distinct letters between a~z in lower case
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

    print(word)


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    palindrome(n, k)
