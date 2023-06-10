from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:/Users/HP/chromedriver_win32/chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.get("https://www.python.org/")
dict = {}
for i in range(5):
    date = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i+1}]/time').text
    event = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i+1}]/a').text
    t_n_dict = {
        'time': date,
        'name': event
    }
    dict[i] = t_n_dict
print(dict)
driver.quit()

