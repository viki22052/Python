
suma = lambda a, b: print(a+b)
substr = lambda a, b: print(a-b)
mult = lambda a, b: print(a*b)
div = lambda a, b: print(a/b)
alt_div = lambda a, b: print(a//b)



if __name__ == '__main__':

    while True:
        try:
            op = input('Enter operation (+, -, *, /, //): ')
            if op in ('+', '-', '*', '/', '//'):
                a = float(input('First Number: '))
                b = float(input('Second Number: '))

                if op in '+':
                    suma(a, b)
                elif op in '-':
                    substr(a, b)
                elif op in '*':
                    mult(a, b)
                elif op in '/':
                    div(a, b)
                else:
                    alt_div(a, b)
            else:
                print('Invalid Choice')
                continue
        except ValueError:
            print('Numbers Only')
            continue
        else:
            break