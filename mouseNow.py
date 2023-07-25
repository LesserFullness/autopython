import pyautogui
print('press ctrl-c to quit')
try:
    while True:
        x, y = pyautogui.position() 
        positionString = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        positionString += ' RGB: (' + str(pixelColor[0]).rjust(3)
        positionString += ', ' + str(pixelColor[1]).rjust(3)
        positionString += ', ' + str(pixelColor[2]).rjust(3) + ')'
        print(positionString,end='\r')
        print('\b' * len(positionString), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone') 
pyautogui.screenshot('screenshot.png') #截图
listSub=pyautogui.locateOnScreen('D:\coding\submit.png')
print(listSub)
