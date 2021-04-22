sum_el = 0

def suma(arr):
    global sum_el
    for i in range(len(arr)):

        if type(arr[i]) == list:
            suma(arr[i])
        else:
            sum_el += arr[i]

    return sum_el



if __name__ == '__main__':

    arr = [1,2,3,[5,6,[7]],4]
    
    print(f'Sum of arr elements is {suma(arr)}')