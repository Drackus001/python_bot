from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        print('email:', email)
        print('password:', password)
        print('cleared login feilds')
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

        print('sending request for login...')
        time.sleep(3)

    def like_tweet(self, hastag):
        bot = self.bot
        time.sleep(3)
        bot.get('https://twitter.com/search?q='+hastag+'&src=typed_query')
        print('searching for ', hastag, '...')

        time.sleep(3)
        scroll = 300
        for i in range(0, 5):
            time.sleep(3)

            # bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            with open('jquery.js', 'r') as jquery_js:
                jquery = jquery_js.read()  # read the jquery from a file
                bot.execute_script(jquery)  # active the jquery lib
                print('Scrolling...')
                script = "$(document).ready(function(){$('body, html').animate({scrollTop: "+str(
                    scroll)+"}, 800)})"
                bot.execute_script(script)
                scroll += 500
                        
            
            tweets = bot.find_elements_by_class_name('tweet')
            #print(tweets)
            links = [elem.get_attribute('data-permalink-path')
                     for elem in tweets]
            
            for link in links:
                bot.get('https://twitter.com'+link)
                print(link +' visiting...')
                try:
                    bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(5)
                except Exception as ex:
                    time.sleep(60)
            
            
            
            # dynamic code stays here...

            # Tweet
            # css-4rbku5 css-18t94o4 css-901oao r-1re7ezh r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0
            # css-4rbku5 css-18t94o4 css-901oao r-1re7ezh r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0
            # r-1q142lx
            # Heart
            # css-1dbjc4n r-sdzlij r-1p0dtai r-xoduu5 r-1d2f490 r-xf4iuw r-u8s1d r-zchlnj r-ipm5af r-o7ynqc r-6416eg
            # r-xf4iuw

            # css-18t94o4 css-1dbjc4n r-1777fci r-11cpok1 r-1ny4l3l r-bztko3 r-lrvibr
            # r-bztko3
            
            #tweets = bot.find_elements_by_xpath("//div[@class='css-4rbku5 css-18t94o4 css-901oao r-1re7ezh r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0']")
            
            tweets = bot.find_elements_by_class_name('r-1q142lx')           
            print(tweets)
            
            links = [elem.get_attribute('href')
                    for elem in tweets]
            print(links)
            for link in links:
                if(link != None):
                    bot.get(link)
                    print(link + ' visiting...')
                    try:
                        clickable = bot.find_elements_by_class_name('r-bztko3')
                        arr_clickable = [elem.get_attribute('data-testid')
                                    for elem in clickable]
                        for x in arr_clickable:
                            if(x == 'like'):
                                print('liked...')
                                #bot.find_element_by_class_name('css-18t94o4 css-1dbjc4n r-1777fci r-11cpok1 r-1ny4l3l r-bztko3 r-lrvibr').click()
                        time.sleep(5)
                    except Exception as ex:
                        time.sleep(60)


            
                      

            


user = TwitterBot('username', 'password')
user.login()
user.like_tweet('automation')
#user.like_tweet('helloworld')
