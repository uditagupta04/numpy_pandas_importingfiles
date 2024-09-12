import openpyxl
path = "excel data.xlsx"
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active
cell_obj = sheet_obj.cell(row = 4,column = 3)
print(cell_obj.value)