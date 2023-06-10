from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time as t
import threading as th
from selenium.common import exceptions as e
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import staleness_of

# Constants
Available = []
ignored_exceptions = (e.NoSuchElementException, e.StaleElementReferenceException)
time_out = 5


# Function to check if upgrades are available
def add_upgrades_to_list():
    global Available
    for i in element_list:
        try:
            if i.get_dom_attribute('class') != 'grayed':
                if i not in Available:
                    Available.append(i)
                    print(i)
                else:
                    continue
            else:
                return None
        except e.StaleElementReferenceException:
            pass


# Check affordable and buy the most expensive:
def check_and_buy_exp():
    global money
    price_list = []
    for i in Available:
        price = int(i.text.split("-")[1].split("\n")[0].replace(',', '').strip())
        price_list.append(price)
    try:
        max_price = max(price_list)
    except ValueError:
        print("empty")
    else:
        if money > max_price:
            for i in Available:
                try:
                    if int(i.text.split("-")[1].split("\n")[0].replace(',', '').strip()) == max_price:
                        i.click()
                    else:
                        print("Not clicked")
                except e.StaleElementReferenceException:
                    pass
        else:
            print("Less money")


# Body code
service = Service("C:/Users/HP/chromedriver_win32/chromedriver.exe")

driver = webdriver.Chrome(service=service)
# Get Website
driver.get("http://orteil.dashnet.org/experiments/cookie/")
# Get money to compare and cookie to click
cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')
upgrade_check = t.time() + 5
time_out = t.time() + 60 * 5

# calling all elements and putting them in list:
cursor = driver.find_element(By.XPATH, '//*[@id="buyCursor"]')
grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]')
factory = driver.find_element(By.XPATH, '//*[@id="buyFactory"]')
mine = driver.find_element(By.XPATH, '//*[@id="buyMine"]')
shipment = driver.find_element(By.XPATH, '//*[@id="buyShipment"]')
alchemy = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]')
portal = driver.find_element(By.XPATH, '//*[@id="buyPortal"]')
t_m = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]')

element_list = [cursor, grandma, factory, mine, shipment, alchemy, portal, t_m]

# Create while loop to click cookie as fast as possible:
while True:
    money = int(driver.find_element(By.XPATH, '//*[@id="money"]').text)
    cookie.click()
    # Create and call a function to check if upgrades are available and purchase the most expensive one:
    add_upgrades_to_list()
    check_and_buy_exp()

driver.quit()
