#import pandas as pd
import re
import requests
import json
from bs4 import BeautifulSoup as bs

def collect_links():
    with open('links_from_MF.txt', 'w', encoding = 'utf-8') as f:
        
        # С первой страницы
        site1 = requests.get("https://www.mirf.ru/category/news/")
        soup = bs(site1.content, features = "html.parser")
        titles = soup.find_all('div', attrs = {'class' : "home_article_item_desc_text"})

        for item in titles:
            link = re.findall(r'"https.+?"', str(item))
            f.write(link[0] + '\n')

        # С последующих страниц
        for j in range(2, 311):
            site = requests.get('https://www.mirf.ru/category/news/page/' + str(j) + '/')
            soup = bs(site.content, features = "html.parser")
            titles = soup.find_all('div', attrs = {'class' : "home_article_item_desc_text"})

            for item in titles:
                link = re.findall(r'"https.+?"', str(item))
                f.write(link[0] + '\n')

def parametrs(soup, i):

    try:
        title = soup.find('h1')
        a = title.text
        words = a.split()
        for item in words:
            item = item.strip()
        title = " ".join(words)
    except AttributeError:
        title = 'no title'
    
    try:
        author = soup.find('a', attrs = {'rel' : "author"})
        b = author.text
        words = b.split()
        for item in words:
            item = item.strip()
        author = " ".join(words)
    except AttributeError:
        author = 'no author'

    try:
        data = re.search('(?<=> )\d.+?(?=<)', str(soup))
        data = data.group(0)
    except AttributeError:
        data = 'no data'

    try:
        time = re.search('(?<=>)\d .+', str(soup))
        time = time.group(0)
        words = time.split()
        for item in words:
            item = item.strip()
        time = " ".join(words)
    except AttributeError:
        time = 'no time for reading'

    articles[str(i)] = {}
    articles[str(i)]['title'] = title
    articles[str(i)]['author'] = author
    articles[str(i)]['data'] = data
    articles[str(i)]['time for reading'] = time
     
def art_text(soup, i):

    try:
        content = ''
        content1 = soup.find('div', attrs = {'class': "entry-content container"})
        content2 = content1.find_all('p')
        len_cont = len(content2)
        j = 0
        for item in content2:
            if j < (len_cont - 2):
                j += 1
                a = item.text
                words = a.split()
                for item in words:
                    item = item.strip()
                text = " ".join(words)
                content = content + ' ' + text
            
    except AttributeError:
        content = 'no content'
        
    articles[str(i)]['text'] = content

articles = {}
#link = 'https://www.mirf.ru/news/dzhonni-depp-poluchit-vosmiznachnyj-gonorar-za-fantasticheskih-tvarej-3-iz-za-osobennostej-kontrakta/'
#site = requests.get(link)
#soup = bs(site.content, features = "html.parser")
#i = 1
#parametrs(soup, i)
#art_text(soup, i)

#print(articles)

i = 0
with open('links_from_MF.txt', 'r', encoding = 'utf-8') as f:
    for link in f:
        link = link.strip('\n"')
        site = requests.get(link)
        soup = bs(site.content, features = "html.parser")
        i += 1
        parametrs(soup, i)
        art_text(soup, i)

with open('articles_MF.json', 'w') as file:
    json.dump(articles, file)



