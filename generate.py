import random
from read_english_dictionary import *


english_words = load_words()

print('fate' in english_words)

words_of_interest = set()
with open('words_of_interest.txt') as word_file:
	 words_of_interest = set(word_file.read().split())

#letters_of_interest = {word[0].lower(): [word.lower()] for word in words_of_interest}
letters_of_interest = {}
for word in words_of_interest:
	if word[0].lower() in letters_of_interest:
		letters_of_interest[word[0].lower()].append(word)
	else:
		letters_of_interest[word[0].lower()] = [word]

#print(letters_of_interest)

acronyms = []
for word in list(english_words)[0:]:	
	acronym=[]
	for letter in word:
		if letter in letters_of_interest:
			acronym.append(random.choice(letters_of_interest[letter]))
		else:
			acronym=[]
			break
	
	if(len(acronym) > 0):
		acronyms.append([word, acronym])

acronyms.sort()
		
for a in acronyms:		
	print(a[0] + " : " + ' '.join(a[1]))
print(str(len(acronyms)) + ' acronyms generated.')	
	
with open('great_acronyms.txt', 'w') as out_file:
	out_file.writelines(a[0] + " : " + ' '.join(a[1]) + '\n' for a in acronyms)