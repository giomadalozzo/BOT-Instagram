from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from secrets_instagram import username, password

import time
import random
import os
import datetime

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
        for x in range(1,4):
            for y in range(1,4):
                post=driver.browser.find_elements_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[{}]/div[{}]/a/div[1]".format(x,y))
                if len(post)!=0:
                    post[0].click()

                    time.sleep(5)

                    like_button=driver.browser.find_elements_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button")

                    if len(like_button) != 0:
                        like_button[0].click()

                    """AQUI VAI ENTRAR ANÁLISE SE ATINGIU LIMITE LIKES"""

                    time.sleep(5)

                    close = driver.browser.find_elements_by_xpath("/html/body/div[4]/div[3]/button")
                    if len(close) == 0:
                        close = driver.browser.find_elements_by_xpath("/html/body/div[3]/div[3]/button")
                    close[0].click()

                    time.sleep(5)



        return count+1


                
#fazer método que entra na pag da hashtag, outro que curte tudo na pagina e um que fica vendo em ql item da lista ta
    
#problema: os full path tão mudando!!!!
    


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




    


'''account = AccountInstagram(username,password)

dir = os.path.dirname(os.path.realpath(__file__))
path = dir+"/chromedriver.exe"
br=webdriver.Chrome(executable_path=path)
br.get('https://www.instagram.com/accounts/login/')
time.sleep(5)
br.find_element_by_name('username').send_keys(account.user)
br.find_element_by_name('password').send_keys(account.pwd,Keys.ENTER)
time.sleep(5)

main_list=GetHashtags.update_file()
count=0
br.get('https://www.instagram.com')
time.sleep(3)
if "Turn on" in br.page_source:
    x=br.find_element_by_class_name('mt3GC')
    a=x.find_elements_by_tag_name('button')
    a[1].click()
    time.sleep(2)
count=0
lul2=1
xyz=2
warn = 0
while xyz==2:
    lul=0
    while lul>51 or lul2==1:
        for i in range(count,len(main_list)):
            tag=(str(main_list[i]))
            a=tag.strip()
            tag=a.lower()
            a=tag.replace(' ','')
            tag=a.replace('\n','')
            a=tag.replace('\t','')


            br.get('https://www.instagram.com/explore/tags/'+a)
            time.sleep(3)
            for w in range(1,4):
                for z in range(1,4):
                    link=br.find_elements_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[{}]/div[{}]/a/div[1]".format(w,z))

                    link[0].click()
                    time.sleep(3)
                    find=br.find_elements_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button")
                    find[0].click()
                    time.sleep(2)
                    if br.find_elements_by_xpath("/html/body/div[5]/div/div/div[2]/button[2]") != []:
                        find=br.find_elements_by_xpath("/html/body/div[5]/div/div/div[2]/button[2]")
                        find[0].click()
                        time.sleep(2)
                        warn = 5
                        find=br.find_elements_by_xpath("/html/body/div[4]/div[3]/button")
                        ue=1
                        while ue==1:
                            if len(find)==0:
                                find=br.find_elements_by_xpath("/html/body/div[4]/div[3]/button")
                            else:
                                ue=2
                        find[0].click()
                        break
                    else:
                        find=br.find_elements_by_xpath("/html/body/div[4]/div[3]/button")
                        ue=1
                        while ue==1:
                            if len(find)==0:
                                find=br.find_elements_by_xpath("/html/body/div[4]/div[3]/button")
                            else:
                                ue=2
                        find[0].click()
                        time.sleep(2)

                        lul=lul+1
                        count=count+1
                if warn==5:
                    break
            if warn==5:
                break
        if warn==5:
                break
    print("Deu limite em: {} com count {} Esperando 40min.".format(datetime.datetime.now(), count))
    time.sleep(2400)




#17:12'''




