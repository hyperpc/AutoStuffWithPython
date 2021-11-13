import subprocess, sys, os, time

def main():
    currentPath = os.path.dirname(sys.argv[0])
    readmeFilePath = os.path.join(currentPath, 'README.MD')
    # 15.8
    calc = subprocess.Popen('c:\\Windows\\System32\\calc.exe')
    print('calc.poll() == None', calc.poll() == None)
    print('calc.wait() = ', calc.wait())
    print('calc.poll() = ', calc.poll())
    # 15.8.1
    readme = subprocess.Popen(['c:\\Windows\\System32\\notepad.exe', readmeFilePath])
    readme.wait()
    # 15.8.5
    helloFilePath = os.path.join(currentPath, 'hello.txt')
    fileObj = open(helloFilePath, 'w')
    fileObj.write('Hello world!')
    fileObj.close()
    hello = subprocess.Popen(['start', helloFilePath], shell=True)
    time.sleep(10)

if __name__ == '__main__':
    main()