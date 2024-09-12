import openpyxl
path = "excel data.xlsx"
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active
cell_obj=sheet_obj['A1':'C6']
for cell1,cell2,cell3 in cell_obj:
    print("%-20s %-20s %-20s"%(cell1.value,cell2.value,cell3.value))