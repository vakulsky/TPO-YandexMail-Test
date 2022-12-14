from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from dotenv import load_dotenv


def before_feature(context, feature):
    load_dotenv()
    driver_path = os.getenv("DRIVER_PATH")
    wait_timeout = os.getenv("WAIT_TIMEOUT")
    context.timeout = wait_timeout
    service = Service(executable_path=driver_path)
    context.browser = webdriver.Chrome(service=service)


def after_feature(context, feature):
    context.browser.close()
