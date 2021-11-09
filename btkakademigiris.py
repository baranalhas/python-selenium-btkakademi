from selenium import webdriver
from selenium.webdriver.common.by import By
import time

username = ''
password = ''


class btkAkademi:
    def __init__(self,username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome()

    def btkAkademiGiris(self):

        self.browser.get("https://1milyonistihdam.hmb.gov.tr/ozgecmis/login?type=btk")
        self.browser.maximize_window()
        time.sleep(2)


        usernameInput = self.browser.find_element(By.XPATH,"//*[@id='identification']")
        passwordInput = self.browser.find_element(By.XPATH,"//*[@id='password']")
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        self.browser.find_element(By.XPATH,"//*[@id='loginform']/button").click()
        print('1Milyonİstihdam Giriş Başarılı')
        time.sleep(3)
        self.browser.find_element(By.CLASS_NAME,'btn.btn-outline-info.px-4').click()
        print('BTK-Akademi Girişi Başarılı !')
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/div/div/ul/li[1]/a").click()
        print('Giriş başarılı.')
        while True:
            a = int(input('1-Tekrar Gir\n2-Çık ;)'))
            if a == 1:
                self.browser.get("https://1milyonistihdam.hmb.gov.tr/ozgecmis/")
                self.browser.maximize_window()
                time.sleep(3)
                self.browser.find_element(By.CLASS_NAME,'btn.btn-outline-info.px-4').click()
                time.sleep(3)
                self.browser.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/div/div/ul/li[1]/a").click()
                print('Giriş başarılı.')
            if a == 2:
                self.browser.close()
                exit(0)
                

btk = btkAkademi(username, password)
btk.btkAkademiGiris()



