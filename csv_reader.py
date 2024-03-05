import csv

def csv_reader(csv_file:str)-> list:
    list_to_return = []
    with open(csv_file) as csvfile:
        content = csv.reader(csvfile)
        worldcities = list(content)                             #puts the content of the csv into a list, to index each line      


    for line in worldcities:                                    #for each line, append necessary column
        list_to_return.append(line[1])                          #change this accordingly

    return list_to_return
