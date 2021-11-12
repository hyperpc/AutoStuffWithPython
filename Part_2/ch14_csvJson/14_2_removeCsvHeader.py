import csv, sys, os

def removeHeader():
    currentPath = os.path.dirname(sys.argv[0])
    srcPath = os.path.join(currentPath, 'headerNotRemoved')
    destPath = os.path.join(currentPath, 'headerRemoved')
    os.makedirs(destPath, exist_ok=True)
    # loop through every file in the current working directory.
    for csvFileName in os.listdir(srcPath):
        if not csvFileName.endswith('.csv'):
            continue # skip non-csv files
        print('Removing header from ', csvFileName + '...')
        #read the csv file in(skipping first row)
        csvRows = []
        csvFileObj = open(os.path.join(srcPath, csvFileName))
        reader = csv.reader(csvFileObj)
        for row in reader:
            if reader.line_num == 1:
                continue # skip first row
            csvRows.append(row)
        csvFileObj.close()
        #write out the csv file
        csvFileObj = open(os.path.join(destPath, csvFileName), 'w', newline='')
        writer = csv.writer(csvFileObj)
        #for row in csvRows:
        #    writer.writerow(row)
        writer.writerows(csvRows)
        csvFileObj.close()

def main():
    removeHeader()

if __name__ == '__main__':
    main()