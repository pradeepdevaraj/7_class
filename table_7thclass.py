from selenium import webdriver

driver=webdriver.Chrome()
driver.get("file:///C:/Users/Pradeepa.D/Desktop/WEBTABLE.html")
driver.maximize_window()
driver.implicitly_wait(30)

ele =  driver.find_elements_by_xpath("/html/body/tittle/tittle/table/thead/tr/th")

ele1 = driver.find_elements_by_xpath("/html/body/tittle/tittle/table/tbody/tr[1]/td")

print(len(ele1))
print("bazinga")
print(len(ele))
#first_part="//*[@id='emp']/thead/tr/th["