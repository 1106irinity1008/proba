from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

wiwdow = Tk()
wiwdow.title('Напоминание')
label = Label(text='Установите напоминание')
label.pack(pady=10)
set_button = Button(text='Установить напоминание')
set_button.pack()

wiwdow.mainloop()
