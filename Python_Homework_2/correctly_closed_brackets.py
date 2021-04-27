
if __name__ == '__main__':

    str = input("Enter brackets sequence: ")
    #j = 0
    k = 0

    for i in range(len(str)):

        if k < 0:
            break
        elif str[0] == ')':
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
            k-=1
            
    if k == 0:
        print('Correct')
    else:
        print('Incorrect')



