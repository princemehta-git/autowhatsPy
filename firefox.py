from time import sleep
from selenium import webdriver
from config import *
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


# # options = Options()
# # options.add_argument("user-data-dir=%s"%profile_path)
# profile = webdriver.FirefoxProfile(profile_path)
# driver = webdriver.Firefox(executable_path='geckodriver.exe', firefox_profile=profile)
# driver.get('https://web.whatsapp.com')


# chrome
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

options = webdriver.ChromeOptions()
# options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument("user-data-dir=%s"%profile_path)
options.add_argument("--app=https://www.google.com")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])

# # options.headless = True # also works
# options.add_argument("--headless")
# options.add_argument("--disable-extensions")
# options.add_argument("--proxy-server='direct://'")
# options.add_argument("--proxy-bypass-list=*")
# options.add_argument("--start-maximized")
# options.add_argument('--disable-gpu')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--no-sandbox')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(120)
driver.maximize_window()
path = 'C:\\Users\\PRINCE MEHTA\\Desktop\\Taranpreet Singh.pdf'
for i in range(5):
    # driver.get('https://web.whatsapp.com/send?phone=' + '+917858001577' + '&text=' + str(i))
    # sleep(3)
    # # driver.save_screenshot(str(i) + 'opened.png')
    # send_box = driver.find_element_by_xpath('//div[@class="_1UWac _1LbR4"]')
    # 
    # # driver.save_screenshot(str(i) + 'searching_sendbox.png')
    # try:
    #     send_box.click()
    #     # driver.save_screenshot(str(i) + 'clicked_1.png')
    # # sleep(1)
    # except:
    #     send_box.click()
    # 
    # sleep(3)
    # # driver.save_screenshot(str(i) + 'clicked_2.png')
    # ActionChains(driver).send_keys(Keys.ENTER).perform()
    # # driver.save_screenshot(str(i) + 'entered.png')
    # try:
    #     send_box.clear()
    # except:
    # 
    #     pass
    # # driver.save_screenshot(str(i) + 'sent.png')
    # sleep(5)
    
    try:

        driver.get('https://web.whatsapp.com/send?phone=' +
                   '+917858001577' + '&text=' + str(i)+"😁😋🤬")
        # sleep(3)
        send_box = driver.find_element_by_xpath('//div[@class="_1UWac _1LbR4"]')
        try:
            send_box.click()
        # sleep(1)
        except:
            send_box.click()
        sleep(1)
        ActionChains(driver).send_keys(':emoji' u'\u2764').perform()
        sleep(1)
        ActionChains(driver).send_keys(Keys.ENTER).perform()

        # try:
        #     send_box.clear()
        # except:
        #     pass
        sleep(3)
        try:
            # ActionChains(driver).key_down(Keys.LEFT_CONTROL).send_keys('v').key_up(Keys.LEFT_CONTROL).perform()
            driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span').click()

        except:
            sleep(1)
            driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span').click()
        sleep(1)
        driver.save_screenshot(str(i) + 'clicked_1.png')
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div[1]/div/ul/li[4]/button/input').send_keys(path)
        except:
            sleep(1)
            driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div[1]/div/ul/li[4]/button/input').send_keys(path)
        driver.save_screenshot(str(i) + 'clicked_2.png')
        sleep(2.5)
        ActionChains(driver).send_keys(Keys.ENTER).perform()
        # send_box = driver.find_element_by_xpath('//div[@class="_1UWac _1LbR4"]')
        # try:
        #     send_box.clear()
        # except:
        #     pass


    # except selenium.common.exceptions.UnexpectedAlertPresentException:
    #
    #     # Alert(driver).dismiss()
    #     sleep(3)
    #     try:
    #         driver.get('https://web.whatsapp.com/send?phone=' +
    #                    '+917858001577' + '&text=' + str(i))
    #         sleep(3)
    #
    #         driver.find_element_by_xpath('//div[@class="_1UWac _1LbR4"]').click()
    #         # sleep(1)
    #
    #         ActionChains(driver).send_keys(Keys.ENTER).perform()
    except :
        # driver.execute_script("window.open()")
        # driver.close()
        # driver.switch_to.window(driver.window_handles[0])
        # try:
        #     # Alert(driver).accept()
        #
        # except:
        #     pass
        # try:
        #     send_box.clear()
        # except:
        #     pass
        driver.get('https://web.whatsapp.com/send?phone=' +
                   '+917858001577' + '&text=' + str(i))
        # sleep(3)

        send_box = driver.find_element_by_xpath('//div[@class="_1UWac _1LbR4"]')
        try:
            send_box.click()
        # sleep(1)
        except:
            send_box.click()

        ActionChains(driver).send_keys(Keys.ENTER).perform()

        # try:
        #     send_box.clear()
        # except:
        #     pass
    sleep(2)