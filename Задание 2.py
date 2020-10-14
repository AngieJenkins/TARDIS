import os
import nltk
from nltk.tokenize import word_tokenize

class FileReader:
    
    def __init__(self, path):
        self.path = path
        
    def read(self):
        try:
            with open (self.path, 'r', encoding = 'utf-8') as f:
                return f.read()
        
        except (FileNotFoundError):
            return ' '

    def write(self, data):
        with open(self.path, 'a', encoding = 'utf-8') as f:
            f.write(data)
            
    def count(self):
        line_count = 0
        word_count = 0
        
        try:
            with open(self.path, 'r', encoding = 'utf-8') as f:
                for line in f:
                    line_count += 1
                words = word_tokenize(f)
                for word in words:
                    word_count += 1
            return line_count, word_count
        
        except (FileNotFoundError):
            return line_count, word_count
            
    def __add__(self, file):
        data = ''
        files = []
        try:
            files.append(self.path)
            files.append(file)
            for item in files:
                with open(item, 'r', encoding = 'utf-8') as f:
                    data = data + f.read()
        
        except (FileNotFoundError):
            print('Файл не найден')

        new = input('Введите название нового файла ')
        path = os.getcwd() + new
        new_file = FileReader(path)
        new_file.write(data)
        return new_file

    def __str__(self):
        return self.path
        
#data = input('Что записать в файл? ')       
#name = 'new_file.txt'
#path = os.path.abspath(name)
#print(path)
#book = FileReader(path)
