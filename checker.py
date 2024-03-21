import pyautogui

while True:
    pos = pyautogui.position()
    image = pyautogui.screenshot(region=(600,600,1000,1000))
    
    color = image.getpixel((pos.x, pos.y))

    print("Pos: {} Color: {}".format(pos, color))