import matplotlib.pyplot as plt  

# 创建数据  
x = [1, 2, 3, 4, 5]  
y = [10, 8, 6, 4, 2]  

# 创建图形  
fig, ax = plt.subplots()  

# 绘制折线图  
ax.plot(x, y)  

# 将x轴位置设置为10刻度处  
ax.set_xticks([10])  
ax.spines['bottom'].set_position('zero')  
ax.spines['top'].set_color('none')  
ax.spines['right'].set_color('none')  
ax.spines['left'].set_position('zero')  
ax.xaxis.set_ticks_position('bottom')  
ax.set_xlabel('X轴标签')  
ax.set_title('标题')   

# 显示图形  
plt.show()