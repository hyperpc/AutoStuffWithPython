import csv, sys, os

def writeCSV():
    currentPath = os.path.dirname(sys.argv[0])
    outputFilePath = os.path.join(currentPath, 'output.csv')
    outputFileObj = open(outputFilePath, 'w', newline='')
    writer = csv.writer(outputFileObj)
    writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
    writer.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
    writer.writerow([1, 2, 3.1415926, 4])
    outputFileObj.close()

def main():
    writeCSV()

if __name__ == '__main__':
    main()