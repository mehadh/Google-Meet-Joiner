import pyautogui
import time
import os

class Numbers:      # This class is for the numbers to have their respective positions.
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y

grayX = 1457    # Gray part of any of the numbers on the keypad. We use this to see whether or not the script has cracked the passcode on that run.
grayY = 932     # Originally I picked the key 1, I've now realized you should probably use the BACKSPACE key as it won't trigger an unintended input.

def success(): # This is our function to check whether or not it was a success. 
    pyautogui.moveTo(grayX, grayY)                  #68, 74, 79 or 0, 79, 164
    pyautogui.click()                               # [(1, (68, 74, 79))] {X=1457,Y=932,Width=427,Height=410}
    time.sleep(1)
    checker = pyautogui.screenshot(
        region = (
            grayX, grayY, 1, 1
        )
    )
    color = checker.getcolors()
    if (color == [(1, (68, 74, 79))]): # This might need to be changed but probably not.
        return False
    else:
        return True

# All definitions of coords were done with the phonesize at 100 on a 1920x1080 monitor running in Windowed mode with a border.
# You can use a tool like BreakthruSoftware's coord finder for reconfiguring.

one = Numbers(1, 1425, 660)
two = Numbers(2, 1516, 660)
three = Numbers(3, 1623, 660)
four = Numbers(4, 1425, 753)
five = Numbers(5, 1516, 753)
six = Numbers(6, 1623, 753)
seven = Numbers(7, 1425, 845)
eight = Numbers(8, 1516, 845)
nine = Numbers(9, 1623, 845)
zero = Numbers(0, 1513, 926)

def converter(number):  # This converter function is a crude way for us to get the positions from above, you'll understand more below.
    dictionary = {'1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six",
            '7': "seven", '8': "eight", '9': "nine", '0': "zero"}
    return " ".join(map(lambda x: dictionary[x], str(number)))

def input(number): # Give this function a number object (from the class defined above) and it will move and click.
    time.sleep(0.5)
    pyautogui.moveTo(number.x, number.y)
    pyautogui.click()

def main():
    for i in range(9999): # From 0000-9999 (all possible PIN codes)
        pin = str(i).zfill(4) # If we picked 1 for example, this will turn it into 0001
        print(pin)
        for i in range(4): # Entering each digit in manually
            numStr = converter(pin[i]) # Get the word form of the number we are converting
            input(eval(numStr)) # Input function to move and click, eval is used to refer to that number string as the actual object itself.
            if (i == 3): # 3 would be the last digit in the PIN code.
                if success():
                    print(pin+" is the pin.")
                    os.system('pause')
                    exit()



main()