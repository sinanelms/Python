
import re

pattern = re.compile("\W") #re is used to compile the expression more than once
#wordstring consisting of a million characters
wordstringgg = '''SCENE I. Yorkshire. Gaultree Forest.
Enter the ARCHBISHOP OF YORK, MOWBRAY, LORD HASTINGS, and others...
'''
with open("kararlar.txt", 'r',encoding="utf-8") as info:
    kararlar = info.read()
    wordlist = kararlar.split() #her kelimeyi bir boşlukla böler

for x, y in enumerate(wordlist):
    special_character = pattern.search(y[-1:]) #searches for a pattern in the string
    try:
        if special_character.group():  #returns all matching groups
            wordlist[x] = y[:-1]
    except:
        continue

wordfreq = [wordlist.count(w) for w in wordlist]  #counts frequency of a letter in the given list

print("String\n {} \n".format(wordstring))
print("List\n {} \n".format(str(wordlist)))
print("Frequencies\n {} \n".format(str(wordfreq)))
print("Pairs\n {}".format(str(dict(zip(wordlist, wordfreq)))))