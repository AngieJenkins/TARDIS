# Метод train я разбила на две части: в первой данные из архива записываются в файл,
# во второй уже считываются из файла и добавляются в словарь. Сделано это с целью
# экономии времени - текстовый файл обрабатывается значительно быстрее архива.

#UnigramMorphAnalyzer[key] не работает, но я не знаю почему)

from corus import load_corpora
import tqdm
import pickle

class UnigramMorphAnalyzer:

    def __init__(self, endings_stat):
        self.endings_stat = endings_stat

    def train_1(self, path, name):
        records = load_corpora(path)
        with open(name + '.txt', 'w', encoding='utf8') as f:
            for rec in tqdm.tqdm(records):
                for par in rec.pars:
                    for sent in par.sents:
                        for token in sent.tokens:
                            f.write(f'{token.text} {token.forms[0].grams[0]}\n')

    def train_2(self, name):
        with open(name2, 'r', encoding='utf8') as f:
            for line in f:
                line = line.split()
                pos = line[1]
                if pos == 'PNCT' or pos == 'UNKN':
                    continue

                if len(line[0]) >= 4:
                    max_end = 5
                else:
                    max_end = len(line[0])
            
                for i in range(1, max_end):
                    end = line[0][-i:]
            
                    if end in endings_stat:
                        if pos in endings_stat[end]:
                            endings_stat[end][pos] += 1
                        else:
                            endings_stat[end][pos] = 1
                    else:
                        endings_stat[end] = {}
                        endings_stat[end][pos] = 1
        return endings_stat

    def save(self):
        with open('data.pickle', 'wb') as f:
            pickle.dump(endings_stat, f, protocol=None)
            
    def load(self):
        with open('data.pickle', 'rb') as f:
            model = pickle.load(f)
        return model

    def predict(self, token):
        numbers = [4, 3, 2, 1]
        if len(token) < 4:
            numbers = numbers[-(len(token)):]

        for i in numbers:
            end = token[-i:]
            dictio = self.load()
            if end in dictio:
                return dictio[end]
                print(end, dictio[end])
                break
            else:
                pass

    def __getitem__(self, key):
        return self.endings_stat[key]
    
    def eval(self):
        with open(name + '.txt', 'r', encoding='utf8') as f:
            with open(name + '_train.txt', 'w', encoding='utf8') as f_train:
                with open(name + '_test.txt', 'w', encoding='utf8') as f_test:

                    j = 0
                    data = []
                    for line in f:
                        data.append(line)
                        j += 1
                    number = j*0.8
                    
                    i = 0
                    for item in data:
                        if i < number:
                            f_train.write(item)
                            i += 1
                        else:
                            f_test.write(item)
                            i += 1

                    self.train_2(name + '_train.txt')
                    self.save()

                    with open(name + '_test.txt', 'r', encoding='utf8') as f_test:
                        for line in f_test:
                            line = line.split()
                            predict_result = self.predict(line[0])
                            try:
                                for key, value in predict_result.items():
                                    max_value = 0
                                    if value > max_value:
                                        max_value = value
                                        answer = key
                            except(AttributeError):
                                answer = 'UNKN'
                                

                            yes = 0
                            no = 0
                            if answer == line[1]:
                                yes += 1
                            else:
                                no += 1
        quality = (100 * yes)/(yes + no)
        return quality
                            
        
            
path = 'C:\\Users\\asus\\Desktop\\annot_opcorpora_xml_byfile.zip'
name = 'pos_data'
name2 = 'pos_data.txt'
token = 'мама'
endings_stat = {}
key = 'ник'

Unigram_Analyser = UnigramMorphAnalyzer(endings_stat)
#print(Unigram_Analyser.eval())
#Unigram_Analyser.train_2(name)
#Unigram_Analyser.save()
#Unigram_Analyser.load()
#print(Unigram_Analyser.predict(token))
#print(Unigram_Analyser.__getitem__(key))
#print(UnigramMorphAnalyzer[key])


