import pyautogui,time
# 确定按钮的坐标
nameField=(648, 401)
submitButton=(648, 505)
submitButtonColor=(255, 255, 255)
submitAnotherLink=(648, 604)

formData=[{'name':'Alice','fear':'eavesdroppers','source':'wand',
           'robocop':4,'comments':'Tell Bob I said hi.'},]

for person in formData:
    print('>>> 5 second pause to let uwer press CTRL-C <<<')
    time.sleep(5)
    while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
        time.sleep(0.5)
        print('Entering %s info...' % (person['name']))
        pyautogui.typewrite(person['name']+'\t')
        pyautogui.typewrite(person['fear']+'\t')
        if person['source'] == 'wand':
            pyautogui.typewrite(['down','\t'])
        elif person['source'] == 'amulet':
            pyautogui.typewrite(['down','down','\t'])
        elif person['source'] == 'crystal ball':
            pyautogui.typewrite(['down','down','down','\t'])
        elif person['source'] == 'money':
            pyautogui.typewrite(['down','down','down','down','\t'])
        if person['robocop'] == 1:
            pyautogui.typewrite([' ','\t'])
        elif person['robocop'] == 2:
            pyautogui.typewrite(['right','\t'])
        elif person['robocop'] == 3:
            pyautogui.typewrite(['right','right','\t'])
        elif person['robocop'] == 4:
            pyautogui.typewrite(['right','right','right','\t'])
        elif person['robocop'] == 5:
            pyautogui.typewrite(['right','right','right','right','\t'])
        pyautogui.typewrite(person['comments']+'\t')
        pyautogui.press('enter')
        print('Clicked submit')
        time.sleep(5)
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])