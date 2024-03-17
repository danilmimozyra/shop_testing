import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
time.sleep(1)
driver.find_element_by_css_selector("[class='fc-button-label']").click()
time.sleep(3)
driver.execute_script("window.scrollBy(0, 900);")
time.sleep(1)
driver.find_element_by_css_selector('[title="Selenium Ruby"]').click()
time.sleep(1)
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(1)
driver.find_element_by_css_selector('[class="reviews_tab"]').click()
time.sleep(1)
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(1)
driver.find_element_by_css_selector('[id="comment"]').send_keys("nice")
driver.find_element_by_css_selector('[class="star-5"]').click()
time.sleep(1)
driver.find_element_by_css_selector('[id="author"]').send_keys("guy")
time.sleep(1)
driver.find_element_by_css_selector('[id="email"]').send_keys('danyllaz40@gmail.com')
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(1)
driver.find_element_by_css_selector('[name="submit"]').click()
time.sleep(2)
driver.quit()