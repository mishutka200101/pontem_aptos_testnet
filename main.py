from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from fake_useragent import UserAgent
import time
import secrets
import string


url = "https://liquidswap.pontem.network/#/"


def main():
    user_agent = UserAgent()
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user_agent.random}")
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_argument('--disable-gpu')
    # options.add_argument('--disable-infobars')
    # options.add_argument("--mute-audio")
    # options.add_argument('--profile-directory=Default')
    # options.add_argument("--mute-audio")
    # options.add_argument('--no-sandbox')
    options.add_extension("multimask-chrome-1.1.2.crx")
    driver = webdriver.Chrome(
        executable_path="chromedriver/chromedriver.exe",
        options=options
    )
    try:
        wait = WebDriverWait(driver, 10)

        time.sleep(10)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.get('chrome-extension://chgmppikpkmedppalnmnbcbnhbfhoile/home.html#initialize/welcome')
        time.sleep(5)
        driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/button').click()
        time.sleep(5)
        driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/button').click()
        time.sleep(5)
        driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]').click()
        time.sleep(5)
        password_location = driver.find_element(by=By.XPATH, value='// *[ @ id = "create-password"]')
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(8))
        password_location.send_keys(password)
        # time.sleep(10)
        driver.find_element(by=By.XPATH, value='//*[@id="confirm-password"]').send_keys(password)
        driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div[2]/form/div[3]/div').click()
        driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div[2]/form/button').click()
        time.sleep(5)
        driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/button').click()
        time.sleep(5)
        driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[5]/div[2]').click()
        time.sleep(5)

        mnemonic = driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[5]/div').text.split(' ')
        print(mnemonic)
        time.sleep(60)
        driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div[2]/div[2]/button[2]').click()
        driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div[2]/div[5]')

        # driver.find_element(by=By.XPATH, value='')
        # driver.find_element(by=By.XPATH, value='')
        # driver.find_element(by=By.XPATH, value='')

        # driver.find_element(by=By.XPATH, value='')
        # driver.find_element(by=By.XPATH, value='')
        # driver.find_element(by=By.XPATH, value='')
        # driver.find_element(by=By.XPATH, value='')


    except Exception as ex:
        print(ex)
        driver.close()
        driver.quit()
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    main()
