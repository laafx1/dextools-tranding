from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time 
import csv
import xlsxwriter
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException       

def welcome():
    # options = webdriver.ChromeOptions()
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--ignore-ssl-errors')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--enable-features=NetworkService,NetworkServiceInProcess')
    # options.add_argument('--dns-prefetch-disable')
    # options.add_argument("--start-maximized")
    # options.add_argument('window-size=1920x1080')
    # # options.add_argument('--headless')
    # options.add_argument("--incognito")
    # driver = webdriver.Chrome(chrome_options = options)
    last_page = input('Your link : ')
    repeat = int(input('how much time repeat: '))
    i=0

    for h in range(1, repeat):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--disable-gpu')
        options.add_argument('--enable-features=NetworkService,NetworkServiceInProcess')
        options.add_argument('--dns-prefetch-disable')
        options.add_argument("--start-maximized")
        options.add_argument('window-size=1920x1080')
        # options.add_argument('--headless')
        options.add_argument("--incognito")
        driver = webdriver.Chrome(chrome_options = options)
        driver.get(last_page)
        time.sleep(1)
        close_button = driver.find_element_by_xpath("//button[@class='close ng-star-inserted']")
        wait = WebDriverWait(driver, 20)
        close_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='close ng-star-inserted']"))).click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[@class='presale-button']").click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element_by_xpath("//a[@class='shared-button ng-tns-c139-4 ng-star-inserted']").click()
        time.sleep(1.5)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        driver.find_element_by_xpath("//a[@class='favs-button ng-tns-c139-4 ng-star-inserted']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//a[@class='ng-tns-c139-4 ng-star-inserted']").click()
        time.sleep(0.5)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.close()
        i+=1


def main():
    welcome()

if __name__ == "__main__":
    main() 



