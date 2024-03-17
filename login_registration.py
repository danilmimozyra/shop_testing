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
time.sleep(1)
driver.find_element_by_link_text('My Account').click()
time.sleep(1)
driver.find_element_by_css_selector('[type="email"][class="woocommerce-Input woocommerce-Input--text input-text"]').send_keys('danyllaz40@gmail.com')
time.sleep(1)
driver.find_element_by_css_selector('[id="reg_password"]').send_keys('DanylLazurk0')
time.sleep(1)
driver.find_element_by_css_selector('[value="Register"]').click()
time.sleep(2)
driver.quit()




driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
time.sleep(1)
driver.find_element_by_css_selector("[class='fc-button-label']").click()
time.sleep(1)
driver.find_element_by_link_text('My Account').click()
time.sleep(1)
driver.find_element_by_css_selector('[id="username"]').send_keys('danyllaz40@gmail.com')
time.sleep(1)
driver.find_element_by_css_selector('[id="password"]').send_keys('DanylLazurk0')
time.sleep(1)
driver.find_element_by_css_selector('[value="Login"]').click()
time.sleep(1)
if driver.find_element_by_css_selector('[class="woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--customer-logout"] > a').get_attribute('href') is not None:
    print('vse ok')
time.sleep(2)
driver.quit()






driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
time.sleep(1)
driver.find_element_by_css_selector("[class='fc-button-label']").click()
time.sleep(1)
driver.find_element_by_css_selector('[id="menu-item-40"]').click()
time.sleep(1)
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(1)
driver.find_element_by_css_selector('[class="post-181 product type-product status-publish product_cat-html product_tag-html has-post-title no-post-date has-post-category has-post-tag has-post-comment has-post-author  instock taxable shipping-taxable purchasable product-type-simple"]').click()
time.sleep(1)
if driver.find_element_by_css_selector('[itemprop="name"]').text == 'HTML5 Forms':
    print('vse ok')
time.sleep(2)
driver.quit()