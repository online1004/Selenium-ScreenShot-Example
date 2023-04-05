from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import string, random

def gen(_LENGTH):
    string_pool = string.ascii_letters + string.digits
    result = "" 
    for i in range(_LENGTH):
        result += random.choice(string_pool)
    return result

def main():
    keyword = input('검색어를 입력하세요\n')
    options = Options()
    options.add_argument('--incognito')
    options.add_experimental_option("detach", True)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1920, 1080)
    url = 'https://naver.com/'
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@id="query"]').send_keys(keyword)
    driver.find_element(By.XPATH, '//*[@id="search_btn"]').click()
    el = driver.find_element(By.TAG_NAME, 'body')
    el.screenshot(f'./image/{gen(6)}.png')
    driver.quit()

main()