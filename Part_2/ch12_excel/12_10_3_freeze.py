import openpyxl, sys, os

def freezeRow():
    currentPath = os.path.dirname(sys.argv[0])
    excelPath = os.path.join(currentPath, "produceSales.xlsx")
    freezePath = os.path.join(currentPath, "freezeExample.xlsx")

    wb = openpyxl.load_workbook(excelPath)
    activeSheet = wb.active
    activeSheet.freeze_panes = 'A2'
    wb.save(freezePath)

def main():
    freezeRow()

if __name__ == '__main__':
    main()