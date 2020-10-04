from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from secrets_instagram import username, password

import time
import random
import os
import datetime as datetime

class GetHashtags:

    def update_file():
        path = os.path.dirname(os.path.realpath(__file__))+"/hashtags.txt"
        with open(path) as f:
            hashtags_list = f.read().splitlines()

        return hashtags_list

class AccountInstagram:
    
    def __init__(self, username, password):
        self.user=username
        self.pwd=password

class WebDriver:

    def __init__(self, path_dir):
        self.path = path_dir + "/chromedriver.exe"

    def start_browser(self):
        browser_on = webdriver.Chrome(executable_path = self.path)
        self.browser = browser_on

    

class NavigationInstagram:

    def check_popup_notification(driver):
        if "Agora não"  or "notifications" in driver.browser.page_source:
            find_class=driver.browser.find_element_by_class_name('mt3GC')
            button=find_class.find_elements_by_tag_name('button')
            button[1].click()

            time.sleep(5)

    def login(driver, username, password):
        driver.browser.get('https://www.instagram.com/accounts/login/')

        time.sleep(5)     # Will be used a 5 seconds delay to let your internet connection update the website. You can change to another delay length if you want.

        driver.browser.find_element_by_name('username').send_keys(username)
        driver.browser.find_element_by_name('password').send_keys(password, Keys.ENTER)

        time.sleep(5)

        driver.browser.get('https://www.instagram.com')

        time.sleep(5)

    def hashtag_page(driver, hashtags_list, line=0):
        hashtag = (str(hashtags_list[line])).strip().lower().replace(' ', '')\
        .replace('\n','').replace('\t','')
        driver.browser.get('https://www.instagram.com/explore/tags/' + hashtag)

        time.sleep(5)

        return line

    def like_post(driver, count):
        keyboard_commands = Keys.TAB

        for x in range(0,12):
            driver.browser.find_elements_by_xpath('//button[text()="Seguir" or "Follow"]')[0].send_keys("webdriver" + keyboard_commands + Keys.ENTER)

            time.sleep(2)

            keyboard_commands = keyboard_commands + Keys.TAB
            
            if len(driver.browser.find_elements_by_css_selector("[aria-label='Curtir']")) == 0:
                if len(driver.browser.find_elements_by_css_selector("[aria-label='Like']")) > 0:
                    driver.browser.find_elements_by_css_selector("[aria-label='Like']")[0].click()
            else:
                driver.browser.find_elements_by_css_selector("[aria-label='Curtir']")[0].click()

            time.sleep(2)

            driver.browser.find_elements_by_xpath('/html')[0].send_keys("webdriver" + Keys.ESCAPE)

            time.sleep(5)
            
        return count+1
    


if __name__ == '__main__':

    hashtags_list = GetHashtags.update_file()

    account = AccountInstagram(username, password)

    driver_path = os.path.dirname(os.path.realpath(__file__))
    chrome = WebDriver(driver_path)

    chrome.start_browser()

    NavigationInstagram.login(chrome, account.user, account.pwd)

    NavigationInstagram.check_popup_notification(chrome)

    line = 0     #Line of the hashtags file that will be the first tag searched on Instagram. You can change here for whatever line you would like to start (PS: FIRST LINE STARTS ON ZERO)
    
    for i in range(line, len(hashtags_list)):
        count = NavigationInstagram.hashtag_page(chrome, hashtags_list, line)
        line = NavigationInstagram.like_post(chrome, count)

        if count % 6 == 0:                                                      #Here's added a 15 minute timeout after every 72 likes to avoid the account getting blocked for spam.
            current_time = datetime.datetime.now()
            timeout_ammount = 900                                               #You can change here the ammount of timeout. DO IT AT YOUR OWN RISK.
            time_delta = datetime.timedelta(seconds=timeout_ammount)
            restart_time = (current_time + time_delta).strftime("%H:%M:%S")
            print("Waiting 15 minutes to not block the account activity. Bot will be up again at {}".format(restart_time))
            time.sleep(timeout_ammount)



