import sys, os, openpyxl

# 12.5.1
currentPath = os.path.dirname(sys.argv[0])
excelPath = os.path.join(currentPath, "writeData.xlsx")
# load the file
wb = openpyxl.load_workbook(excelPath)
activeSheet = wb.active
activeSheet.title = 'Spam Spam Spam'
wb.save(excelPath)

# 12.5.2
wb.create_sheet() # 'Sheet' default
wb.create_sheet(index=0, title='First Sheet')
wb.create_sheet(index=2, title='Middle Sheet')
print(wb.sheetnames)
wb.remove(wb['Sheet'])
wb.remove(wb['Middle Sheet'])
print(wb.sheetnames)

# 12.5.3
activeSheet = wb.active
activeSheet.cell(1, 1, 'Hello world!')
print(activeSheet.cell(1, 1).value)
wb.save(excelPath)