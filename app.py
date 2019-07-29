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
        bot.get('https://twitter.com/search?q='+hastag+'&src=typed_query')
        print('searching for ', hastag, '...')

        
        time.sleep(3)
        scroll = 300
        for i in range(1, 10):
            time.sleep(5)
            
            # bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            with open('jquery.js', 'r') as jquery_js:
                jquery = jquery_js.read()  # read the jquery from a file
                bot.execute_script(jquery)  # active the jquery lib
                print('Scrolling...')
                script = "$(document).ready(function(){$('body, html').animate({scrollTop: "+str(scroll)+"}, 800)})"
                bot.execute_script(script)
                scroll += 500
            #bot.execute_script(
            #"$(document).ready(function(){$('body, html').animate({scrollTop: 156}, 800)})")
            
            #tweets = bot.find_element_by_class_name('r-1udh08x')
            #Xpath= "//div[@class='css-1dbjc4n r-1udh08x r-utggzx']"
            # css-1dbjc4n r-18u37iz r-thb0q2
            # tweets=bot.find_elements_by_class_name(
            #    'css-1dbjc4n r-18u37iz r-thb0q2')
            # print(tweets.__getattribute__('href'))
            # tweets.send_keys(Keys.RETURN)
            #tweets2 = bot.find_elements_by_xpath("//div[@class='css-1dbjc4n r-18u37iz r-thb0q2']")
            # tweets.send
            # new WebDriverWait(bot, 20).until(ExpectedConditions.elementToBeClickable(By.xpath("//div[contains(@class, 'css-1dbjc4n r-1udh08x r-utggzx')]"))).click();
            #xyz = bot.find_elements_by_css_selector("div[class$='css-1dbjc4n r-1udh08x r-utggzx']")
            # new WebDriverWait(bot, 20).until(ExpectedConditions.elementToBeClickable(By.cssSelector("div[class$='css-1dbjc4n r-1udh08x r-utggzx'][data-testid='tweet']"))).click();
            # print(xyz.count)

            # href="/TwistaTim/status/1155545324846403584
            # css-4rbku5 css-18t94o4 css-901oao r-1re7ezh r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0
            # __getattribute__('href')
            # links=[elem
            #         for elem in tweets]
            # print(links)
            # for x in xyz:
            #     print(x.value)
            #     print(x.sep)

            #xxx = bot.find_elements_by_class_name("div[class$='css-18t94o4 css-1dbjc4n r-1777fci r-11cpok1 r-1ny4l3l r-bztko3 r-lrvibr'][data-testid='like']")

            # time.sleep(2)
            # for link in links:
            #    bot.get('https://twitter.com' + link)
            #    try:
            #        bot.find_element_by_class_name('css-ldbjc4n').click()
            #        time.sleep(7)
            #    except Exception as ex:
            #        time.sleep(60)


satyam = TwitterBot('username', 'password')
satyam.login()
# satyam.like_tweet('automation')
satyam.like_tweet('helloworld')
