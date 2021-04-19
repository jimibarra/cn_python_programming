'''
Do some research on other popular python packages and what the are used for. Feel free to import them
and play around a little.

Note - Moved this script to within the testenv virtual environment.
'''

import requests

url = 'https://pypi.org'
response = requests.get(url)
print(response.status_code)




