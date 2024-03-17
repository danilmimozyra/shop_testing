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
driver.find_element_by_css_selector('[id="username"]').send_keys('danyllaz40@gmail.com')
time.sleep(1)
driver.find_element_by_css_selector('[id="password"]').send_keys('DanylLazurk0')
time.sleep(1)
driver.find_element_by_css_selector('[value="Login"]').click()
time.sleep(1)
driver.find_element_by_css_selector('[id="menu-item-40"]').click()
time.sleep(1)
driver.find_element_by_css_selector('[class="cat-item cat-item-19"] > a').click()
time.sleep(1)
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(1)
if len(driver.find_elements_by_css_selector('[class="woocommerce-LoopProduct-link"]')) == 3:
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
driver.find_element_by_link_text('My Account').click()
time.sleep(1)
driver.find_element_by_css_selector('[id="username"]').send_keys('danyllaz40@gmail.com')
time.sleep(1)
driver.find_element_by_css_selector('[id="password"]').send_keys('DanylLazurk0')
time.sleep(1)
driver.find_element_by_css_selector('[value="Login"]').click()
time.sleep(1)
driver.find_element_by_css_selector('[id="menu-item-40"]').click()
time.sleep(1)
if driver.find_element_by_css_selector('select > option[value="menu_order"]').get_attribute("selected") is not None:
    print("vse ok 1")
select = Select(driver.find_element_by_css_selector('[name="orderby"]'))
select.select_by_value("price")
time.sleep(1)
if driver.find_element_by_css_selector('select > option[value="price"]').get_attribute("selected") is not None:
    print("vse ok 2")
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
driver.find_element_by_css_selector('[id="menu-item-40"]').click()
time.sleep(1)
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)
driver.find_element_by_css_selector('[class="post-169 product type-product status-publish product_cat-android product_tag-android has-post-title no-post-date has-post-category has-post-tag has-post-comment has-post-author first instock sale downloadable taxable shipping-taxable purchasable product-type-simple"').click()
time.sleep(1)
text1 = driver.find_element_by_css_selector('del>[class="woocommerce-Price-amount amount"]').text
assert text1 == "₹600.00"
text2 = driver.find_element_by_css_selector('ins>[class="woocommerce-Price-amount amount"]').text
assert text2 == "₹450.00"
driver.find_element_by_css_selector('div[class="images"] > a > img').click()
img_open = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="pp_close"]')))
driver.find_element_by_css_selector('[class="pp_close"]').click()
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
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)
driver.find_element_by_css_selector('[data-product_id="182"]').click()
time.sleep(1)
text1 = driver.find_element_by_css_selector('[class="cartcontents"]').text
assert text1 == '1 Item'
text2 = driver.find_element_by_css_selector('[class="amount"]').text
assert text2 == '₹180.00'
time.sleep(1)
driver.find_element_by_css_selector('[id="wpmenucartli"]').click()
subtotal = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-title="Subtotal"] > span')))
if driver.find_element_by_css_selector('[data-title="Subtotal"] > span').text is not None:
    print('vse ok 1')
total = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'strong > [class="woocommerce-Price-amount amount"]')))
if driver.find_element_by_css_selector('strong > [class="woocommerce-Price-amount amount"]').text is not None:
    print('vse ok 2')
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
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)
driver.find_element_by_css_selector('[data-product_id="182"]').click()
time.sleep(1)
driver.find_element_by_css_selector('[data-product_id="170"]').click()
time.sleep(1)
driver.find_element_by_css_selector('[id="wpmenucartli"]').click()
time.sleep(1)
driver.find_element_by_css_selector('td[class="product-remove"] > a[data-product_id="182"]').click()
time.sleep(1)
driver.find_element_by_css_selector('[class="woocommerce-message"] > a').click()
time.sleep(1)
driver.find_element_by_css_selector('[class="quantity"] > input').clear()
time.sleep(1)
driver.find_element_by_css_selector('[class="quantity"] > input').send_keys("3")
time.sleep(1)
driver.find_element_by_css_selector('[name="update_cart"]').click()
time.sleep(1)
if int(driver.find_element_by_css_selector('[class="quantity"] > input').get_attribute("value")) == 3:
    print('vse ok 1')
time.sleep(1)
driver.find_element_by_css_selector('[name="apply_coupon"]').click()
time.sleep(1)
if driver.find_element_by_css_selector('[class="woocommerce-error"]').text == "Please enter a coupon code.":
    print('vse ok 2')
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
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)
driver.find_element_by_css_selector('[data-product_id="182"]').click()
time.sleep(1)
driver.find_element_by_css_selector('[id="wpmenucartli"]').click()
time.sleep(1)
driver.find_element_by_css_selector('[class="checkout-button button alt wc-forward"]').click()
time.sleep(1)
first_name = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id="billing_first_name"]')))
driver.find_element_by_css_selector('[id="billing_first_name"]').send_keys('Danyl')
driver.find_element_by_css_selector('[id="billing_last_name"]').send_keys('Lazurko')
driver.find_element_by_css_selector('[id="billing_email"]').send_keys('danyllaz40@gmail.com')
driver.find_element_by_css_selector('[id="billing_phone"]').send_keys('+71234567890')
time.sleep(1)
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)
driver.find_element_by_css_selector('[id="select2-chosen-1"]').click()
time.sleep(1)
driver.find_element_by_css_selector('div[class="select2-drop select2-display-none select2-with-searchbox select2-drop-active"] > div[class="select2-search"] > input').send_keys('Russi')
time.sleep(1)
driver.find_element_by_css_selector('[class="select2-drop select2-display-none select2-with-searchbox select2-drop-active"] > ul > :nth-child(1)').click()
time.sleep(1)
driver.find_element_by_css_selector('[id="billing_address_1"]').send_keys('Boyarskoho 2')
driver.find_element_by_css_selector('[id="billing_city"]').send_keys('Moscow')
driver.find_element_by_css_selector('[id="billing_state"]').send_keys('Russia')
driver.find_element_by_css_selector('[id="billing_postcode"]').send_keys('12345')
time.sleep(1)
driver.execute_script("window.scrollBy(0, 800);")
time.sleep(1)
driver.find_element_by_css_selector('[id="payment_method_cheque"]').click()
time.sleep(2)
driver.find_element_by_css_selector('[id="place_order"]').click()
text1 = driver.find_element_by_css_selector('[class="woocommerce-thankyou-order-received"]').text
assert text1 == 'Thank you. Your order has been received.'
text2 = driver.find_element_by_css_selector('[class="method"] > strong').text
assert text2 == 'Check Payments'
time.sleep(2)
driver.quit()