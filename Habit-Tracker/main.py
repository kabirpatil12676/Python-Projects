import requests
from datetime import datetime
USERNAME = "kabir12676"
TOKEN = "kabir12676"

parameters = {
    "token" : USERNAME,
    "username" : TOKEN,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}
pixela_endpoint = " https://pixe.la/v1/users"
# response = requests.post(url=pixela_endpoint, json=parameters)
# data = response.json()
# print(data)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id" : "graph1",
#     "name" :"Coding Graph",
#     "unit" : "hour",
#     "type" : "float",
#     "color" : "ajisai",
# }
headers = {
    "X-USER-TOKEN" : TOKEN,
}
# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)


coding_endpoint = (f"{graph_endpoint}/graph1")
today = datetime.now()
coding_config ={
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many hours did Code today?: "),
}
response = requests.post(url=coding_endpoint,json=coding_config,headers=headers)
print(response.text)

update_config ={
    "quantity" : "200",
}
update_endpoint =(f"{graph_endpoint}/graph1/{ today.strftime('%Y%m%d')}")
# response = requests.put(url=update_endpoint,json=update_config,headers=headers)
# print(response.text)


# response = requests.delete(url=update_endpoint,headers=headers)
# print(response.text)