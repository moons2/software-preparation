'''
how to merge dicts and lists
'''

if __name__ == '__main__':
    dictA = {'a': 0, 'b': 1}
    dictB = {'c': 0, 3: 'A'}

    dictAB = {**dictA, **dictB}

    listA = [1, 2, 3]
    listB = [4, 5, 6]

    listAB = [*listA, *listB]
