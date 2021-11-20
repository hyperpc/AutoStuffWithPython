import pyautogui

img = pyautogui.screenshot()
target_color = img.getpixel((1600, 60))
print(target_color)
print(pyautogui.pixelMatchesColor(1600, 60, target_color))
print(pyautogui.pixelMatchesColor(1600, 200, target_color))