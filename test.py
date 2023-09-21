
# 导入必要的库  
from PyInstaller import __main__  

# 设置字体文件的路径  
font_path = "D:/OneDrive/code/autopython/fonts/SimHei.ttf"  

# 打包可执行文件，并添加字体文件  
__main__.run([  
    "T3LineChart.py",
    "--add-data", f"{font_path};.",
    "-w",
    "-F" 
])