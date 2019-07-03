import requests
# response = requests.get("https://www.baidu.com/")
# print(type(response))
# print(response.status_code)
# print(type(response.text))
# print(response.text)
# print(response.cookies)
#response = requests.get("http://httpbin.org/get?name=will&age=22")
data={
    "name":"will",
    "age":11
}
response = requests.get("http://httpbin.org/get",params=data)
print(response.text)
print(response.json())