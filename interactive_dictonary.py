import json # library to interact with .jason type files
import difflib  # library used for comparision
from difflib import get_close_matches #to get a list of words that closely match to a given word
data = json.load(open("data.json"))#dictionary file containing meanings of words
word=input('Enter a word:')

#function to get the meaning from dictionary

def translate(w):
	#it will return a word in the form of list which closesly matches with the input
	w= w.lower()
	suggestion = get_close_matches(w,data.keys(),n=1,cutoff=0.8)
	if w in data:
		return data[w]
	elif w.title() in data:
		return data[w.title()]
	elif w.upper() in data:
		return data[w.upper()]
	elif len(suggestion)>0:
		accuracy_of_suggestion = input("Did you mean " +suggestion[0]+ " instead? If yes enter Y else N for no :")
		if accuracy_of_suggestion.upper()=='Y':
			return translate(suggestion[0])
		elif accuracy_of_suggestion.upper()=='N':
			return "The word dosen't exist.Please check again."
		else:
			return "Sorry we didn't understand your entry."
	else:
     		return "The word dosen't exist.Please check again."

output = translate(word)
if type(output) == list:
	for i in output:
		print(i)
else:
	print(output)