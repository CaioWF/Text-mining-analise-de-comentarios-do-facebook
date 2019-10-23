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
    with open('./OPOVOOnline sobre escolha do novo reitor UFC.csv') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file)
        senti = PySentiStr()
        senti.setSentiStrengthPath("/home/caio/Documentos/Projeto Analise Comentarios Facebook/SentiStrength.jar")
        senti.setSentiStrengthLanguageFolderPath("/home/caio/Documentos/Projeto Analise Comentarios Facebook/SentStrength_Data/portuguese/")
        prev_message = ""
        
        with open('/home/caio/Documentos/Projeto Analise Comentarios Facebook/Frases_Neutras.csv', 'w') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow(["Frase", "notaPositiva", "notaNegativa"])
            #sentistrength
            for row in csv_dict_reader:
                if prev_message != row["message"] and row["message"]:
                    sentence = row["message"]
                    #sentence = RemoveAccent(sentence)
                    sentence = Tokenize(sentence)
                    if sentence:
                        sentence = RemoveStopWords(sentence)
                        if sentence:
                            sentence = Stemming(sentence)
                            sentence = " ".join(sentence)
                            result = senti.getSentiment(sentence, score='binary')
                            if result[0][0] + result[0][1] == 0:
                                #salvar frase tokenizada
                                #spamwriter.writerow([sentence, result[0][0], result[0][1]])
                                #salvar frase inteira
                                spamwriter.writerow([row["message"], result[0][0], result[0][1]])
                #publicacao com resposta de comentários
                if row["object_link.connections.comments.message"] != 'null' and row["object_link.connections.comments.message"]:
                    sentence = row["object_link.connections.comments.message"]
                    #sentence = RemoveAccent(sentence)
                    sentence = Tokenize(sentence)
                    if sentence:
                        sentence = RemoveStopWords(sentence)
                        if sentence:
                            sentence = Stemming(sentence)
                            sentence = " ".join(sentence)
                            result = senti.getSentiment(sentence, score='binary')
                            if result[0][0] + result[0][1] == 0:
                                #mostrar tokenizada
                                #spamwriter.writerow([sentence, result[0][0], result[0][1]])
                                #mostrar frase inteira
                                spamwriter.writerow([row["object_link.connections.comments.message"], result[0][0], result[0][1]])
                prev_message = row["message"]
            print("finish!")
    

if __name__ == '__main__':
    main()