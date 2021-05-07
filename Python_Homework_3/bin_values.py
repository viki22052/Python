
def bin_values(n):

    for num in range(n):
    
        yield bin(num)


if __name__ == '__main__':

    g = bin_values(3)

    print(next(g))
    print(next(g))
    print(next(g))
    