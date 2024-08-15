import pyautogui,time
#谷歌浏览器
#submitButton=(1146, 1080)
#submitButtonColor=(255, 255, 255)

for i in range(4):
    time.sleep(1)
    pyautogui.click(440,620,button='left')
    #print('>>> 5 second pause to let uwer press CTRL-C <<<')
    time.sleep(3)
    # 获取页面的总高度  
    total_height = pyautogui.size()[1]  
    # 滚动到底部  
    pyautogui.scroll(-total_height)
    time.sleep(1)
    #while pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
        #print('可以点击确认按钮了')
    pyautogui.click(1150, 1080, button='left')
    time.sleep(2)
    pyautogui.click(1220, 840, button='left')
    time.sleep(2)
    pyautogui.click(1285, 845, button='left')
    time.sleep(1)


