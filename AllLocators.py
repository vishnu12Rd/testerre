import logging
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Firefox()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
rounds=driver.find_elements(By.CSS_SELECTOR,"input.radioButton")
for round in rounds:
    round.click()
driver.find_element(By.CSS_SELECTOR,"input#autocomplete").send_keys("Ind")
wait=WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"div.ui-menu-item-wrapper")))
countries=driver.find_elements(By.CSS_SELECTOR,"div.ui-menu-item-wrapper")
for country in countries:
    if country.text == 'India':
        country.click()
windows=driver.window_handles
driver.switch_to.window(windows[1])
select=Select(driver.find_element(By.CSS_SELECTOR,"select#dropdown-class-example"))
select.select_by_value("option2")
check_boxes=driver.find_elements(By.XPATH,"//div[@id='checkbox-example']//input")
for check in check_boxes:
    check.click()
driver.find_element(By.CSS_SELECTOR,"button#openwindow").click()
windows=driver.window_handles
driver.switch_to.window(windows[1])
print(driver.find_element(By.XPATH,"//div[@class='support float-left']//span").text)
driver.close()
driver.switch_to.window(windows[0])
driver.find_element(By.CSS_SELECTOR,"a#opentab.btn-style").click()
time.sleep(2)
windows=driver.window_handles
driver.switch_to.window(windows[1])
driver.close()
time.sleep(2)

driver.switch_to.window(windows[0])
driver.find_element(By.CSS_SELECTOR,"cd")
driver.find_element(By.CSS_SELECTOR,"input#name").send_keys("VIsh")
driver.find_element(By.CSS_SELECTOR,"input#confirmbtn").click()
time.sleep(2)
alert=driver.switch_to.alert
alert.accept()
element=driver.find_element(By.CSS_SELECTOR,"input#displayed-text")
#driver.execute_script("arguments[0].scrollIntoView(true);",element)
#location=element.location_once_scrolled_into_view
#print(location)
driver.execute_script("arguments[0].scrollIntoView(true);",element)
time.sleep(4)
assert driver.find_element(By.CSS_SELECTOR,"input#displayed-text").is_displayed()
driver.find_element(By.CSS_SELECTOR,"input#hide-textbox").click()
driver.find_element(By.CSS_SELECTOR,"input#show-textbox").click()
assert driver.find_element(By.CSS_SELECTOR,"input#displayed-text").is_displayed()
print(driver.find_element(By.XPATH,"(//table[@id='product']//td)[1]").text)
action=ActionChains(driver)
action.drag_and_drop_by_offset()
ele=driver.find_element(By.XPATH, "(//table[@id='product'])[1]//td[1]")
action.click(ele).send_keys()
instructor=[]
Course=[]
Price=[]
#mile=driver.find_elements(By.XPATH,"(//table[@id='product'])[1]//td[i]")
instructors=driver.find_elements(By.XPATH, "(//table[@id='product'])[1]//td[1]")
for i in instructors:
    instructor.append(i.text)

for i in ran
    ge(1,2):
    for j in range(1,4):
        if j == 1:
            instructors = driver.find_elements(By.XPATH, "(//table[@id='product'])[1]//td[1]")
            print(len(instructors))
            for inst in instructors:
                instructor.append(inst.text)
        elif j == 2:
            courses = driver.find_elements(By.XPATH, "(//table[@id='product'])[1]//td[2]")
            print(len(courses))
            for cour in courses:
                Course.append(cour.text)
        else:
            prices = driver.find_elements(By.XPATH, "(//table[@id='product'])[1]//td[3]")
            print(len(prices))
            for pri in prices:
                Price.append(pri.text)
logging.DEBUG(instructor)
print(Course)
print(Price)
action=ActionChains(driver)
action.move_by_offset()
action.move_to_element_with_offset()
action.move_to_element().perform()