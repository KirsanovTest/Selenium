from selenium import webdriver
import time

url = "https://www.youtube.com/"

browser = webdriver.Chrome(executable_path="C:\\Users\\ilyab\\Desktop\\QA\\AutoTest\\chromedriver.exe")

try:
    browser.get(url=url)

    searchbox = browser.find_element_by_xpath('//*[@id="search"]')
    searchbox.send_keys('ilusha') 
    searchbutton = browser.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
    searchbutton.click()

    time.sleep(5)

except Exception as ex: 
    print(ex)   
finally:
    browser.close()
    browser.quit()


# browser.get('https://www.youtube.com/') 
# searchbox = browser.find_element_by_xpath('//*[@id="search"]')
# searchbox.send_keys('ilusha')  