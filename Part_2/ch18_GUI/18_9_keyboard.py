import time
import pyautogui, sys, os, subprocess

currentPath = os.path.dirname(sys.argv[0])
fname = os.path.join(currentPath, '18_9_keyboard.txt')
notepad = 'C:\\Windows\\notepad.exe'
file = open(fname, 'w', encoding='utf-8')
file.write('')
file.close()
subprocess.Popen([notepad, fname])

time.sleep(5)
# 18.9.1
pyautogui.click(100,100)
pyautogui.typewrite('Hello world!', 0.25)
# 18.9.2
pyautogui.typewrite('\r\n', 0.25)
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y', 'right', 'right'], 0.25)
# 18.9.3
pyautogui.typewrite('\r\n', 0.25)
pyautogui.keyDown('shift')
pyautogui.press('4')
pyautogui.keyUp('shift')
# 18.9.4
pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')

#pyautogui.typewrite('\r\n', 0.25)
pyautogui.hotkey('ctrlleft', 'v')

#pyautogui.typewrite('\r\n', 0.25)
time.sleep(5)

print('Done.')