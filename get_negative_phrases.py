import csv

def main():
    #trocar o caminho da entrada
    with open('./Comentarios_csv/Reforma_Previdencia/For region/Norte/CommentsNorteClassified.csv') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file)
        #trocar o caminho da saída
        with open('./Comentarios_csv/Reforma_Previdencia/For region/Norte/NegativePhrases.csv', 'w') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow(["Comentario"])
            for row in csv_dict_reader:
                if row["Comentário"] and row["Sentimento"] == "negativo":
                    spamwriter.writerow([row["Comentário"]])
               
            print("finish!")

if __name__ == '__main__':
    main()