import search
def getPOS(sent, dex):
	ar = search.toArray(sent,' ')
	if 'ing' in ar[dex] or 'ed' in ar[dex]:
		return "verb"
	if dex < len(sent)-1 and 'ing' in ar[dex+1] or 'ed' in ar[dex+1]:
		return "noun"
	return "adj"
