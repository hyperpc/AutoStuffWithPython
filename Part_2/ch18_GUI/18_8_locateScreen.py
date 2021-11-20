import pyautogui, sys, os

currentPath = os.path.dirname(sys.argv[0])
buttonFilePath = os.path.join(currentPath, 'file_explore.png')
first_matched_location = pyautogui.locateOnScreen(buttonFilePath)
print(first_matched_location)
all_matched_location = pyautogui.locateAllOnScreen(buttonFilePath)
print(list(all_matched_location))
#for item in all_matched_location:
#    print(item)

center_location = pyautogui.center(first_matched_location)
print(center_location)
pyautogui.click(center_location)

print('Done!')