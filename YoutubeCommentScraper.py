from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import pandas as pd
import time
import random

#Setting the global random seed
random.seed = 55

#Func to take the clean the string and only leave the numeric characters
def cleanComz(inpString):
    a = inpString.replace(' Comments','')
    a = a.replace(',','')
    return a

def checkEnoughComz(number):
    if(number <= 59):
        return 4
    else:
        return number/20

CommenteeNameList, TotLikesList, TimeAgoList =  [],[],[]
CommentFullList =[]

webURL = 'https://www.youtube.com/watch?v=rqeCzp4c1Zg'
try:
    #Using Firefox as the browser is recommended.
    driver = webdriver.Firefox(executable_path = r'C:\Program Files\Selenium Drivers 64\geckodriver.exe')
    driver.maximize_window()
    driver.get(webURL)
    print('Opening browser\n')

    #Ideally a quicker code will check for length of the page and compare it with the length before the scroll (and keep this as loop condition for scrolling). Work in progress...
    # for i in range(20):
    #     ele = driver.find_element_by_tag_name('body')
    #     ele.send_keys(Keys.END)
    #     time.sleep(1)
    # oldlen = driver.get_window_size()
    # while oldlen != newlen:
    #     ele = driver.find_element_by_tag_name('body')
    #     ele.send_keys(Keys.END)
    #     time.sleep(1)
    #     newlen = driver.get_window_size()


    time.sleep(random.randint(4,5))
    ele = driver.find_element_by_xpath('//body')
    # ele = driver.find_element_by_xpath('/html/body')
    time.sleep(random.randint(4,5))
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(random.randint(4,8))

    totalcomments =driver.find_element_by_xpath('//*[@id="count"]/yt-formatted-string').text
    totalcomments = checkEnoughComz(int((cleanComz(totalcomments))))
    print('Searching for tags\n')
    #Loop to scroll to the bottom and load all comments
    for i in range(int(round(totalcomments/20))):
        ele.send_keys(Keys.END)
        time.sleep(random.randint(1,5))

    print('Almost there...\n')

    #Searching for all the elements and appending them to their respective lists
    commenta = driver.find_elements_by_xpath('//*[@id="content-text"]')
    authors = driver.find_elements_by_xpath('//a[@id="author-text"]/span')
    time_ago = driver.find_elements_by_xpath('//*[@id="header-author"]/yt-formatted-string/a')
    likes = driver.find_elements_by_xpath('//*[@id="vote-count-middle"]')
    for  a in range(len(commenta)):
        CommentFullList.append(commenta[a].text)
        CommenteeNameList.append(authors[a].text)
        TimeAgoList.append(time_ago[a].text)
        TotLikesList.append(likes[a].text)
    driver.quit()

    # zipping all the lists into one dataframe and then exporting it into CSV format. Data cleaning of emojis ,etc to be added
    df = pd.DataFrame(list(zip(CommenteeNameList, CommentFullList, TimeAgoList, TotLikesList)) , columns = ['Commenter' , 'Comment' , 'Time_Ago', 'Total_Likes'])
    print('Dataframe completed\n')
    df2 = df.drop(index=[0], axis=0)
    df2["Total Likes"] = df["Total Likes"].str.replace('K','00')
    df2["Total Likes"] = df["Total Likes"].str.replace('.','')
    df2.to_csv("YoutubeComments.csv" , index =False)
    print('Success!')
except Exception as e:
    driver.quit()
    print('Ran into some error!\n')
    print(e)
