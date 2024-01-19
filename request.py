import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'P/E':0, 'EPS':0, 'P/B':0, 'D/E': 0})

print(r.json())