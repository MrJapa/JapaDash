import os
import tkinter as tk
from tkinter.constants import ANCHOR
import tkinter.font as font
import webbrowser
import winshell
import win32com.client
import keyboard
import time
from PIL import ImageTk
import PIL.Image
from tkinter import Canvas, PhotoImage, ttk
from tkinter import messagebox
from tkinter import Button, Tk, HORIZONTAL
from tkinter.ttk import Progressbar
from ttkbootstrap import Style
from tkinter import *
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
from selenium.webdriver.chrome.options import Options
os.chdir(os.path.dirname(os.path.abspath(__file__)))

options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
driver.get('https://pms.praktikpladsen.dk/soeg-opslag/0/Data-%20og%20kommunikationsuddannelsen/Datatekniker%20med%20speciale%20i%20programmering?aftaleFilter=alle&medarbejdereFilter=alle&adresse=0a3f50ca-f5a5-32b8-e044-0003ba298018&afstand=20')

def website():
    try:
        result = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,'//*[@id="resultater"]/div[1]/div/p')))
        print(result.text)
        if path.exists("praktikpladsen.png"):
            pass
        else:
            all_ = driver.find_element_by_xpath('//*[@id="resultater"]')
            location = all_.location
            size = all_.size
            driver.save_screenshot('praktikpladsen.png')
        posts = '0 stillingsopslag og 35 godkendte virksomheder'
        if result != posts:
            all_ = driver.find_element_by_xpath('//*[@id="resultater"]')
            location = all_.location
            size = all_.size
            driver.save_screenshot('praktikpladsen.png')
        else:
            pass
    except:
        pass
    driver.quit()

def output_result():
    try:
        global result
        result = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,'//*[@id="resultater"]/div[1]/div/p')))
        result = result.text
        print(result)
        driver.quit()
    except:
        pass
    driver.quit()

root = Tk()
bg = ImageTk.PhotoImage(file='images/background.png')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
resolution = '{}x{}'.format(screen_width,screen_height)
print(resolution)
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
logolabel = Label(rootcanvas,image=logo,bd=0,highlightthickness=0).place(x=550,y=350,anchor="center")

ppresult = Label(rootcanvas,text=result).place(x=700,y=400)

#root.bind("<Configure>", resize_bg)
root.mainloop()