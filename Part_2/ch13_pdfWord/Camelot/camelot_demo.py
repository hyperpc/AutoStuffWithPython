import camelot, sys, os

def pdfToCsv():
    '''
    通过Camelot-py库，从pdf幅度去数据，并导出为csv
    download sample file from github:
    https://github.com/camelot-dev/camelot.git
    '''
    current_path = os.path.dirname(sys.argv[0])
    fname = os.path.join(current_path, 'pdf', 'foo.pdf')
    tables = camelot.read_pdf(fname)
    print('tables:\n',tables)
    # json, excel, html, markdown, sqlite
    tables.export(os.path.join(current_path, 'foo_all.csv'), f='csv', compress=True)
    print('tables[0]:\n',tables[0])
    print('tables[0].parsing_report:\n',tables[0].parsing_report)
    # to_json, to_excel, to_html, to_markdown, to_sqlite
    tables[0].to_csv(os.path.join(current_path, 'foo_0.csv'))
    # get a pandas DataFrame!
    print('tables[0].df:\n',tables[0].df)

def main():
    pdfToCsv()

if __name__ == '__main__':
    main()