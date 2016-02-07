with open("th_en_US_new.dat","r") as fil:
	fil = list(fil)
def clean(word):
	letters = "qwertyuiopasdfghjklzxcvbnm"
	if len(word) == 1:
		return [word, ""]
	toRet = word
	f = list(word)
	end = len(word)-1
	for i in range(1,len(f)+1):
		if f[len(f)-i] in letters:
			end = len(f)-i+1
			break
	return [word[:end], word[end:]]
	
	return toRet
def replacePhraseForLength(word, pos):#pos = part of speech
	if len(word) <= 3:
		return word
	if pos != "" and not(list(pos)[0]=='(' and list(pos)[len(pos)-1]==')'):
		pos = '('+pos+')'#make sure pos is surrounded by parenthesis
	line = ""
	for i in range(len(fil)):
		if word in fil[i] and pos in fil[i]:
			line = fil[i].split('|')[2:]
			if word in line:
				break
	if line == "":
		return word
	toRet = ""
	for i in line:
		if len(i)>len(toRet):
			toRet = i
	return toRet
def toString(array, sep, isArr):#sep = separator
	toRet = ""
	for i in array:
		if i != "":
			if isArr:
				toRet += i[0]+sep
			else:
				toRet += i+sep
	return toRet
