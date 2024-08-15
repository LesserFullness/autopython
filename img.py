from PIL import Image  

# 定义一个更细致的ASCII字符集  
ASCII_CHARS = "@%#*+=-:. "  

# 将图片转换为灰度图像  
def to_grayscale(image):  
    return image.convert("L")  

# 调整图像大小  
def resize_image(image, new_width=50):  
    # 这里我们保持宽高比，但只设置新的宽度  
    width, height = image.size  
    ratio = height / width  
    new_height = int(new_width * ratio)  
    return image.resize((new_width, new_height))  

# 将灰度值映射到ASCII字符  
def map_pixels_to_ascii(image, chars=ASCII_CHARS):  
    pixels = image.getdata()  
    ascii_str = ""  
    for pixel in pixels:  
        # 将灰度值线性映射到ASCII字符索引  
        char_index = int((pixel / 255.0) * (len(chars) - 1))  
        ascii_str += chars[char_index]  
    return ascii_str  

# 将ASCII字符串拆分成多行  
def split_ascii_str(ascii_str, width):  
    return "\n".join(ascii_str[i:i + width] for i in range(0, len(ascii_str), width))  

# 主函数  
def image_to_ascii(image_path, output_file="output.txt", width=150):  
    try:  
        image = Image.open(image_path)  
        image = to_grayscale(image)  
        image = resize_image(image, width)  
        ascii_str = map_pixels_to_ascii(image)  
        ascii_str = split_ascii_str(ascii_str, width)  
        
        with open(output_file, "w", encoding="utf-8") as f:  
            f.write(ascii_str)  
        
        print(f"ASCII艺术图像已保存到 {output_file}")  
    except FileNotFoundError:  
        print(f"文件 {image_path} 未找到。")  
    except Exception as e:  
        print(f"发生错误：{e}")  

# 调用函数进行转换  
image_to_ascii("D:/OneDrive/code/2.jpg", width=200)