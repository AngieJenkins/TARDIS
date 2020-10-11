import os

class FileReader:
    
    def __init__(self):
        pass
        
    def read(self, way):
        content = ''
        try:
            with open(os.path.abspath(way), 'r', encoding = 'utf-8') as self.f:
                for line in self.f:
                    content = content + line + ' '
            self.f.close()
            return content
        
        except (FileNotFoundError):
            return content

    def write(self, way, data):
        with open(os.path.abspath(way), 'a', encoding = 'utf-8') as self.f:
            self.f.write(data)
            
    def count(self, way):
        line_count = 0
        word_count = 0
        
        try:
            with open(os.path.abspath(way), 'r', encoding = 'utf-8') as self.f:
                for line in self.f:
                    line_count += 1
                    for word in line:
                        word_count += 1
            self.f.close()
            return line_count, word_count
        
        except (FileNotFoundError):
            return line_count, word_count
            
    def __add__(self, way1, way2):
        data = ''
        files = []
        try:
            files.append(way1)
            files.append(way2)
            for file in files:
                with open(os.path.abspath(file), 'r', encoding = 'utf-8') as self.f:
                    for line in self.f:
                        data = data + line + ' '
                self.f.close()
        
        except (FileNotFoundError):
            print('Файл не найден')

        new = input('Введите название нового файла ')
        way = os.getcwd() + new
        new_file = FileReader()
        new_file.write(way, data)
        return new_file

    def __str__(self):
        return os.path.abspath(way)
        
#data = input('Что записать в файл? ')       
#way1 = input('Введите имя первого файла ')
#way2 = input('Введите имя второго файла ')
#way = input('Введите имя файла ')
#book = FileReader()


