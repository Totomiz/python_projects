import xlrd

book = xlrd.open_workbook('E:\docments\媒资.xls')
print('num of sheet is {0}'.format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
print("Cell D30 is {0}".format(sh.cell_value(rowx=0, colx=1)))

print(sh.row_values(0))
# print(sh.row_values(5000))
for x in sh.row_values(0):
    print(x)

# for rx in sh.col_values(1,0):
#     print(rx)

def findAllValue():
    count = 0
    for rx in range(sh.nrows):
        if sh.cell_value(rx, sh.ncols - 1) == "":
            continue
        else:
            print(sh.row(rx))
            count += 1
    print("All not empty item =",count)

findAllValue()

