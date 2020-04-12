from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://zzzscore.com/memory/en")
assert "Memory Test. couple cards" in driver.title

#Locators
countElement = '.count'
element = '#grid div span'
resultsSelector = '.resultContent > .level'

result = WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, countElement)))

allElements = driver.find_elements_by_css_selector(element);

seen = set()
unique = [obj for obj in allElements if obj.get_attribute('class') not in seen and not seen.add(obj.get_attribute('class'))]

for u in unique:
    
    cardType = u.get_attribute("class")
    print(cardType)
    matchingCards = [item for item in allElements if item.get_attribute("class") == cardType]
    for c in matchingCards:
        c.find_element_by_xpath('./..').click()

#Get Results
result = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, resultsSelector)))
print("Final Score %s" % (result.text))

#Save Screenshot
driver.get_screenshot_as_file("results.png")

driver.quit()