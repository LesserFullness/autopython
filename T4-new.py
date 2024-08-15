import pyautogui,time
#谷歌浏览器

for i in range(15):
    image_path = 'T4dianji.png'  
    # 使用locateOnScreen()查找图像  
    location = pyautogui.locateOnScreen(image_path)
    if location:  
        print(f"找到图像，位置：{location}")  
    # location是一个元组：(left, top, width, height)  
    # 你可以使用这些值来执行进一步的操作，如点击或移动鼠标到该位置  
        pyautogui.click(location[0] + location[2] // 2, location[1] + location[3] // 2)  # 点击图像中心 
        time.sleep(5)
    # 获取页面的总高度  
        total_height = pyautogui.size()[1]  
        time.sleep(0.5)
    # 滚动到底部  
        pyautogui.scroll(-total_height)
        time.sleep(2)
    #while pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
        #print('可以点击确认按钮了')
        pyautogui.click(1150, 1080, button='left')
        time.sleep(2)
        pyautogui.click(1220, 840, button='left')
        time.sleep(2)
        pyautogui.click(1285, 845, button='left')
        time.sleep(1)
    else:  
        print("未找到T4点击图像")
    #print('>>> 5 second pause to let uwer press CTRL-C <<<')
    


