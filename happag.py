import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
import subprocess
import sys
from datetime import date, timedelta
import calendar


def happag(from_city, to_city, date):
    try:
        subprocess.call("TASKKILL /F /IM chrome.exe", shell=True)
    except:
        print("No apps closed")
        
    driver = uc.Chrome()

    while True:
        try:
            driver.get("https://solutions.hapag-lloyd.com/quick-quotes/#/")
            sleep(3)
            start_loc = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/form/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/label/div/div[1]/div[2]/div[1]/input")
            start_loc.click()
            start_loc.send_keys(from_city)
            sleep(2)
            option = driver.find_elements(By.CLASS_NAME, "q-item__section.column.q-item__section--main.justify-center")
            option[0].click()


            end_loc = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/form/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/label/div/div/div[2]/div[1]/input")
            end_loc.click()
            end_loc.send_keys(to_city)
            sleep(2)
            option = driver.find_elements(By.CLASS_NAME, "q-item__section.column.q-item__section--main.justify-center")
            option[0].click()


            #q-item__label
            driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/form/div/div[2]/div[2]/div[2]/div[1]/div/div/label/div/div/div[1]/input").click()
            date_element = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/form/div/div[2]/div[2]/div[2]/div[1]/div/div/label/div/div/div[1]/input")
            date_element.send_keys(Keys.CONTROL, 'a')
            date_element.send_keys(Keys.BACKSPACE)
            driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/form/div/div[2]/div[2]/div[2]/div[1]/div/div/label/div/div/div[1]/input").send_keys(date)
            # q-item__section column q-item__section--main justify-center

            driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/form/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/label/div/div/div[1]/div[1]").click()
            sleep(1)
            container_types = driver.find_elements(By.CLASS_NAME, "q-item__section.column.q-item__section--main.justify-center")
            container_types[0].click() # 0 CHOOSES 20' GENERAL PURPOSE, 1 CHOOSES 40' GENERAL PURPOSE


            checkbox = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/form/div/div[3]/div[2]/div[2]/div/div[1]/label/div/div/div/div/div[1]")
            driver.execute_script("arguments[0].scrollIntoView();", checkbox)
            checkbox.click()

            sleep(0.1)

            driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/form/div/div[3]/div[2]/div[2]/div/div[2]/button").click()
          

            break


        except:
            try:
                wait = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/iframe")))
                iframe = driver.find_element("xpath", "/html/body/div[2]/div/div[2]/iframe")
                driver.switch_to.frame(iframe)
                wait = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div")))
                driver.find_element("xpath", '/html/body/div[2]/div/div/form/div[3]/div[1]/input').click()
                driver.find_element("xpath", '/html/body/div[2]/div/div/form/div[3]/div[1]/input').click()
                driver.find_element("xpath", '/html/body/div[2]/div/div/form/div[3]/div[1]/input').send_keys("timescantaufeek")

                #/html/body/div[2]/div/div/form/div[3]/div[2]/input

                driver.find_element("xpath", '/html/body/div[2]/div/div/form/div[3]/div[2]/input').click()
                driver.find_element("xpath", '/html/body/div[2]/div/div/form/div[3]/div[2]/input').click()
                driver.find_element("xpath", '/html/body/div[2]/div/div/form/div[3]/div[2]/input').send_keys("TIMESCAN")

                driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/div[3]/div[4]/button").click()
                driver.switch_to.default_content()
                wait = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/form/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/label/div/div[1]/div[2]/div[1]/input")))
                continue
            except:
                print("solve captcha")
                wait = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#request > div")))
                continue

todays_date = date.today()
two_weeks = todays_date + timedelta(weeks = 2)  
two_weeks_list = str(two_weeks).split("-")
date_input = two_weeks_list[2] + "." + two_weeks_list[1] + "." + two_weeks_list[0]


happag(sys.argv[1], sys.argv[2], date_input)