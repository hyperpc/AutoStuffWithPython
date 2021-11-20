import pyautogui, time

def keepScreenAlive():
    print('Press Ctrl-C to quit.')
    try:
        distance = 100
        width, height = pyautogui.size()
        pyautogui.moveTo(int(width/2), int(height/2), duration=0.25)
        while True:
            pyautogui.dragRel(distance, 0, duration=0.2) # move right
            pyautogui.dragRel(0, distance, duration=0.2) # move right
            pyautogui.dragRel(-distance, 0, duration=0.2) # move right
            pyautogui.dragRel(0, -distance, duration=0.2) # move right
            time.sleep(10)
    except KeyboardInterrupt:
        print('\nDone.')

def main():
    keepScreenAlive()

if __name__ == '__main__':
    main()