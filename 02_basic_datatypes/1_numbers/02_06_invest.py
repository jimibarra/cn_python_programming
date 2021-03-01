'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

present_value = int(input('Please enter the investment amount: '))
annual_interest_rate = float(input('Please enter the annual interest rate percentage: '))
years = int(input('Please enter the number of years to invest: '))
future_value = present_value * ((1 + annual_interest_rate/100)**years)
print(f'The future value is {future_value}.')
