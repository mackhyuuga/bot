"""from selenium import webdriver
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
"""






from selenium import webdriver
from time import sleep
import log

class bot:
    def __init__(self):
        self.driver_path = '/home/mack/Documents/code/bot/geckodriver'
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument('user-data-dir=Perfil')
        self.browser = webdriver.Firefox(
            executable_path=self.driver_path,
            options = self.options
        )       

    def access(self, site):
        self.browser.get(site)
        sleep(5)

    def sign_in(self):
        try:

            buttons = [ '/html/body/div[1]/div/div[2]/div/div/div[1]/button',
                        '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button',
                        '/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[1]/div/button',
                        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]',
                        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input',
                        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]',
                        '/html/body/div[2]/div/div/div/div/div[3]/button[1]/span',
                        '/html/body/div[2]/div/div/div/div/div[3]/button[2]/span',
            ]
            
            self.browser.find_element_by_xpath(buttons[0]).click()
            sleep(1)

            self.browser.find_element_by_xpath(buttons[1]).click()
            sleep(3)

            self.browser.find_element_by_xpath(buttons[2]).click()
            sleep(3)

            self.browser.switch_to_window(self.browser.window_handles[1])

            input_login = self.browser.find_element_by_id('identifierId')
            input_login.send_keys(log.E)
            
            button = self.browser.find_element_by_xpath(buttons[3])
            sleep(1)
            button.click()
            sleep(3)

            input_password = self.browser.find_element_by_xpath(buttons[4])
            input_password.send_keys(log.P)

            button = self.browser.find_element_by_xpath(buttons[5])
            sleep(1)
            button.click()
            sleep(7)

            self.browser.switch_to_window(self.browser.window_handles[0])

            '''self.browser.find_element_by_xpath(buttons[6]).click()
            sleep(3)

            self.browser.find_element_by_xpath(buttons[7]).click()
            sleep(1)'''

            sleep(10)


        except Exception as e:
            print('error signing in')

    def like(self, n = 1000):
        for i in range(n):
            try:
                self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button/span').click()
                sleep(0.5)
            except Exception as error:
                print("the following error occurred: ", error)
                sleep(10)

    def send_messagem(self, n = 100):
        for i in range(n):
            try:
                self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/aside/nav/div/div/div/div[2]/div[1]/div[1]/div[1]/a/div[1]/div').click
                sleep(2)
                messagem = self.browser.find_element_by_xpath('//*[@id="chat-text-area"]')
                messagem.send_keys('ola')
                sleep(1)
                self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button[2]/span').click
            except Exception as error:
                print("the following error occurred: ", error)
        

    def exit(self):
        self.browser.quit()


if __name__ == '__main__':
    tinder = bot()
    tinder.access('https://tinder.com/?lang=pt')
    tinder.sign_in()
    #tinder.like()
    #tinder.send_messagem()


"""sleep(10)
browser.exit()"""
