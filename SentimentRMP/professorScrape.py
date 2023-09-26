from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time


def getProfNames(arr):

    #establish webdriver
    driver = webdriver.Chrome()

    # ad blocker
    chrome_options = ChromeOptions()
    chrome_options.add_extension('extension_5_10_1_0.crx')
    driver = webdriver.Chrome(options = chrome_options)
    #access web page using web driver
    driver.get("https://www.ratemyprofessors.com/search/professors/18846?q=*")

    # names = []
    count = 0

    # number of profs
    numNames = driver.find_element("xpath", '//*[@id="root"]/div/div/div[4]/div[1]/div[1]/div[1]/div/h1')
    numNamesText = numNames.text
    numNamesInt = int(numNamesText[:4])
    # Close cookies button
    buttonClose = driver.find_element("xpath", '/html/body/div[5]/div/div/button')
    buttonClose.click()

    for i in range(1, 20):
    # for i in range(1, numNamesInt + 1):
        # 8 professors per page
        if count == 8:
            time.sleep(3)
            # click show more button
            buttonShow = driver.find_element("xpath", '//*[@id="root"]/div/div/div[4]/div[1]/div[1]/div[4]/button')
            buttonShow.click()
            time.sleep(3)
            count = 0
        # scrape prof names
        xpath = f'//*[@id="root"]/div/div/div[4]/div[1]/div[1]/div[3]/a[{i}]/div/div[2]/div[1]'
        xpath_name = driver.find_element("xpath", xpath)
        name_text = xpath_name.text
        arr.append(name_text)
        count += 1
        print(arr)

names = []
getProfNames(names)

