from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
import keyboard
from datetime import datetime
import csv

#to open a chrome broswer and go to the given link
class zoom_bot:

    def join(self,meeting_link):
        self.bot = webdriver.Chrome("chromedriver.exe")
        self.bot.get(meeting_link)
        time.sleep(10)
        keyboard.send("tab",do_press=True,do_release=True)
        keyboard.send("tab",do_press=True,do_release=True)
        keyboard.send("enter",do_press=True,do_release=True)

        time.sleep(10)

        self.bot.quit()

#An instance of the zoom_bot class
bot = zoom_bot()

#To open the csv file and make it into a list
meeting_data = csv.reader(open('Meeting_link.csv'))
data_lines = list(meeting_data)

#To go to the scheduled meeting
for i in data_lines:
    while True:
        if datetime.now().hour == int(i[0].split(':')[0]) and datetime.now().minute == int(i[0].split(':')[1]):
            bot.join(i[1])
            
