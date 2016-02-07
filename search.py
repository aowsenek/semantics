with open("th_en_US_new.dat","r") as fil:
	fil = list(fil)
def replacePhraseForLength(word, pos):#pos = part of speech
	if pos != "" and not(list(pos)[0]=='(' and list(pos)[len(pos)-1]==')'):
		pos = '('+pos+')'
	line = ""
	for i in range(len(fil)):
		if word in fil[i] and pos in fil[i]:
			line = toArray(fil[i],'|')[2:]
			if word in line:
				break
	if line == "":
		return word
	toRet = ""
	for i in line:
		if len(i)>len(toRet):
			toRet = i
	return toRet
def toArray(word,sep):#sep = separator
	toRet = []
	toAdd = ""
	for i in word:
		if i == sep:
			toRet += [toAdd]
			toAdd = ""
		else:
			toAdd+=i
	return toRet+[toAdd]
