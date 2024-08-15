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
    # 图像文件的路径  
    image_path = 'ancigongdanxinjian.png'  
    # 使用locateOnScreen()查找图像  
    location = pyautogui.locateOnScreen(image_path)
    if location:  
        print(f"找到图像，位置：{location}")  
    # location是一个元组：(left, top, width, height)  
    # 你可以使用这些值来执行进一步的操作，如点击或移动鼠标到该位置  
        pyautogui.click(location[0] + location[2] // 2, location[1] + location[3] // 2)  # 点击图像中心  
    else:  
        print("未找到按次工单新建图像")
    time.sleep(10)
    #工单主题
    pyautogui.click(625, 414, button='left')
    pyperclip.copy(gd['key'])
    print(gd['key'])
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.typewrite("\n", interval=2)
    time.sleep(2)
    #项目
    pyautogui.click(643, 465, button='left')
    time.sleep(1)
    pyautogui.click(785, 513, button='left')
    time.sleep(1)
    pyautogui.click(740, 595, button='left')
    time.sleep(1)
    pyautogui.click(740, 625, button='left')
    time.sleep(1)
    #工作量记录
    #设备类型
    pyautogui.click(640, 610, button='left')
    time.sleep(0.5)
    pyautogui.click(646, 650, button='left')
    time.sleep(0.5)
    #服务内容/外部干扰
    pyautogui.click(795, 610, button='left')
    time.sleep(0.5)
    pyautogui.click(830, 880, button='left')
    time.sleep(0.5)
    #数量
    pyautogui.click(1245, 610, button='left')
    time.sleep(0.5)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('1')
    time.sleep(2)
    #处理人
    pyautogui.click(1410, 720, button='left')
    time.sleep(2)
    #pyautogui.click(1140, 570, button='left')#全选
    pyautogui.click(970, 585, button='left')
    time.sleep(0.5)
    pyperclip.copy('余小龙')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    #pyautogui.click(1770, 1070, button='left')
    pyautogui.click(1090, 580, button='left')#搜索
    time.sleep(0.5)
    pyautogui.doubleClick(1140, 580, button='left')#全选
    time.sleep(1)
    pyautogui.click(1770, 1090, button='left') #确定
    time.sleep(1)
    #截止时间
    pyautogui.click(875, 780, button='left')#点击月历图标
    time.sleep(1)
    pyautogui.click(810, 825, button='left')#月数翻页
    time.sleep(1)
    pyautogui.click(830, 950, button='left')
    time.sleep(1)
    #审批人
    pyautogui.click(1410, 830, button='left')
    time.sleep(1)
    pyautogui.click(970, 585, button='left')
    time.sleep(0.5)
    pyperclip.copy('徐总梁')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.click(1200, 580, button='left')#搜索
    time.sleep(1)
    pyautogui.doubleClick(1250, 580, button='left')#全选
    time.sleep(0.5)
    pyautogui.click(1650, 1085, button='left')#确定
    time.sleep(1)
    #是否省公司审批
    pyautogui.click(650, 883, button='left')
    time.sleep(0.5)
    #工单内容
    pyautogui.click(875, 940, button='left')
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
    image_path = 'tijiao.png'  
    # 使用locateOnScreen()查找图像  
    location = pyautogui.locateOnScreen(image_path)
    if location:  
        print(f"找到图像，位置：{location}")  
    # location是一个元组：(left, top, width, height)  
    # 你可以使用这些值来执行进一步的操作，如点击或移动鼠标到该位置  
        pyautogui.click(location[0] + location[2] // 2, location[1] + location[3] // 2)  # 点击图像中心  
    else:  
        print("未找到提交图像")
    
    time.sleep(30)
    #操作成功
    pyautogui.click(1290, 830, button='left')
    time.sleep(3)