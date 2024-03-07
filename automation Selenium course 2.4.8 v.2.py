from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
start = time.perf_counter()







url = "http://suninjuly.github.io/explicit_wait2.html"
with webdriver.Chrome() as driver:
    driver.get(url)

    WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    driver.find_element(By.ID, 'book').click()

    spans = driver.find_elements(By.CLASS_NAME, 'nowrap')
    x = int(spans[3].text)
    eq = math.log(abs(12 * math.sin(x)))
    inp = driver.find_element(By.ID, 'answer')
    inp.send_keys(eq)
    driver.find_element(By.ID, 'solve').click()

    time.sleep(10)







stop = time.perf_counter()
print('\n' + 'script time =', stop - start, 'sec')
