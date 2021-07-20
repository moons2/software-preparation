'''
usually uses three approaches

stores intermediate results to became the computarion faster

> 1. Recursion
> 2. Store (mozaic)
> 3. Bottom-Up

> 1. Recursion
def fib(n):
    if n <= 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result
'''


def fib(n):
    # exponential fib
    return n if n <= 1 else fib(n-1) + fib(n-2)


# no stack overflows! just pretty!
def dynamic_bottom_up_fib(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i-1] + f[i-2])
    return f[n]


if __name__ == '__main__':
    print(
        dynamic_bottom_up_fib(int(input()))
    )
