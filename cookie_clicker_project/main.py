from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

# timeout variable can be omitted, if you use specific value in the while condition
game_timeout = 300   # [seconds] #5 minutes

game_check_timeout = 5

time_start = time.time()
check_start_time = time.time()

while time.time() < time_start + game_timeout:
    cookie.click()

    if time.time() > check_start_time + game_check_timeout:
        store_menu = driver.find_elements(By.CSS_SELECTOR, "#store div:not(.grayed) b")

        current_money = int(driver.find_element(By.ID, value="money").text)
        menu_items_amount = []

        for item_no in range(0, len(store_menu)):
            item_price = int(store_menu[item_no].text.split(" - ")[1])
            menu_items_amount.append(item_price)

        for item_no in range(len(menu_items_amount)-1, -1, -1):
            if menu_items_amount[item_no] < current_money:
                item_to_be_purchased = store_menu[item_no]
                item_to_be_purchased.click()
                break

        check_start_time = time.time()


cookies_per_second = driver.find_element(By.ID, value="cps").text
print(cookies_per_second)

driver.quit()
