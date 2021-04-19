'''
In 3 lines of code, fetch the HTML text from codingnomads' main page
and print it to your console.

TIP:
- if you wonder what to use, google something like
    "most popular python package"
- if you run into encoding/decoding errors, you're experiencing something
    very common. head over to SO and find a solution!
Note - Moved this script to within the testenv virtual environment.

'''
import requests
url = 'https://codingnomads.co'
response = requests.get(url)
print(response.text)



