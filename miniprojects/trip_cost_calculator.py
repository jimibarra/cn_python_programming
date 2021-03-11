print("This script will calculate the cost of a trip")
distance = int(input("Please type the distance to drive in kilometers: "))
usage = float(input("Please type the fuel usage of your car in liters/kilometer: "))
cost_per_liter = float(input("Please type the cost of a liter of fuel: "))

total_cost = cost_per_liter * usage * distance

print(f'The total cost of your trip is {total_cost}.')


