import requests 
#http://
url = 'http://localhost:3333/'
response = requests.get(url)

# print(response)
# print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.text)
# print(response.json())
print(response.text)
