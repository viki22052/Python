
def remove_duplicates(func):
    def wrapper(arr):
        res = []
        for i in arr:
            if i not in res:
                res.append(i)
        g = func(res)
        return g
    return wrapper


if __name__ == '__main__':

    arr = [1,2,3,4,5,2,3,4]
    
    dec_sum = remove_duplicates(sum)
    print(f'Sum without duplicates {dec_sum(arr)}')
    print(f'Original sum {sum(arr)}')

