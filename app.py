from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(2)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)  
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)

    def like_tweet(self, hastag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hastag+'&src=typed_query')
        time.sleep(2)
satyam = TwitterBot('username', 'password')
satyam.login()
satyam.like_tweet('webscrapling')