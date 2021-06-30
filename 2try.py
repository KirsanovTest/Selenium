from selenium import webdriver
import time


browser = webdriver.Chrome()


    
browser.get('https://webdesign-master.ru/blog/tools/578.html')
forBusiness = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/article/div/div[2]/div[3]/p[2]/a').click()  #Second try
memTest = browser.find_element_by_xpath('/html/body/header/div/div[1]/div[2]/div[2]/a').click()




time.sleep(7)
browser.close()
browser.quit()
    