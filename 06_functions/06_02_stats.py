'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

my_list = [1, 2, 3, 4, 5, 6, 7]

def stats(num_list):
  max_num = max(num_list)
  min_num = min(num_list)
  sum_num = sum(num_list)
  average_num = sum_num / len(num_list)
  result_dict = {}
  result_dict['max'] = max_num
  result_dict['min'] = min_num
  result_dict['sum'] = sum_num
  result_dict['average'] = average_num
  return result_dict

results = stats(my_list)
print(f'The max value is: {results["max"]}')
print(f'The min value is: {results["min"]}')
print(f'The sum is: {results["sum"]}')
print(f'The average is: {int(results["average"])}')


