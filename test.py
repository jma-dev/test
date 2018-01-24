import pandas as pd
import requests

url = 'www.google.com'
r = requests.get(url)
print(r.text)
