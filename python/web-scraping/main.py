import requests
import bs4


file_path = "./index.html"

with open(file_path) as file:
    file_response = file.read()


response = bs4.BeautifulSoup(file_response, 'html.parser')
print(response.body.text)


"""
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()

header = {'user-agent': ua.random}
response = requests.get("https://www.lipsum.com/", header)
bs = BeautifulSoup(response.text, "html.parser")

# # response.headers['Content-Type'] = 'text/html'
print(bs.html())
# print(response.headers)
# print(response.elapsed)
# print(response.connection)
# print(response.cookies)
# print(response.history)
"""
