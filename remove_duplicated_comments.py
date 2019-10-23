import csv

def main():
    with open('./Comentarios_csv/Massacre_Suzano/Diario_Online.csv') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file)
        prev_message = ""
        
        with open('./Comentarios_csv/Massacre_Suzano/only_comments/doldiarioonline.csv', 'w') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow(["Comentario"])
            #sentistrength
            for row in csv_dict_reader:
                if prev_message != row["message"] and row["message"]:
                    spamwriter.writerow([row["message"]])
                prev_message = row["message"]
            print("finish!")
    

if __name__ == '__main__':
    main()