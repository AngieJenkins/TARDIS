import sys
import requests
from bs4 import BeautifulSoup

githubers = ['torvalds', 'gvanrossum', 'poettering', 'dhh', 'moxie', 'fabpot', 'brendangregg', 'bcantrill', 'antirez']
site = 'https://api.github.com/users/'

class GitHubUser():
    
    def __init__(self):
        pass


    def name_desc(self):
        number_user = sys.argv[1]
        githuber = githubers[int(number_user)]
        
        r = requests.get(site + githuber + '/repos', verify = False)
        if r.status_code != 200:
            print(r.status_code)
            print ("Ахтунг!")
            
        repos = r.json()
        names = {}

        for rep in repos:
            names[(rep["name"])] = rep["description"]

        return names


    def languages(self):
        number_user = sys.argv[1]
        githuber = githubers[int(number_user)]
        
        r = requests.get(site + githuber + '/repos')
        if r.status_code != 200:
            print(r.status_code)
            print ("Ахтунг!")
            
        repos = r.json()
        langs = {}

        for rep in repos:
            if rep["language"] in langs:
                langs[rep["language"]] += 1
            else:
                langs[rep["language"]] = 1
        return langs


    def max_repos(self):
        max_num = 0
        arguments = sys.argv[1:]
        for one in arguments:
            person = githubers[int(one)]
            r = requests.get(site + person + '/repos')
            repos = r.json()
            if len(repos) > max_num:
                max_num = len(repos)
                max_rep = repos[0]["owner"]["login"]
        return max_rep


    def pop_lang(self):
        total_langs = {}
        arguments = sys.argv[1:]
        for one in arguments:
            person = githubers[int(one)]
            dict_lang = languages(person)
            for key, value in dict_lang.items():
                if key in total_langs:
                    total_langs[key] += dict_lang[key]
                else:
                    total_langs[key] = dict_lang[key]

        max_num = 0
        for key, value in total_langs.items():
            if value > max_num:
                max_num = value
                max_lang = key
            
        return max_lang


    def max_foll(self):
        max_folls = 0
        arguments = sys.argv[1:]
        for one in arguments:
            person = githubers[int(one)]
            r = requests.get(site + person + '/followers')
            folls = r.json()
            if max_folls < len(folls):
                max_folls = len(folls)
                most_popular_guy = person
        return most_popular_guy
        
#man = GitHubUser()
#print(pop_lang())


