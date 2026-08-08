import openpyxl as xl
workbook = xl.load_workbook('data/transactions.xlsx')
worksheet = workbook['Sheet1']
cell = worksheet['a1']
cell=worksheet.cell(1,1)
print (worksheet.max_column)


for row in range(2, worksheet.max_row + 1):
    for col in range(1, worksheet.max_column + 1):
        cell = worksheet.cell(row, col)
        print(cell.value)