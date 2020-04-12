from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://zzzscore.com/1to50/")
assert "1to50" in driver.title

#Locators
numberSelector = '//*[@id=\"grid\"]//div[text()=\"%s\"]'
resultsSelector = '.resultContent > .level'

for x in range(1, 50+1):
    print("Looking for %d" % (x))
    elem = driver.find_element_by_xpath(numberSelector % (x))
    elem.click()

#Get Results
result = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, resultsSelector)))
print("Final Score %s" % (result.text))

#Save Screenshot
driver.get_screenshot_as_file("results.png")

driver.quit()