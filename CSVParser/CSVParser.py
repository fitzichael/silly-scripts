import csv
import sys
import pandas as pd

def convert_string_to_search(string):
    new_string = ""
    for c in range(len(string)):
        if string[c] == ' ':
            new_string += "+"
        else:
            new_string += string[c]
    return new_string

f = open(sys.argv[1])
reader = csv.reader(f)
spreadsheet = []
spreadsheet_iter = 0

for row in reader:
    row_to_add = []
    for i in range(len(row)):
        row_to_add.append(row[i])
    spreadsheet.append(row_to_add)
    spreadsheet_iter += 1
print(spreadsheet)
for row in spreadsheet[1:]:
    search = convert_string_to_search(row[2])
    print(search)
    url = r'https://connectny.info/search~S0/?searchtype=l&searcharg=' + search
    tables = pd.read_html(url)
    library_table = []
    for i in range(len(tables)):
        if tables[i][0][0] == "Library":
            library_table = tables[i]
    library_other_than_rensalaer = False
    for library in library_table[0]:
        if (library != "Rensselaer"):
            library_other_than_rensalaer = True
    if library_other_than_rensalaer:
        row[1] = 'y'
    else:
        row[1] = 'n'
print(spreadsheet)


#writing to the csv afterwards
w = open('./results.csv', mode = 'w')
writer = csv.writer(w, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
for i in range(len(spreadsheet)):
    writer.writerow(spreadsheet[i])
f.close()
w.close()