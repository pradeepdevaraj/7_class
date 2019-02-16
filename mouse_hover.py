from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(30)

element = driver.find_element_by_xpath("//*[@id='container']/div/div[2]/div/ul/li[3]/span")

ActionChains(driver).move_to_element(element).click(element).perform()

#ActionChains(driver).move_to_element(element).click(element).perform()