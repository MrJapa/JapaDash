import os
import threading
import tkinter as tk
import tkinter.font as font
import webbrowser
from selenium.webdriver.remote import file_detector
from selenium.webdriver.remote.command import Command
from tkvideo.tkvideo import tkvideo
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
from os import path, terminal_size
from webout import output
import threading
from tooltip import CreateToolTip
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
root.iconbitmap('images/icon.ico')
#root.overrideredirect(1)
root.resizable(True,True)
style = Style(theme='japa')
rootcanvas = Canvas(root,border=0,highlightthickness=0)
rootcanvas.pack(fill="both",expand=YES)
rootcanvas.create_image(0,0,image=bg,anchor='nw')

logo = PhotoImage(file="images/icon.png")
logolabel = Label(rootcanvas,image=logo,bd=0,highlightthickness=0).place(x=350,y=350,anchor="center")

def loloption():
    global loloptions
    loloptions = Toplevel()
    loloptions.geometry("450x350+710+290")
    loloptions.title('LoL Options')
    loloptions.iconbitmap('images/icon.ico')
    style = Style(theme='japa')
    loloptions.overrideredirect(1)

    loloptionsbg = PhotoImage(file='images/small.png')
    loloptionlabel = Label(loloptions, image=loloptionsbg)
    loloptionlabel.place(x=0,y=0)

    exitimg = PhotoImage(file="images/exit.png")

    exit_button = ttk.Button(loloptions, text="Exit",command=exits)
    exit_button.pack(expand=False,pady=25)


    loloptions.mainloop()
####!LEAGUE
def league():
    lolnew = 'https://euw.leagueoflegends.com/en-us/news/game-updates/'
    lolnewout = output(lolnew,'//*[@id="gatsby-focus-wrapper"]/div/div[2]/div/div[1]/div/ol/li[1]/a/article/div[2]/div/h2')
    lolnewresult = Label(rootcanvas,bg='#1B2222',text=output.output_result(lolnewout)).place(x=500,y=450)

    lolurl = 'https://euw.leagueoflegends.com/en-us/news/tags/patch-notes'
    lolout = output(lolurl,'//*[@id="gatsby-focus-wrapper"]/div/div[2]/div/div[1]/div/ol/li[1]/a/article/div[2]/div/h2')
    lolresult = Label(rootcanvas,bg='#1B2222',text=output.output_result(lolout)).place(x=500,y=500)

Label(rootcanvas,bg='#1B2222',text="Latest game update:").place(x=500,y=425)
Label(rootcanvas,bg='#1B2222',text="Latest League patch:").place(x=500,y=475)
lol = PhotoImage(file='images/lol.png')
lol_button = Button(text="",image=lol,highlightthickness=0,bd=0,command=loloption)
lol_canvas = rootcanvas.create_window(500,350,anchor="nw",window=lol_button)
####!TECHCOLLEGE
def techcollege():
    ppurl = 'https://pms.praktikpladsen.dk/soeg-opslag/0/Data-%20og%20kommunikationsuddannelsen/Datatekniker%20med%20speciale%20i%20programmering?aftaleFilter=alle&medarbejdereFilter=alle&adresse=0a3f50ca-f5a5-32b8-e044-0003ba298018&afstand=20'
    praktikout = output(ppurl,'//*[@id="resultater"]/div[1]/div/p')
    ppresult = Label(rootcanvas,bg='#1B2222',text=output.output_result(praktikout)).place(x=800,y=450)

Label(rootcanvas,bg='#1B2222',text="Praktikpladsen:").place(x=800,y=425)
techcollegeimg = PhotoImage(file='images/techcollege.png')
techcollege_button = Button(text="",image=techcollegeimg,highlightthickness=0,bd=0,command=None)
techcollege_canvas = rootcanvas.create_window(800,350,anchor="nw",window=techcollege_button)
####!NYHEDER
def nyheder():
    covidurl = 'https://nyheder.tv2.dk/samfund/dagens-coronatal-overblik-over-smittede-indlagte-og-doede'
    covidout = output(covidurl,'//*[@id="main"]/article/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr[1]/th[1]')
    covidresult = Label(rootcanvas,bg='#1B2222',text=output.output_result(covidout)).place(x=800,y=700)

Label(rootcanvas,bg='#1B2222',text="Dagens coronatal:").place(x=800,y=675)
covid = PhotoImage(file="images/covid.png")
covid_button = Button(text="",image=covid,highlightthickness=0,bd=0,Command=None)
covid_canvas = rootcanvas.create_window(800,600,anchor="nw",window=covid_button)

def opgg():
    opggurl = 'https://euw.op.gg/summoner/userName=S%CE%B9vas'
    opggout = output(opggurl, '//*[@id="SummonerLayoutContent"]/div[2]/div[1]/div[1]/div/div[2]')
    opggresult = Label(rootcanvas,bg='#1B2222',text=output.output_result(opggout)).place(x=500,y=700)

Label(rootcanvas,bg='#1B2222',text="OP.GG Stats:").place(x=500,y=675)
opggimg = PhotoImage(file="images/opgg.png")
opgg_button = Button(text="",image=opggimg,highlightthickness=0,bd=0,Command=None)
opgg_canvas = rootcanvas.create_window(500,600,anchor="nw",window=opgg_button)

def github():
    git = 'https://github.com/MrJapa'
    gitrepoout = output(git, '//*[@id="js-pjax-container"]/div[1]/div/div/div[2]/div/nav/a[2]')
    gitreporesult = Label(rootcanvas,bg="#1B2222",text=output.output_result(gitrepoout)).place(x=1100,y=450)

    gitconout = output(git, '//*[@id="js-pjax-container"]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/h2')
    gitconresult = Label(rootcanvas,bg="#1B2222",text=output.output_result(gitconout)).place(x=1100,y=475)
    
    gitactout = output(git, '//*[@id="js-contribution-activity"]/div[2]/div/div')
    gitactresult = Label(rootcanvas,bg="#1B2222",text=output.output_result(gitactout)).place(x=1100,y=500)

Label(rootcanvas,bg="#1B2222",text="Info:").place(x=1100,y=425)
gitimg = PhotoImage(file="images/github.png")
git_button = Button(text="",image=gitimg,highlightthickness=0,bd=0,command=None)
git_canvas = rootcanvas.create_window(1100,350,anchor="nw",window=git_button)

def threads():
    p1 = threading.Thread(target=league)
    p1.setDaemon(True)
    p2 = threading.Thread(target=techcollege)
    p2.setDaemon(True)
    p3 = threading.Thread(target=opgg)
    p3.setDaemon(True)
    p4 = threading.Thread(target=nyheder)
    p4.setDaemon(True)
    p5 = threading.Thread(target=github)
    p5.setDaemon(True)
    p1.start();p2.start();p3.start();p4.start();p5.start()

def exits():
    loloptions.destroy()

if __name__=='__main__':
    threads()
    root.mainloop()