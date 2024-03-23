import pandas as pd  
import matplotlib.pyplot as plt  
import numpy as np
from matplotlib.font_manager import FontProperties #字体
import tkinter as tk
from tkinter import filedialog
import os

# 设置字体为SimHei，这是一种常见的支持中文的字体  
font = FontProperties(fname="D:/OneDrive/code/autopython/SimHei.ttf")    

root=tk.Tk()
root.withdraw() #隐藏主窗口

#打开文件对话框，选择文件
file_path=filedialog.askopenfilename(filetypes=[("Excel Files","*.xlsx")])
# 读取Excel文件  
df=pd.read_excel(file_path)

# 创建文件夹并保存折线图
def save_chart_to_folder(folder_name, chart_name, data):
    if not os.path.exists(folder_name):  # 检查文件夹是否存在
        os.makedirs(folder_name)  # 如果文件夹不存在，则创建新文件夹
    os.chdir(folder_name)  # 切换到文件夹中
    plt.savefig(f'{chart_name}.png', dpi=200)  # 保存折线图
    os.chdir('..')  # 切换回原来的工作目录

#遍历每一行数据，绘制折线图并保存
for i in range(len(df)):
    #获取当前行的数据
    row=df.iloc[i]
    #获取文件夹名称
    folder_name = str(df.iloc[i, 0])  # 文件夹名称为A列的值
    #获取折线图名称和数据
    chart_name=row.iloc[1] # 折线图名称为B列的值
    data=row[2:] # 数据从C列开始
    #绘制折线图
    #plt.figure(figsize=(7,4)) #创建一个新的图形窗口,7英寸宽，4英寸高
    fig,ax=plt.subplots(figsize=(7,4))
    plt.plot(data,linewidth=3.0) #折线的宽度是3

    # 设置x轴和y轴的边界值  
    plt.xlim([0, 270])  # 设置x轴边界值，这里设置为0到10  
    plt.ylim([-130,-60])  # 设置y轴边界值，这里设置为-130到-60

    # 设置x轴的刻度间隔和标签  
    plt.xticks(np.arange(0, 272, 9), ['PRB0', 'PRB9', 'PRB18', 'PRB27', 'PRB36', 'PRB45', 'PRB54', 'PRB63', 'PRB72', 'PRB81', 'PRB90', 'PRB99',
                                'PRB108', 'PRB117', 'PRB126', 'PRB135', 'PRB144', 'PRB153', 'PRB162', 'PRB171', 'PRB180', 'PRB189', 'PRB198', 
                                'PRB207', 'PRB216', 'PRB225', 'PRB234', 'PRB243', 'PRB252', 'PRB261', 'PRB270'], rotation=290)

    # 在多个y处添加透明度为50%的线条  
    y_values = [-130,-120,-110, -100,-90,-80,-70,-60]  
    for y in y_values:  
        plt.plot([0, 272], [y, y], color='gray', linestyle='--', alpha=0.5)

    # 将x轴标签放在上边界轴线下  
    ax.xaxis.set_ticks_position('bottom')

    ax.spines['right'].set_color('none')  # 隐藏右边的轴线
    ax.spines['left'].set_color('none')  # 隐藏左边的轴线
    ax.spines['top'].set_color('none')  # 隐藏顶部的轴线
    ax.spines['bottom'].set_color('none')  # 隐藏底部的轴线
    # 添加标题，并使用SimHei字体
    #plt.title(chart_name, fontproperties=font)
    ax.set_title(chart_name, fontproperties=font, fontsize=10)
    # 缩小X轴标签字体  
    ax.tick_params(axis='x', labelsize=6)  # 将X轴标签字体大小设置为10

    # 保存折线图
    #plt.savefig(f'{chart_name}.png', dpi=200)
    #plt.show()
    #plt.close()
    # 保存折线图到文件夹中
    save_chart_to_folder(folder_name, chart_name, data)