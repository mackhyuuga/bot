from selenium import webdriver
from time import sleep

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')

    def login(self):
        self.driver.get('https://tinder.com/?lang=pt')

        sleep(60)
        
        for i in range(1, 10000):
            sleep(0.5)
            like = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
            like.click()
    
bot = TinderBot()
bot.login()
