import pyautogui
import time
#edge浏览器
for i in range(28):
    time.sleep(1)
    pyautogui.click(445,599,button='left')
    time.sleep(3)

    # 获取页面的总高度  
    total_height = pyautogui.size()[1]  
    # 滚动到底部  
    pyautogui.scroll(-total_height)
    time.sleep(1)
    pyautogui.click(1159, 959, button='left')
    time.sleep(3)
    pyautogui.click(1192, 833, button='left')
    time.sleep(3)
    pyautogui.click(1250, 831, button='left')
    time.sleep(1)
