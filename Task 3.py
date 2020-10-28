from collections import defaultdict, Counter

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

string = 'Toss a coin to your whitcher'
string = string.lower()
string = Counter(string)

new_string = ''
for letter in alphabet:
    if letter in string:
        new_string = new_string + letter * string[letter]

string = new_string
print(string)
        
    
