import pyautogui
import time
import tkinter as tk  
from tkinter import messagebox
#edge浏览器
def show_popup():  
    root = tk.Tk()  
    root.withdraw()  # 隐藏主窗口  
    messagebox.showinfo("信息", "Python程序运行结束！") 

for i in range(19):
    time.sleep(1)
    pyautogui.click(450,595,button='left')
    time.sleep(3)

    # 获取页面的总高度  
    total_height = pyautogui.size()[1] 
    time.sleep(1) 
    # 滚动到底部  
    pyautogui.scroll(-total_height)
    time.sleep(1)
    pyautogui.click(1170, 955, button='left')
    time.sleep(3)
    pyautogui.click(1200, 830, button='left')
    time.sleep(3)
    pyautogui.click(1260, 830, button='left')
    time.sleep(1)
# 程序结束时调用弹窗  
show_popup()