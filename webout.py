from logging import root
import os
import tkinter as tk
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
os.chdir(os.path.dirname(os.path.abspath(__file__)))
options = Options()
options.headless = True

class output():
    def __init__(self,website,result):
        self.website = website
        self.result = result
        
    def output_result(self):
        driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
        driver.get(self.website)
        try:
            result = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,self.result)))
            result = result.text
            driver.quit()
            return result
        except:
            print("fail")
            pass
        driver.quit()

