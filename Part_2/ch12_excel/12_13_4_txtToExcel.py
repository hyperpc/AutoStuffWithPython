import sys, os
from openpyxl.workbook import Workbook
    
def txtToExcel():
    currentPath = os.path.dirname(sys.argv[0])
    txtFiles = ['1.txt', '2.txt', '3.txt']
    excelPath = os.path.join(currentPath, 'txtExcel.xlsx')

    wb = Workbook()
    activeSheet = wb.active

    for i in range(0, len(txtFiles)):
        txtFilePath = os.path.join(currentPath, txtFiles[i])
        txtFile = open(txtFilePath)
        lines = txtFile.readlines()
        for j in range(0, len(lines)):
            activeSheet.cell(j+1, i+1).value = lines[j]
    wb.save(excelPath)

def main():
    txtToExcel()

if __name__ == '__main__':
    main()