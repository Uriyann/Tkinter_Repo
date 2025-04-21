from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws['C3'] = "hallo excel"
wb.save("exam.xlsx")