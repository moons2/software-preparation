
# Desenhe um algoritmo que imprima todas
# as permutações de uma string. Assuma que cada
# caractere eh unico

def strInsertAt(index, char, chain):
    if index > len(chain):
        return None
    return chain[:index] + char + chain[index:]


def main(string):
    strLen = len(string)

    if(strLen <= 1):
        print(string)
        return

    hashT = {string[0]}

    for i in range(1, strLen):
        auxHash = set()
        for subStr in hashT:
            for j in range(i, -1, -1):
                auxHash.add(strInsertAt(j, string[i], subStr))
        hashT = auxHash

    # agora imprimimos todas as variacoes
    for permutacao in hashT:
        print(permutacao)

    print(len(hashT))


if __name__ == '__main__':
    main(str(input()))
