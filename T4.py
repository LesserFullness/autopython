import pyautogui,time

submitButton=(1272, 1047)
submitButtonColor=(70, 130, 188)

for i in range(11):
    pyautogui.click(486,635,button='left')
    #print('>>> 5 second pause to let uwer press CTRL-C <<<')
    time.sleep(3)
    # 获取页面的总高度  
    total_height = pyautogui.size()[1]  
    # 滚动到底部  
    pyautogui.scroll(-total_height)
    time.sleep(1)
    while pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
        #print('可以点击确认按钮了')
        pyautogui.click(1272, 1047, button='left')
        time.sleep(1)
        pyautogui.click(1191, 829, button='left')
        time.sleep(1)
        pyautogui.click(1260, 829, button='left')
        time.sleep(3)


