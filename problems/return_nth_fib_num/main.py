'''
Given an integer
write an algorithm to return the n-th element
of the fibonacci sequencia

SOLUTION

starting from the position 0
fibbonacci sequencie looks like

0, 1, 1, 2, 3, 5, 8, 13
what is exatly 
n = n-1 + n-2

this way given the first two elements
its possible to find the n-th element of the sequency


'''


def fib(pos):
    arr = [0, 1]

    if pos < 2:
        return arr[pos]

    for i in range(2, pos + 1):
        print(f'{i} : {arr}')
        arr[i % 2] += arr[(i+1) % 2]

    return arr[pos % 2]


if __name__ == "__main__":
    pos = int(input())
    print(fib(pos))
