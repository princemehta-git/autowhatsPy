from selenium import webdriver
from config import *
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=%s"%profile_path)