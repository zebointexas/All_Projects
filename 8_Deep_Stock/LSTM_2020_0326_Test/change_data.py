import xlrd
import csv


def delete_first_lines(self, filename, count):
    fin = open(filename, 'r')
    a = fin.readlines()
    fout = open(filename, 'w')
    b = ''.join(a[count:])
    fout.write(b)

def csv_from_excel():

    path = "/Users/dior/Documents/GitHub/iProject/8_Deep_Stock/LSTM_2020_0326_Test/data/tmp/";

    wb = xlrd.open_workbook(path+'1.xlsx')
    sh = wb.sheet_by_name('Sheet 1')

    your_csv_file = open(path+'1.csv', 'w')


    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    i = 0;

    for rownum in range(sh.nrows):

        i += 1
        if(i>27):
             wr.writerow(sh.row_values(rownum))


    your_csv_file.close()



# runs the csv_from_excel function:
csv_from_excel()