
def factor(n):

    if n == 0:
        return 1
    elif n > 0:
        return n * factor(n-1)
    
    return 0


if __name__ == '__main__':

    n = int(input('Enter n: '))

    print(f'Factorial of {n} is {factor(n)}')

