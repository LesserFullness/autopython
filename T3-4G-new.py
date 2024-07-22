import pandas as pd  
import matplotlib.pyplot as plt  
import numpy as np  
from matplotlib.font_manager import FontProperties  
import tkinter as tk  
from tkinter import filedialog  
import os  

# 设置字体为SimHei，这是一种常见的支持中文的字体 
font = FontProperties(fname="D:/OneDrive/code/autopython/SimHei.ttf")  

# 初始化Tkinter以选择文件  
root = tk.Tk()  
root.withdraw()  # 隐藏主窗口  
file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])  

# 读取Excel文件  
df = pd.read_excel(file_path)  

# 创建文件夹并保存折线图的函数  
def save_chart_to_folder(folder_name, chart_name, data):  
    if not os.path.exists(folder_name):  
        os.makedirs(folder_name)  
    plt.savefig(os.path.join(folder_name, f'{chart_name}.png'), dpi=200)  

# 遍历每一行数据，绘制折线图并保存  
for index, row in df.iterrows():  
    # 获取当前行的数据  
    folder_name = str(row['文件夹名称'])  # 文件夹名称在第一列  
    chart_name = str(row['标题'])  # 图表名称在第二列  
    data_to_plot = row[2:].tolist()  # 数据从第三列开始，转换为列表  

    # 绘制折线图  
    fig, ax = plt.subplots(figsize=(7, 4))  
    plt.plot(data_to_plot, linewidth=3.0)  

    # 设置x轴和y轴的边界值
    plt.xlim([0, len(data_to_plot) - 1])  # 设置x轴边界值，基于数据长度  
    plt.ylim([-130, -60])  # 设置y轴边界值  

    # 隐藏默认的x轴刻度标签和刻度线  
    ax.xaxis.set_ticks_position('none')  # 隐藏x轴刻度线  
    ax.set_xticklabels([])  # 隐藏x轴刻度标签
    # 设置x轴的刻度间隔和标签
    x_ticks = np.arange(0, len(data_to_plot), 3)  # 每隔3个数据点设置一个刻度  
    x_labels = ['PRB{}'.format(i*3) for i in range(len(x_ticks) + 1)]  # 生成对应的标签
    
    # 在顶部添加自定义的x轴刻度标签  
    for xtick, label in zip(x_ticks, x_labels):  
        # 添加垂直文本
        ax.text(xtick, 0.89, label, ha='center', va='bottom', rotation=90, fontsize=6, transform=ax.get_xaxis_transform()) 

    # 在多个y处添加透明度为50%的线条 
    y_values = [-130, -120, -110, -100, -90, -80, -70, -60]  
    for y in y_values:  
        plt.plot([0, len(data_to_plot) - 1], [y, y], color='gray', linestyle='-', linewidth=0.5, alpha=0.5)  


    # 隐藏顶部和右侧的轴线
    ax.spines['right'].set_color('none')  # 隐藏右边的轴线
    ax.spines['left'].set_color('none')  # 隐藏左边的轴线
    ax.spines['top'].set_color('none')  # 隐藏顶部的轴线
    ax.spines['bottom'].set_color('none')  # 隐藏底部的轴线

    # 隐藏所有刻度线
    plt.tick_params(length=0)
    
    # 添加标题，并使用SimHei字体
    ax.set_title(chart_name, fontproperties=font, fontsize=10)
    # 缩小X轴标签字体  
    #ax.tick_params(axis='x', labelsize=5)  # 将X轴标签字体大小设置为5

    # 保存折线图到指定文件夹  
    save_chart_to_folder(folder_name, chart_name, data_to_plot)  

    # 关闭图形窗口以释放内存  
    plt.close(fig) 

# 清理Tkinter资源（如果需要的话）  
root.destroy()