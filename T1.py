import openpyxl
import pyautogui
import time
import pandas as pd
import pyperclip

df = pd.read_excel('T1.xlsx')
data_dict = df.to_dict(orient='records')

for gd in data_dict:
    #新建
    pyautogui.click(198, 950, button='left')
    time.sleep(1)
    #工单主题
    pyautogui.click(575, 390, button='left')
    pyperclip.copy(gd['key'])
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.typewrite("\n", interval=2)
    time.sleep(1)
    #项目
    pyautogui.click(576, 437, button='left')
    time.sleep(0.5)
    pyautogui.click(662, 491, button='left')
    time.sleep(0.5)
    pyautogui.click(743, 544, button='left')
    time.sleep(0.5)
    pyautogui.click(743, 571, button='left')
    time.sleep(1)
    #工作量记录
    #设备类型
    pyautogui.click(640, 588, button='left')
    time.sleep(0.5)
    pyautogui.click(640, 625, button='left')
    time.sleep(0.5)
    #服务内容
    pyautogui.click(795, 581, button='left')
    time.sleep(0.5)
    pyautogui.click(800, 644, button='left')
    time.sleep(0.5)
    #数量
    pyautogui.click(1224, 583, button='left')
    time.sleep(0.5)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('1')
    time.sleep(1)
    #处理人
    pyautogui.click(1391, 699, button='left')
    time.sleep(2)
    pyautogui.click(1138, 569, button='left')
    time.sleep(0.5)
    pyautogui.click(1288, 818, button='left')
    time.sleep(0.5)
    pyautogui.click(1757, 1073, button='left')
    time.sleep(1)
    #截止时间
    pyautogui.click(660, 757, button='left')
    time.sleep(0.5)
    pyautogui.click(598, 1010, button='left')
    time.sleep(1)
    #审批人
    pyautogui.click(1390, 810, button='left')
    time.sleep(0.5)
    pyautogui.click(996, 570, button='left')
    time.sleep(0.5)
    pyperclip.copy('徐强')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.click(1205, 567, button='left')
    time.sleep(0.5)
    pyautogui.doubleClick(1214, 749, button='left')
    time.sleep(0.5)
    pyautogui.click(1649, 1074, button='left')
    time.sleep(1)
    #工单内容
    pyautogui.click(1336, 977, button='left')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyperclip.copy(gd['name'])
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    #提交
    pyautogui.click(408, 1368, button='left')
    time.sleep(1)
    #操作成功
    pyautogui.click(1286, 830, button='left')
    time.sleep(10)
