import requests
response = requests.get(url="https://api.kanye.rest/")
data = response.json()
quote = data["quote"]
print(quote)