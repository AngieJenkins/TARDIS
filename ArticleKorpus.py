import re
import requests
import json
from collections import Counter
from bs4 import BeautifulSoup as bs
from natasha import NewsEmbedding, NewsNERTagger, Doc, Segmenter, MorphVocab

# Собираем ссылки на новости

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


# Извлекаем информацию о названии, авторе, дате публикации
# и приблизительном времени на чтение статьи

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


# Извлекаем текст статьи

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


# Собираем корпус статей

def collect_corpus():
    articles = {}

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


# Извлекаем из статей именованные сущности, записываем в словарь json

def make_names_dict():
    emb = NewsEmbedding()
    ner_tagger = NewsNERTagger(emb)
    segmenter = Segmenter()
    morph_vocab = MorphVocab()

    with open ('articles_MF.json', 'r') as read_file:
        data = json.load(read_file)

    names_dict = {}

    for i in range(1, (len(data)+1)):
        art = data[str(i)]['text']
        doc_art = Doc(art)
        doc_art.segment(segmenter)
        doc_art.tag_ner(ner_tagger)
        doc_art.ner
        
        names = []

        for span in doc_art.spans:
            span.normalize(morph_vocab)

        {span.text: names.append(span.normal) for span in doc_art.spans} 
        
        names_dict[str(i)] = Counter(names)

    with open('names_MF.json', 'w') as write_names:
        json.dump(names_dict, write_names)






