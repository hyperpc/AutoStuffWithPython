#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - delete one keyword from clipboard.
#        py.exe mcb.pyw delete - delete all keywords from clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('D:\\pyAuto\\mcbAdvdata')

# Save clipboard content or to delete one keyword.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcbShelf.keys():
        del mcbShelf[sys.argv[2]]
    else:
        print('Not found keyword:' + sys.argv[2])
elif len(sys.argv) == 2:
# List keywords and load content or to delete all keywords.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        for k in mcbShelf.keys():
            del mcbShelf[k]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

'''
#
# debug the content (keys and values)
#
mcbShelfR = shelve.open('D:\\pyAuto\\mcbAdvdata')
print(list(mcbShelfR.keys()))
print(list(mcbShelfR.values()))
mcbShelfR.close()
'''