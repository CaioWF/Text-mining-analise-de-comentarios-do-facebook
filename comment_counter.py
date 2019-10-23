import csv

def main():
    with open('./Comentarios_csv/Reforma_Previdencia/For region/Sul/NeutralPhrases.csv') as csvfile:
            csv_dict_reader = csv.DictReader(csvfile)
            line_number = 0
            for row in csv_dict_reader:
                line_number += 1
            print("finish!\n")
            print("comment number is ", line_number)

if __name__ == '__main__':
    main()