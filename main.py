#from search import replace

def inputparagraph():
    st = input("Paragraph: ")
    words = st.split()
    clasues = st.split(",.")
    phrases = []
    for i in words.length-2:
        phrases.append([words[i],words[i+1],words[i+2]])
    return words, clauses, phrases

def printpara(endpara):
    print ' '.join(endpara)


def main():
   words, clauses, phrases = inputparagraph()
   printpara(words)

main()
