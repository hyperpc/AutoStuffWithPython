import traceback, sys, os
currentPath = os.path.dirname(sys.argv[0])
try:
    raise Exception('This is the error message.')
except:
    errorFile = open(os.path.join(currentPath, 'errInfo.log'), 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errInfo.log.')