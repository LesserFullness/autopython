import pandas as pd  
import matplotlib.pyplot as plt  
import numpy as np
from matplotlib.font_manager import FontProperties #字体
import tkinter as tk
from tkinter import filedialog

# 设置字体为SimHei，这是一种常见的支持中文的字体  
font = FontProperties(fname="fonts/SimHei.ttf")    

root=tk.Tk()
root.withdraw() #隐藏主窗口

#打开文件对话框，选择文件
file_path=filedialog.askopenfilename(filetypes=[("Excel Files","*.xlsx")])
# 读取Excel文件  
df=pd.read_excel(file_path)

#遍历每一行数据，绘制折线图并保存
for i in range(len(df)):
    #获取当前行的数据
    row=df.iloc[i]
    #获取折线图名称和数据
    chart_name=row.iloc[0]
    data=row[1:]
    #绘制折线图
    plt.figure(figsize=(7,4)) #创建一个新的图形窗口,7英寸宽，4英寸高
    plt.plot(data,linewidth=3.0) #折线的宽度是3

    # 设置x轴和y轴的边界值  
    plt.xlim([0, 99])  # 设置x轴边界值，这里设置为0到10  
    plt.ylim([-130,-60])  # 设置y轴边界值，这里设置为-130到-60

    # 设置x轴的刻度间隔和标签  
    plt.xticks(np.arange(0, 100, 3), ['PRB0', 'PRB3', 'PRB6', 'PRB9', 'PRB12', 'PRB15', 'PRB18', 'PRB21', 'PRB24', 'PRB27', 'PRB30',
                                'PRB33', 'PRB36', 'PRB39', 'PRB42', 'PRB45', 'PRB48', 'PRB51', 'PRB54', 'PRB57', 'PRB60', 'PRB63',
                                'PRB66', 'PRB69', 'PRB72', 'PRB75', 'PRB78', 'PRB81', 'PRB84', 'PRB87', 'PRB90', 'PRB93', 'PRB96',
                                'PRB99'], rotation=270)

    # 在多个y处添加透明度为50%的线条  
    y_values = [-120, -110, -100,-90,-80,-70]  
    for y in y_values:  
        plt.plot([0, 99], [y, y], color='gray', linestyle='--', alpha=0.5)

    # 添加标题，并使用SimHei字体
    plt.title(chart_name, fontproperties=font)

    # 保存折线图
    plt.savefig(f'{chart_name}.png', dpi=200)
    plt.close()