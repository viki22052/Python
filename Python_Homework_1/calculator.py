if __name__ == "__main__":

   
    while True:

        op = input('Choose operation (+, -, /, //, *, q - quit): ')
        
        if op in 'q':
            break

        firstN = float(input("First Number: "))

        secondN = float(input("Second Number: "))
        
        if op in '+':
            print(f'Result: {firstN + secondN}')
        
        elif op in '-':
            print(f'Result: {firstN - secondN}')

        elif op in '/':
            print(f'Result: {firstN / secondN}')

        elif op in '//':
            print(f'Result: {firstN // secondN}')
        
        elif op in '*':
            print(f'Result: {firstN * secondN}')
        
        else:
            print('Invalid or Unsupported operation!!!')

    print('Turning off')
