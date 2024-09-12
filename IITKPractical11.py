import openpyxl
path = "excel data.xlsx"
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active
cell_obj=sheet_obj['A1':'B6']
for cell1,cell2 in cell_obj:
    print(cell1.value,cell2.value)