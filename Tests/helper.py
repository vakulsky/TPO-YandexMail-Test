from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


def document_initialised(driver):
    return driver.execute_script("return initialized")


def find_by_class(context, class_name):
    return WebDriverWait(context.browser, timeout=context.timeout)\
        .until(lambda driver: driver.find_element(By.CLASS_NAME, class_name))


def find_by_xpath(context, xpath):
    return WebDriverWait(context.browser, timeout=context.timeout)\
        .until(lambda driver: driver.find_element(By.XPATH, xpath))


def find_by_id(context, element_id):
    return WebDriverWait(context.browser, timeout=context.timeout)\
        .until(lambda driver: driver.find_element(By.ID, element_id))


def find_by_link(context, link):
    return WebDriverWait(context.browser, timeout=context.timeout)\
        .until(lambda driver: driver.find_element(By.LINK_TEXT, link))


def find_by_partial_link(context, partial_link):
    return WebDriverWait(context.browser, timeout=context.timeout)\
        .until(lambda driver: driver.find_element(By.PARTIAL_LINK_TEXT, partial_link))


def find_by_css_selector(context, css_selector):
    return WebDriverWait(context.browser, timeout=context.timeout)\
        .until(lambda driver: driver.find_element(By.CSS_SELECTOR, css_selector))

