import pyautogui  
import time  
import tkinter as tk  
from tkinter import messagebox  

def wait(seconds):  
    """等待指定秒数"""  
    time.sleep(seconds)  

def click_at(x, y, button='left'):  
    """在指定位置点击"""  
    pyautogui.click(x, y, button=button)  
    wait(1)  # 假设每次点击后需要等待1秒  

def scroll_to_bottom():  
    """滚动到页面底部"""  
    total_height = pyautogui.size()[1]  
    pyautogui.scroll(-total_height)  
    wait(1)  

def edge_operations():  
    """执行Edge浏览器的操作"""  
    for i in range(19):  
        click_at(450, 595)  
        wait(3)  
        scroll_to_bottom()  
        click_at(1170, 955)  
        wait(3)  
        click_at(1200, 830)  
        wait(3)  
        click_at(1260, 830)  
        wait(1)  

def show_popup():  
    """显示弹窗"""  
    root = tk.Tk()  
    root.withdraw()  # 隐藏主窗口  
    messagebox.showinfo("信息", "Python程序运行结束！")  

# 调用函数执行Edge浏览器的操作  
edge_operations()  

# 程序结束时调用弹窗  
show_popup()