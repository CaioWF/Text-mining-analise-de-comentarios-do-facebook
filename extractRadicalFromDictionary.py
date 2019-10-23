import nltk
from nltk.stem import RSLPStemmer

#tokenize
#nltk.download('punkt')
def Tokenize(sentence):
    sentence = sentence.lower()
    sentence = nltk.word_tokenize(sentence)
    return sentence

#reduzir ao radical
#nltk.download('rslp')
def Stemming(sentence):
    stemmer = RSLPStemmer()
    return stemmer.stem(sentence.lower())
    

def main():
    doc = open('/home/caio/Documentos/Projeto Analise Comentarios Facebook/Novo_Dicionario.txt', encoding='utf-8-sig')
    text = doc.readlines()
    wordlist = []
    radicallist = dict()
    for line in text:
        line = Tokenize(line)
        line[0] = Stemming(line[0])
        line[1] = int(line[1])
        radicallist[line[0]] = line[1]
        wordlist.append(line)
    file = open("Dicionario_de_Radicais.txt", "w")
    for key in radicallist:
        sum = 0
        divider = 0
        for word in wordlist:
            if key == word:
                sum += radicallist[key]
                divider += 1
        if divider > 1:
            radicallist[key] = sum / divider
        file.write("{}\t{}\n".format(key, radicallist[key]))
    doc.close()
    file.close()
    print("finish!")

if __name__ == '__main__':
    main()