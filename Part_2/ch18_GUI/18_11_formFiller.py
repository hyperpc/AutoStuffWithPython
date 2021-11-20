#! python3
# formFiller.py - Automatically fills in the form.

import pyautogui, time

# set these to the correct coordinates for your computer.
nameField = (648, 319)
submitBtn = (651, 817)
submitBtnColor = (75, 141, 249)
submitAnotherLink = (760, 224)

formData = [
    {
        'name':'Alice',
        'fear':'eavesdroppers',
        'source':'wand',
        'robocop':4,
        'comments':'Tell Bob I said hi.'
    },{
        'name':'Bob',
        'fear':'bees',
        'source':'amulet',
        'robocop':4,
        'comments':'n/a'
    },{
        'name':'Carol',
        'fear':'puppets',
        'source':'crystal ball',
        'robocop':1,
        'comments':'Please take the puppets out of the break room.'
    },{
        'name':'Alex Murphy',
        'fear':'ED-209',
        'source':'money',
        'robocop':5,
        'comments':'Protect the innocent. Serve the public trust. Upload the law.'
    }
]
pyautogui.PAUSE = 0.5

for person in formData:
    # give the user a chance to kill the script.
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(0.5)
    # wait until the form page for loaded.
    while not pyautogui.pixelMatchesColor(submitBtn[0], submitBtn[1], submitBtnColor):
        time.sleep(0.5)

        print('Entering %s info...' % (person['name']))
        pyautogui.click(nameField[0], nameField[1])
        # fill out the name field
        pyautogui.typewrite(person['name'] + '\t')
        # fill out the Greatest Fear(s) field.
        pyautogui.typewrite(person['fear'] + '\t')
        # fill out the source of wizard powers field.
        if person['source'] == 'wand':
            pyautogui.typewrite(['down', '\t'])
        elif person['source'] == 'amulet':
            pyautogui.typewrite(['down', 'down', '\t'])
        elif person['source'] == 'crystal ball':
            pyautogui.typewrite(['down', 'down', 'down', '\t'])
        elif person['source'] == 'money':
            pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])
        # fill out the robacop field.
        if person['robacop'] == 1:
            pyautogui.typewrite([' ', '\t'])
        elif person['robacop'] == 2:
            pyautogui.typewrite(['right', '\t'])
        elif person['robacop'] == 3:
            pyautogui.typewrite(['right', 'right', '\t'])
        elif person['robacop'] == 4:
            pyautogui.typewrite(['right', 'right', 'right','\t'])
        elif person['robacop'] == 5:
            pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])
        # fill out the additional  comments field.
        pyautogui.typewrite(person['comments'] + '\t')
        # click submit.
        pyautogui.press('enter')
        # wait until form page has loaded.
        print('Clicked Submit.')
        time.sleep(5)
        # click the submit another response link.
        pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])