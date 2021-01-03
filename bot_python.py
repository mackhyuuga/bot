from selenium import webdriver
from time import sleep

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'/home/mack/Documents/code/bot/chromedriver')

    def login(self):
        self.driver.get('https://tinder.com/?lang=pt')

        sleep(40)
        
        while True:
            sleep(0.5)
            try:
                like = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
                like.click()
            except Exception as error:
                print("the following error occurred: ", error)
                sleep(30)
    
bot = TinderBot()
bot.login()
