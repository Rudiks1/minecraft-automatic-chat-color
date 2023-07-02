from tkinter import *
from keyboard import is_pressed, write
from time import sleep
from threading import Thread

color = '&f' #default color

selfrun=True

def colorchange(input): #handle color change
    global color
    color = input
    text2 = Label(win, text=color, font=('Arial 10 bold')) #write out new color
    text2.grid(row=5, column=1)

def close(): #handle closing threads
    global selfrun
    selfrun=False
    main1.isDaemon = True
    main2.isDaemon = True
    win.destroy()

def gui(): #GUI
    global win
    win = Tk()
    
    win.geometry('360x160')
    win.title('MC Automatic Chat Color')
    win.resizable(False, False)

    button1 = Button(win, text='&4', width='8', height='1', bg='#AA0000', activebackground='grey', font=('Arial 12 bold'), command=lambda: colorchange('&4'))
    button1.grid(row=1, column=0)

    button2 = Button(win, text='&c', width='8', height='1', bg='#FF5555', activebackground='grey', font=('Arial 12 bold'), command=lambda: colorchange('&c'))
    button2.grid(row=1, column=1)

    button3 = Button(win, text='&6', width='8', height='1', bg='#FFAA00', activebackground='grey', font=('Arial 12 bold'), command=lambda: colorchange('&6'))
    button3.grid(row=1, column=2)

    button4 = Button(win, text='&e', width='8', height='1', bg='#FFFF55', activebackground='grey', font=('Arial 12 bold'), command=lambda: colorchange('&e'))
    button4.grid(row=1, column=3)

    button5 = Button(win, text='&2', width='8', height='1', bg='#00AA00', activebackground='grey', font=('Arial 12 bold'), command=lambda: colorchange('&2'))
    button5.grid(row=2, column=0)

    button6 = Button(win, text='&a', width='8', height='1', bg='#55FF55', activebackground='grey', font=('Arial 12 bold'), command=lambda: colorchange('&a'))
    button6.grid(row=2, column=1)

    button7 = Button(win, text='&b', width='8', height='1', bg='#55FFFF', activebackground='grey', font=('Arial 12 bold'), command=lambda: colorchange('&b'))
    button7.grid(row=2, column=2)

    button8 = Button(win, text='&3', width='8', height='1', bg='#00AAAA', activebackground='grey', font=('Arial 12 bold'), command=lambda: colorchange('&3'))
    button8.grid(row=2, column=3)

    button9 = Button(win, text='&1', width='8', height='1', bg='#0000AA', activebackground='grey', font=('Arial 12 bold'), command=lambda: colorchange('&1'))
    button9.grid(row=3, column=0)

    button10 = Button(win, text='&9', width='8', height='1', bg='#5555FF', activebackground='grey', font=('Arial 12 bold'), command=lambda: colorchange('&9'))
    button10.grid(row=3, column=1)

    button11 = Button(win, text='&d', width='8', height='1', bg='#FF55FF', activebackground='grey', font=('Arial 12 bold'), command=lambda: colorchange('&d'))
    button11.grid(row=3, column=2)

    button12 = Button(win, text='&5', width='8', height='1', bg='#AA00AA', activebackground='grey', font=('Arial 12 bold'), command=lambda: colorchange('&5'))
    button12.grid(row=3, column=3)

    button13 = Button(win, text='&f', width='8', height='1', bg='#FFFFFF', activebackground='grey', font=('Arial 12 bold'), command=lambda: colorchange('&f'))
    button13.grid(row=4, column=0)

    button14 = Button(win, text='&7', fg='white', width='8', height='1', bg='#AAAAAA', activebackground='grey', font=('Arial 12 bold'), command=lambda: colorchange('&7'))
    button14.grid(row=4, column=1)

    button15 = Button(win, text='&8', fg='white', width='8', height='1', bg='#555555', activebackground='grey', font=('Arial 12 bold'), command=lambda: colorchange('&8'))
    button15.grid(row=4, column=2)

    button16 = Button(win, text='&0', fg='white', width='8', height='1', bg='#000000', activebackground='grey', font=('Arial 12 bold'), command=lambda: colorchange('&0'))
    button16.grid(row=4, column=3)

    text1 = Label(win, text='Current color:', font=('Arial 10'))
    text1.grid(row=5, column=0)
    
    buttonclose = Button(win, text='Close', width='8', height='1', bg='#AA0000', activebackground='grey', font=('Arial 10 bold'), command=lambda: close())
    buttonclose.grid(row=5, column=3)
    
    win.mainloop()


def command(): #detect if the user types a command
    global run
    while selfrun:
        if is_pressed('shift+6'):
            run = False
            sleep(1)
        else:
            run = True
        sleep(0.05)

def main():
    pre = False
    #pre = False => the chat is closed, pre = True if the chat is opened
    while selfrun:
        if is_pressed('t') and pre == False:
            commandthread = Thread(target=command) #starting a thread for command detection
            commandthread.start()
            sleep(0.5) #time before writing the color (waiting if user types a '/')
            if run:
                write(color) #write the color
                pre = True
        if is_pressed('enter'): #only write the color again if it's a new message
            pre = False
        sleep(0.05)


main1 = Thread(target=gui)
main1.start()

main2 = Thread(target=main)
main2.start()

#Made by Rudiks