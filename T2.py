import pyautogui
import time

for i in range(8):
    time.sleep(1)
    pyautogui.click(486,635,button='left')
    time.sleep(3)

    # 获取页面的总高度  
    total_height = pyautogui.size()[1]  
    # 滚动到底部  
    pyautogui.scroll(-total_height)
    time.sleep(1)
    pyautogui.click(1274, 915, button='left')
    time.sleep(3)
    pyautogui.click(1192, 833, button='left')
    time.sleep(3)
    pyautogui.click(1250, 831, button='left')
    time.sleep(1)
