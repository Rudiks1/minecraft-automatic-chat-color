import keyboard
from time import sleep
from threading import Thread

color = str(input('Write here the color you want to use (Example: &e): '))  #color code

if color == "":  #color code validation
    print('Invalid color! Start again and choose a valid color!')

def command():  #detect if the user types a command
    global run
    while True:
        if keyboard.is_pressed("shift+6"):
            run = False
            sleep(1)
        else:
            run = True
        sleep(0.05)

def main():
    pre = False
    #pre = False => the chat is closed, pre = True if the chat is opened
    while True:
        if keyboard.is_pressed("t") and pre == False:
            t1 = Thread(target=command)  #starting a thread for command detection
            t1.start()
            sleep(0.5)  #time before writing the color (waiting if user types a "/")
            if run:
                keyboard.write(color)  #write the color
                pre = True
        if keyboard.is_pressed("enter"):  #only write the color again if it's a new message
            pre = False
        sleep(0.05)

main()
