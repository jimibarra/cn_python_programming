def division_calc(dividend, divisor):
    return dividend / divisor

if __name__=='__main__':
    x = int(input('Please type dividend: '))
    y = int(input('Please type divisor: '))
    result = division_calc(x, y)
    print(f'The quotient is {result}.')
