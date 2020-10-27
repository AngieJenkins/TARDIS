import pymorphy2
from itertools import product
import random

morph = pymorphy2.MorphAnalyzer()
#krasivy = morph.parse('Красивый')[0]
#print(krasivy)
#print (krasivy.tag.POS)

i = 0
with open('nouns.txt', 'w', encoding = 'utf-8') as f_n:
    with open('adjective.txt', 'w', encoding = 'utf-8') as f_a:
        with open('rus_shuffled.txt', 'r', encoding = 'utf-8') as f:
            for line in f:
                line = line.strip()
                if i <= 30000:
                    word = morph.parse(line)[0]
                    PoS = word.tag.POS
                    
                    if PoS == 'NOUN':
                        if ('masc' in word.tag) or ('femn' in word.tag) or ('neut' in word.tag):
                            f_n.write(word.normalized.word + '\n')
                        else:
                            print(line)
                    elif PoS == 'ADJF':
                        f_a.write(word.normalized.word + '\n')
                  
                    else:
                        pass
                    i += 1
                else:
                    break

print('part two')

nouns = []
adjectives = []
with open('nouns.txt', 'r', encoding = 'utf-8') as f_n:
    with open('adjective.txt', 'r', encoding = 'utf-8') as f_a:
        for line in f_n:
            line = line.strip()
            morph_line = morph.parse(line)[0]
            if (morph_line.tag.POS == 'NOUN') and (('masc' in morph_line.tag) or ('femn' in morph_line.tag) or ('neut' in morph_line.tag)):
                nouns.append(line)
            else:
                print(line)
                
        for line in f_a:
            line = line.strip()
            adjectives.append(line)

        
data = list(product(adjectives, nouns))
data = [list(ele) for ele in data]

for pair in data:
    adj = morph.parse(pair[0])[0]
    nn = morph.parse(pair[1])[0]
    try: 
        if nn.tag.gender == 'femn':
            pair[0] = adj.inflect({'femn'}).word
        elif nn.tag.gender == 'neut':
            pair[0] = adj.inflect({'neut'}).word
        elif nn.tag.gender == 'masc':
            pass
        else:
            print(pair)
            print(nn.tag.POS)
            print(nn.tag.gender)
            data.remove(pair)
    except(AttributeError):
        data.remove(pair)
        
print(random.sample(data, 100))    





        
        
    
