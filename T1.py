import openpyxl
import pyautogui
import time
import pandas as pd
import pyperclip
#谷歌浏览器
df = pd.read_excel('T1.xlsx')
data_dict = df.to_dict(orient='records')

for gd in data_dict:
    #新建
    pyautogui.click(205, 880, button='left')
    time.sleep(2)
    #工单主题
    pyautogui.click(620, 393, button='left')
    pyperclip.copy(gd['key'])
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.typewrite("\n", interval=2)
    time.sleep(1)
    #项目
    pyautogui.click(626, 437, button='left')
    time.sleep(1)
    pyautogui.click(662, 491, button='left')
    time.sleep(0.5)
    pyautogui.click(708, 570, button='left')
    time.sleep(0.5)
    pyautogui.click(748, 602, button='left')
    time.sleep(1)
    #工作量记录
    #设备类型
    pyautogui.click(640, 585, button='left')
    time.sleep(0.5)
    pyautogui.click(646, 625, button='left')
    time.sleep(0.5)
    #服务内容/外部干扰
    pyautogui.click(795, 581, button='left')
    time.sleep(0.5)
    pyautogui.click(830, 840, button='left')
    time.sleep(0.5)
    #数量
    pyautogui.click(1245, 580, button='left')
    time.sleep(0.5)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('1')
    time.sleep(2)
    #处理人
    pyautogui.click(1400, 695, button='left')
    time.sleep(2)
    pyautogui.click(1140, 570, button='left')#全选
    time.sleep(1)
    pyautogui.click(1770, 1070, button='left')
    time.sleep(0.5)
    #pyautogui.click(1757, 1073, button='left')
    time.sleep(1)
    #截止时间
    pyautogui.click(874, 752, button='left')#点击月历图标
    time.sleep(1)
    pyautogui.click(810, 795, button='left')#月数翻页
    time.sleep(1)
    pyautogui.click(830, 895, button='left')
    time.sleep(1)
    #审批人
    pyautogui.click(1400, 800, button='left')
    time.sleep(1)
    pyautogui.click(970, 575, button='left')
    time.sleep(0.5)
    pyperclip.copy('沈辰')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.click(1200, 570, button='left')#搜索
    time.sleep(1)
    pyautogui.doubleClick(1250, 570, button='left')#全选
    time.sleep(0.5)
    pyautogui.click(1645, 1075, button='left')
    time.sleep(1)
    #是否省公司审批
    pyautogui.click(653, 854, button='left')
    time.sleep(0.5)
    #工单内容
    pyautogui.click(874, 939, button='left')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyperclip.copy(gd['name'])
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    # 获取页面的总高度  
    total_height = pyautogui.size()[1]  
    # 滚动到底部  
    pyautogui.scroll(-total_height)
    time.sleep(1)
    #提交
    pyautogui.click(410, 1305, button='left')
    time.sleep(15)
    #操作成功
    pyautogui.click(1290, 830, button='left')
    time.sleep(3)
