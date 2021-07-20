"""
Given two string, write a method to decide if one is a permutation
of the other
"""

# essa abordagem verifica se as strings são iguais e o numero de
# ocorrencias de cada caractere
# tempo de execucao O(n)
#


def isPermutation(str1, str2):
    # n = len(str1)
    # m = len(str2)
    # O(n + m)
    if(len(str1) != len(str2)):
        return False

    # certo que n == m

    cH = {}

    # O(n)
    for char in str1:
        if(cH.get(char)):
            cH[char] += 1
        else:
            cH[char] = 1

    # O(n)
    for char in str2:
        if(cH.__contains__(char) and cH.get(char) >= 0):
            cH[char] -= 1
        else:
            return False

    return True


if __name__ == '__main__':
    str1 = str(input())
    str2 = str(input())

    print(isPermutation(str1, str2))
