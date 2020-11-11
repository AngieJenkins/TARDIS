import re
import requests
from bs4 import BeautifulSoup as bs

headers = []
link = 'https://www.kommersant.ru/archive/rubric/4/month/2020-10-01'
site = requests.get(link)
soup = bs(site.content, features = "html.parser")
header_tag = soup.find_all('h3', attrs = {'class' : "article_name"})
for item in header_tag:
    header = item.text
    headers.append(header)


for item in headers:
    korona = re.search(' корона', item)
    kovid = re.search(' COVID', item)
    if (korona != None) or (kovid != None):
        print(item)
        
