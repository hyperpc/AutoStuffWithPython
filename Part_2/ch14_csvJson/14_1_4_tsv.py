import csv, sys, os

def writeTSV():
    currentPath = os.path.dirname(sys.argv[0])
    tsvFilePath = os.path.join(currentPath, 'example.tsv')
    tsvFileObj = open(tsvFilePath, 'w', newline='')
    writer = csv.writer(tsvFileObj, delimiter='\t', lineterminator='\n\n', quotechar='"', quoting = csv.QUOTE_MINIMAL)
    writer.writerow(['apples', 'oranges', 'grapes'])
    writer.writerow(['eggs', 'bacon', 'ham', 123])
    writer.writerow(['ham,ham', 'ham', 'ham', 'ham', 'ham', 'ham'])
    tsvFileObj.close()

def main():
    writeTSV()

if __name__ == '__main__':
    main()