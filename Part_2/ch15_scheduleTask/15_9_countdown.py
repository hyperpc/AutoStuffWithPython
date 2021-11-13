#! python3
import time, subprocess, sys, os

def countdown():
    timeleft = 10
    while timeleft > 0:
        print(timeleft, '...', end='')
        time.sleep(1)
        timeleft -= 1
    print('Break time is over!')
    # at the end of the countdown, play a sound file
    currentPath = os.path.dirname(sys.argv[0])
    soundFilePath = os.path.join(currentPath, 'alarm.wav')
    subprocess.Popen(['start', soundFilePath], shell=True)

def main():
    countdown()

if __name__ == '__main__':
    main()
