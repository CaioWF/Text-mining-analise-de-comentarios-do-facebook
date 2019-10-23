import csv
import nltk
from sentistrength import PySentiStr
from nltk.stem import RSLPStemmer
import pandas as pd
import glob
#from unicodedata import normalize

"""remover acentuação
def RemoveAccent(sentence):
    return normalize('NFKD', sentence).encode('ASCII', 'ignore').decode('ASCII')
"""

#tokenize
#nltk.download('punkt')
def Tokenize(sentence):
    sentence = sentence.lower()
    sentence = nltk.word_tokenize(sentence)
    sentence = [word for word in sentence if word.isalpha()]
    return sentence

#reduzir ao radical
#nltk.download('rslp')
def Stemming(sentence):
    stemmer = RSLPStemmer()
    phrase = []
    for word in sentence:
        phrase.append(stemmer.stem(word.lower()))
    return phrase

#retirar stopwords em português
#nltk.download('stopwords')
def RemoveStopWords(sentence):
    stopwords = nltk.corpus.stopwords.words('portuguese')
    phrase = []
    for word in sentence:
        if word not in stopwords:
            phrase.append(word)
    return phrase

def main():
    #mudar entrada
    with open('./Comentarios_csv/Test/OPOVOOnline sobre escolha do novo reitor UFC.csv') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file)
        senti = PySentiStr()
        senti.setSentiStrengthPath("/home/caio/Documentos/Projeto Analise Comentarios Facebook/SentiStrength.jar")
        senti.setSentiStrengthLanguageFolderPath("/home/caio/Documentos/Projeto Analise Comentarios Facebook/SentStrength_Data/portuguese/")
        
        #mudar saída
        with open('./Comentarios_csv/Test/teste.csv', 'w') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow(["Comentário", "notaPositiva", "notaNegativa", "Sentimento"])
            for row in csv_dict_reader:
                #colocar nome da coluna que tem o comentario
                if row["message"]:
                    sentence = row["message"]
                    #sentence = RemoveAccent(sentence)
                    sentence = Tokenize(sentence)
                    if sentence:
                        sentence = RemoveStopWords(sentence)
                        if sentence:
                            sentence = Stemming(sentence)
                            sentence = " ".join(sentence)
                            #sentistrength                            
                            result = senti.getSentiment(sentence, score='binary')
                            if result[0][0] + result[0][1] <= -1:
                                sentiment = 'negativo'
                            elif result[0][0] + result[0][1] >= 1:
                                sentiment = 'positivo'
                            else:
                                sentiment = 'neutro'
                            spamwriter.writerow([row["message"], result[0][0], result[0][1], sentiment])
            print("finish!")

if __name__ == '__main__':
    main()