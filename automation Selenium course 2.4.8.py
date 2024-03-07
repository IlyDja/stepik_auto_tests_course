from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# import  os
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, 'book').click()



    # browser.find_element(By.TAG_NAME, 'button').click()
    # time.sleep(1)
    # browser.switch_to.window(browser.window_handles[1])
    # time.sleep(1)

    spans = browser.find_elements(By.CLASS_NAME, 'nowrap')
    x = int(spans[3].text)
    eq = math.log(abs(12 * math.sin(x)))
    inp = browser.find_element(By.ID, 'answer')
    inp.send_keys(eq)
    browser.find_element(By.ID, 'solve').click()


    # inpts = browser.find_elements(By.TAG_NAME, 'input')
    # for inp in inpts[:-1]:
    #     inp.send_keys('anon')
    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # file_name = "gg.txt"
    # file_path = os.path.join(current_dir, file_name)
    # element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    # element.send_keys(file_path)

    # inpts[-1].send_keys(os.path.dirname(__file__) + '\\11.txt')
    # time.sleep(1)
    # browser.find_element(By.TAG_NAME, "button").click()
    # res = calc(int(browser.find_element(By.ID, 'input_value').text))
    # button = browser.find_element(By.TAG_NAME, "button")
    # #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # browser.execute_script("window.scrollBy(0, 100);")
    # browser.find_element(By.ID, 'answer').send_keys(res)
    # browser.find_element(By.ID, 'robotCheckbox').click()
    # browser.find_element(By.ID, 'robotsRule').click()
    # button.click()
    # browser.find_element(By.ID, 'dropdown').click()
    # browser.find_element(By.CSS_SELECTOR, f"[value='{x}']").click()
    # browser.find_element(By.TAG_NAME, 'button').click()


    # name = browser.find_element(By.XPATH, pattern.format('first'))
    # surname = browser.find_element(By.XPATH, pattern.format('second'))
    # email = browser.find_element(By.XPATH, pattern.format('third'))
    # form = [name, surname, email]
    # for input_ in form:
    #     input_.send_keys('anon')
    #     time.sleep(1)
    #
    # # Отправляем заполненную форму
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()
    #
    # # Проверяем, что смогли зарегистрироваться
    # # ждем загрузки страницы
    # time.sleep(1)
    #
    # # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text
    #
    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text


except Exception as e:
    print(f"Oops, something went wrong! {e}")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()