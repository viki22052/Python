
if __name__ == '__main__':

    str = input("Enter brackets sequence: ")
    j = 0
    k = 0

    for i in range(len(str)):

        if str[0] == ')':
            k = 1
            print('Incorrect!')
            break
        elif str[len(str)-1] == '(':
            k = 1
            print('Incorrect!')
            break
        elif str[i] == '(':
            k+=1
        else:
            j+=1
            
    if j == k:
        print('Correct')
    else:
        print('Incorrect')



