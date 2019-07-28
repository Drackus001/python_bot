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
        print('cleared login feilds')
        email.send_keys(self.username)  
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        print('sending request for login...')
        time.sleep(3)

    def like_tweet(self, hastag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hastag+'&src=typed_query')
        print('searching for ',hastag,'...')


        time.sleep(3)
        for i in range(1, 4):
            time.sleep(5)
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            print('Scrolling...')
            #tweets = bot.find_element_by_class_name('r-1udh08x')
            #Xpath= "//div[@class='css-1dbjc4n r-1udh08x r-utggzx']"
            #tweets = bot.find_elements_by_xpath("//div[@class='css-1dbjc4n r-1udh08x r-utggzx']")
            #new WebDriverWait(bot, 20).until(ExpectedConditions.elementToBeClickable(By.xpath("//div[contains(@class, 'css-1dbjc4n r-1udh08x r-utggzx')]"))).click();
            #xyz = bot.find_elements_by_css_selector("div[class$='css-1dbjc4n r-1udh08x r-utggzx']")
            #new WebDriverWait(bot, 20).until(ExpectedConditions.elementToBeClickable(By.cssSelector("div[class$='css-1dbjc4n r-1udh08x r-utggzx'][data-testid='tweet']"))).click();
            #print(xyz.count)
            
            
            # links = [elem.get_attribute('data-permalink-path')
            #            for elem in xyz]
            # print(links)
            # for x in xyz:
            #     print(x.value)
            #     print(x.sep)
                
            #xxx = bot.find_elements_by_class_name("div[class$='css-18t94o4 css-1dbjc4n r-1777fci r-11cpok1 r-1ny4l3l r-bztko3 r-lrvibr'][data-testid='like']")
            
            #time.sleep(2)
            #for link in links:
            #    bot.get('https://twitter.com' + link)
            #    try:
            #        bot.find_element_by_class_name('css-ldbjc4n').click()
            #        time.sleep(7)
            #    except Exception as ex:
            #        time.sleep(60)

satyam = TwitterBot('username', 'password')
satyam.login()
satyam.like_tweet('automation')