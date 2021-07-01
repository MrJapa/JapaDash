import os
import tkinter as tk
import tkinter.font as font
import webbrowser
from selenium.webdriver.remote import file_detector
from selenium.webdriver.remote.command import Command
import winshell
import win32com.client
import keyboard
import time
from PIL import ImageTk
import PIL.Image
from tkinter import Canvas, PhotoImage, ttk
from tkinter import messagebox
from tkinter import Button, Tk, HORIZONTAL
from tkinter.ttk import Label
from tkinter.ttk import Progressbar
from ttkbootstrap import Style
from tkinter import *
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import selenium
from selenium.webdriver.common import keys
from selenium.webdriver.common import by
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import *
from os import path
from webout import output
os.chdir(os.path.dirname(os.path.abspath(__file__)))

options = Options()
options.headless = True
praktikurl = 'https://pms.praktikpladsen.dk/soeg-opslag/0/Data-%20og%20kommunikationsuddannelsen/Datatekniker%20med%20speciale%20i%20programmering?aftaleFilter=alle&medarbejdereFilter=alle&adresse=0a3f50ca-f5a5-32b8-e044-0003ba298018&afstand=20'

root = Tk()
bg = ImageTk.PhotoImage(file='images/background.png')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
resolution = '{}x{}'.format(screen_width,screen_height)
root.geometry(resolution)
root.state('zoomed')
root.title('JapaDash')
root.iconbitmap('')
#root.overrideredirect(1)
root.resizable(True,True)
style = Style(theme='japa')
rootcanvas = Canvas(root,border=0,highlightthickness=0)
rootcanvas.pack(fill="both",expand=YES)
rootcanvas.create_image(0,0,image=bg,anchor='nw')

logo = PhotoImage(file="images/icon.png")
logolabel = Label(rootcanvas,image=logo,bd=0,highlightthickness=0).place(x=350,y=350,anchor="center")

####!LEAGUE
Label(rootcanvas,bg='#1B2222',text="Newest game update:").place(x=500,y=425)
lolnew = 'https://euw.leagueoflegends.com/en-us/news/game-updates/'
lolnewout = output(lolnew,'//*[@id="gatsby-focus-wrapper"]/div/div[2]/div/div[1]/div/ol/li[1]/a/article/div[2]/div/h2')
lolnewresult = Label(rootcanvas,bg='#1B2222',text=output.output_result(lolnewout)).place(x=500,y=450)

Label(rootcanvas,bg='#1B2222',text="Newest League patch:").place(x=500,y=475)
lolurl = 'https://euw.leagueoflegends.com/en-us/news/tags/patch-notes'
lolout = output(lolurl,'//*[@id="gatsby-focus-wrapper"]/div/div[2]/div/div[1]/div/ol/li[1]/a/article/div[2]/div/h2')
lolresult = Label(rootcanvas,bg='#1B2222',text=output.output_result(lolout)).place(x=500,y=500)

lol = PhotoImage(file='images/lol.png')
lol_button = Button(text="",image=lol,highlightthickness=0,bd=0,command=None)
lol_canvas = rootcanvas.create_window(500,350,anchor="nw",window=lol_button)

####!TECHCOLLEGE
Label(rootcanvas,bg='#1B2222',text="Praktikpladsen:").place(x=800,y=425)
ppurl = 'https://pms.praktikpladsen.dk/soeg-opslag/0/Data-%20og%20kommunikationsuddannelsen/Datatekniker%20med%20speciale%20i%20programmering?aftaleFilter=alle&medarbejdereFilter=alle&adresse=0a3f50ca-f5a5-32b8-e044-0003ba298018&afstand=20'
praktikout = output(ppurl,'//*[@id="resultater"]/div[1]/div/p')
ppresult = Label(rootcanvas,bg='#1B2222',text=output.output_result(praktikout)).place(x=800,y=450)

techcollege = PhotoImage(file='images/techcollege.png')
techcollege_button = Button(text="",image=techcollege,highlightthickness=0,bd=0,Command=None)
techcollege_canvas = rootcanvas.create_window(800,350,anchor="nw",window=techcollege_button)

####!YOUTUBE
Label(rootcanvas,bg='#1B2222',text="Steam News Hub:").place(x=1100,y=425)
steamurl = 'https://store.steampowered.com/news/collection/featured/'
steamout = output(steamurl,'//*[@id="application_root"]/div/div/div[2]/div/div/div[2]/div/div[2]/div/a/div/div/div[1]/div[2]/div[1]/div[1]/div')
steamresult = Label(rootcanvas,bg='#1B2222',text=output.output_result(steamout)).place(x=1100,y=450)

steamout2 = output(steamurl,'//*[@id="application_root"]/div/div/div[2]/div/div/div[2]/div/div[2]/div/a/div/div/div[1]/div[2]/div[2]')
steamresult2 = Label(rootcanvas,underline=1,bg='#1B2222',text=output.output_result(steamout2)).place(x=1100,y=475)
steam = PhotoImage(file='images/steam.png')
steam_button = Button(text="",image=steam,highlightthickness=0,bd=0,Command=None)
steam_canvas = rootcanvas.create_window(1100,350,anchor="nw",window=steam_button)

root.mainloop()
