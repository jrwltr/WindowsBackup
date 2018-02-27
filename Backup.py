import os
from subprocess import call
from tkinter import *
from tkinter import font

Buttons = []

win=Tk()
win.winfo_toplevel().title("Backup")
win.attributes("-toolwindow",1) # removes minimize/maximize buttons

font.nametofont('TkDefaultFont').configure(size=16)

def BackupFunction(BackupDirectory):
    def Backup():
        for B in Buttons:
            B.config(state='disabled')
        TextBox.insert(END, 
                       os.popen("robocopy.exe " + 
                                "c:\\data" + BackupDirectory + 
                                " " + 
                                "\\\\NetGearUSB\\USB_Storage\\LapTopBackUp" + BackupDirectory +
                                " /MIR /NP /NJH /DST /FFT").read()
                      )
        for B in Buttons:
            B.config(state='active')
    return Backup

def NewButton(ButtonText, ButtonCommand, Row, Column, ColumnSpan):
    B = Button(win,text=ButtonText,command=ButtonCommand)
    B.grid(row=Row,column=Column,columnspan=ColumnSpan,sticky=E+W,padx=5,pady=5)
    Buttons.append(B)

NewButton("All",       BackupFunction(""                ), 0, 0, 2)
NewButton("Pictures",  BackupFunction("\\Pictures"      ), 1, 0, 1)
NewButton("Finance",   BackupFunction("\\jrw\\Finance"  ), 1, 1, 1)
NewButton("Quicken",   BackupFunction("\\q"             ), 2, 0, 1)
NewButton("Passwords", BackupFunction("\\jrw\\Passwords"), 2, 1, 1)

SBar = Scrollbar(win)
TextBox = Text(win, height=20, width=80)
SBar.config(command=TextBox.yview)
TextBox.config(yscrollcommand=SBar.set)
SBar.grid(row=3,column=1,sticky=N+S+E+W)
TextBox.grid(row=3,column=0,columnspan=2,sticky=E+W,padx=5,pady=5)

win.mainloop()

