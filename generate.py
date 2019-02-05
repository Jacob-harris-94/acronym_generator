import random
import sys
from math import floor
from progress.bar import Bar
from read_english_dictionary import *

english_words = load_words()

print('fate' in english_words)

words_of_interest = set()
with open('words_of_interest.txt') as word_file:
	 words_of_interest = set(word_file.read().split())

#letters_of_interest = {word[0].lower(): [word.lower()] for word in words_of_interest}
# build a map of   letter : list of words starting with that letter
letters_of_interest = {}
for word in words_of_interest:
	if word[0].lower() in letters_of_interest:
		letters_of_interest[word[0].lower()].append(word)
	else:
		letters_of_interest[word[0].lower()] = [word]

#print(letters_of_interest)

acronyms = []
#for word in Bar('processing').iter(english_words):
bar = Bar('Processing', max=100, suffix='%(percent)d%%')
for (count, word) in enumerate(english_words):	
	if (floor(count/len(english_words)*100) > floor((count-1)/len(english_words)*100)):
		bar.next() 
	acronym=[]
	for letter in word:
		if letter in letters_of_interest:
			acronym.append(random.choice(letters_of_interest[letter]))
		else:
			acronym=[]
			break
	if(len(acronym) > 0):
		acronyms.append([word, acronym])
bar.finish()

acronyms.sort()
		
#for a in acronyms:		
#	print(a[0] + " : " + ' '.join(a[1]))
print(str(len(acronyms)) + ' acronyms generated.')	
	
with open('great_acronyms.txt', 'w') as out_file:
	out_file.writelines(a[0] + " : " + ' '.join(a[1]) + '\n' for a in acronyms)