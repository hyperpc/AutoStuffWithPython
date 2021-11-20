import pyperclip, sys, os, time
import pyautogui, subprocess

currentPath = os.path.dirname(sys.argv[0])
fname = os.path.join(currentPath, '18_5_3_numbers.txt')
notepad = 'C:\\Windows\\notepad.exe'

numbers = ''
for i in range(200):
    numbers += str(i) + '\n'

pyperclip.copy(numbers)

file = open(fname, 'w', encoding='utf-8')
file.write(pyperclip.paste())
file.close()

subprocess.Popen([notepad, fname])

time.sleep(5)

pyautogui.scroll(80, 100, 100)

time.sleep(5)

print('\nDone!')