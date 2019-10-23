from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
import pandas as pd

df = pd.read_csv(r"./Comentarios_csv/Reforma_Previdencia/acriticacom.csv", encoding ="utf-8")

comment_words = ' '
stopwords = set(nltk.corpus.stopwords.words('portuguese'))

#Mudar para a coluna desejada
for val in df.Comment:
    val = str(val)

    tokens = val.split()

    for i in range (len(tokens)):
        tokens[i] = tokens[i].lower()
    
    for words in tokens:
        comment_words = comment_words + words + ' '

wordcloud = WordCloud(width = 800, height = 800, background_color = 'white', stopwords = stopwords,
                min_font_size = 10).generate(comment_words)

plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0)

plt.show()