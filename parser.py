import search
import nltk
x = True
newEssay = open("/website/assets/newEssay.txt","w+")
#x is whether or not we're making sure we use the right form of the word
with open("essay.txt",'r') as parseText:
	caps = "QWERTYUIOPASDFGHJUIKLZXCVBNM"
	parseText = list(parseText)
	for t in range(len(parseText)):
		toRead = parseText[t].split()
		for i in range(len(toRead)):
			toRead[i] = search.clean(toRead[i])
		parseText[t] = search.toString(toRead, ' ', True)
		if x:
			teff = nltk.pos_tag(nltk.tokenize.word_tokenize(parseText[t]))
		for i in range(len(toRead)):
			if not(toRead[i][0][0] in caps):
				if x:
					POS = ""
					if   'V' in teff[i][1]:
						POS = "(verb)"
					elif 'J' in teff[i][1]:
						POS = "(adj)"
					elif 'N' in teff[i][1]:
						POS = "(noun)"
					else:
						toRead[i] = toRead[i][0]+toRead[i][1]
					if POS !="":
						toRead[i] = search.replacePhraseForLength(toRead[i][0], POS)+toRead[i][1]
				else:
					toRead[i] = search.replacePhraseForLength(toRead[i][0], "")+toRead[i][1]
				if '\n' in toRead[i]:
					toRead[i] = toRead[i][:-1]
			else:
				toRead[i] = toRead[i][0]
		newEssay.write(search.toString(toRead, ' ',False)+'\n')
