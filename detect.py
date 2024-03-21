import pyautogui
import time 

def color_match(pixel_color):
    #print(type(pixel_color))
          
    colors = [
        (200,28,25),
        (206,29,25),
        (219,42,22),
        (215,42,12),
        (221,45,19),
        (222,38,15),
    ]
    if pixel_color in colors:
        return True
    return False

def check():
    img = pyautogui.screenshot(region=(600,600,1000,1000))
    for x in range(img.width): 
        for y in range(img.height): 
            #print(img.getpixel((x, y)))
            if color_match(img.getpixel((x, y))):
                print("Found")
                return True
    return False

def find_icon():
    button_locations = pyautogui.locateAllOnScreen(
        image="data/icons/ic_fish.png", 
        grayscale=True, 
        region=(0,0,1920,1080), 
        confidence=0.65) 
    
    for button in button_locations:
        print(button)
        pyautogui.click(button.x+50, button.y+50)
        


if __name__ == "__main__":
    
    #button = find_icon()
    #pyautogui.click(button.left+50, button.top+50)
    while True:
        find_icon()
        time.sleep(0.5)