
import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'text':"I'm happy today"})

print(r.json())