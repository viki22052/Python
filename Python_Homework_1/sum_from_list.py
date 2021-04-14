if __name__ == "__main__":

    z = 15
    m = [5, 11, 10, 2, 9, 4, 10]
    i = 0
    j = len(m) - 1

    while i != len(m) - 1:


        if j == i:
            i += 1
            j = len(m) - 1

        if z == m[i] + m[j]:
            print(f'Result: {m[i]}[{i}] + {m[j]}[{j}]')
            flag = 1

        j -= 1
        

    if flag != 1:
        print('No pairs') 

