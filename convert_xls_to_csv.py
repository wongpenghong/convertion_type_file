import openpyxl
import csv

wb = openpyxl.load_workbook('data_sentiment.xlsx')
sh = wb.get_active_sheet()
with open('data_sentiment.csv', 'w', newline="") as f:  # open('test.csv', 'w', newline="") for python 3
    c = csv.writer(f)
    for r in sh.rows:
        c.writerow([cell.value for cell in r])