import csv, sys, os

def readCSV():
    currentPath = os.path.dirname(sys.argv[0])
    exampleFilePath = os.path.join(currentPath, 'example.csv')
    fileObj = open(exampleFilePath)
    reader = csv.reader(fileObj)
    data = list(reader)
    print('list(reader) = ', data)
    print('data[0][0] = ', data[0][0])
    print('data[0][1] = ', data[0][1])
    print('data[0][2] = ', data[0][2])
    print('data[1][1] = ', data[1][1])
    print('data[6][1] = ', data[6][1])
    
    fileObj = open(exampleFilePath)
    reader = csv.reader(fileObj)
    for row in reader:
        print('Row #', str(reader.line_num), ' ', str(row))

def main():
    readCSV()

if __name__ == '__main__':
    main()