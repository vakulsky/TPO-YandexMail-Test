from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from helper import document_initialised

import os
from dotenv import load_dotenv
import traceback

use_step_matcher("re")

Y_MAIL_AUTH_URL = "https://mail.yandex.ru/"
Y_MAIL_URL = "https://mail.yandex.ru/"


@given("I'm authenticated user on inbox page")
def step_impl(context):
    load_dotenv()
    email = os.getenv("EMAIL")
    password = os.getenv("PASS")

    try:
        context.browser.get(Y_MAIL_AUTH_URL)
        to_login_button = context.browser.find_element(By.CLASS_NAME, "PSHeader-NoLoginButton")
        to_login_button.click()

        email_field = context.browser.find_element(By.ID, "passp-field-login")
        login_button = context.browser.find_element(By.ID, "passp:sign-in")
        email_field.send_keys(email)
        login_button.click()
        password_field = WebDriverWait(context.browser, timeout=3).until(lambda driver: driver.find_element(By.ID, "passp-field-login"))
        password_field.send_keys(password)
        login_button.click()
        WebDriverWait(context.browser, timeout=10).until(document_initialised)

    except Exception as e:
        traceback.print_exc()

        # close modal promo banner if found
        try:
            promo_close_button = context.browser.find_element(By.CLASS_NAME, "Button2_pin_circle-circle")
            promo_close_button.click()
        except:
            pass

        # close fullscreen promo banner if found
        # try:
        #     promo_close_button = context.browser.find_element(By.CLASS_NAME, "Button2_pin_circle-circle")
        #     promo_close_button.click()
        # except:
        #     pass


@when("I click on Write button")
def step_impl(context):
    write_button = context.browser.find_element(By.LINK_TEXT, "#compose")
    write_button.click()


@step("I fill Email field with user's email")
def step_impl(context):
    load_dotenv()
    email = os.getenv("EMAIL")
    email_field = context.browser.find_element(By.CLASS_NAME, "composeYabbles")
    email_field.send_keys(email)


@step("I fill Subject field with (?P<subject>.+)")
def step_impl(context, subject):
    subject_field = context.browser.find_element(By.CLASS_NAME, "composeTextField")
    subject_field.send_keys(subject)


@step("I fill Body field with (?P<body>.+)")
def step_impl(context, body):
   body_field = context.browser.find_element(By.CLASS_NAME, "composeYabbles")
   body_field.send_keys(body)


@step("Click Send button")
def step_impl(context):
    send_button = context.browser.find_element(By.CLASS_NAME, "ComposeSendButton-Text")
    send_button.click()


@step("I navigate to Sent messages")
def step_impl(context):
    sent_href = context.browser.find_element(By.LINK_TEXT, "#sent")
    sent_href.click()


@then("I should see new message with subject (?P<subject>.+)")
def step_impl(context, subject):
    subject_data = context.browser.find_element(By.XPATH, "//span[@class='mail-MessageSnippet-Item mail-MessageSnippet-Item_subject']/span[1]")
    assert (subject_data.get_text() == subject)


@step("I navigate to Inbox messages")
def step_impl(context):
    inbox_href = context.browser.find_element(By.LINK_TEXT, "#inbox")
    inbox_href.click()


@step("Click Delay button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Click Delay button')


@step("Fill time field with (?P<time>.+)")
def step_impl(context, time):
    """
    :type context: behave.runner.Context
    :type time: str
    """
    raise NotImplementedError(u'STEP: And Fill time field with <time>')


@step("Click Save button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Click Save button')


@step("I navigate to Outbox messages")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I navigate to Outbox messages')


@then("I should see a message with subject (?P<subject>.+) and delayed time (?P<time>.+)")
def step_impl(context, subject, time):
    """
    :type context: behave.runner.Context
    :type subject: str
    :type time: str
    """
    raise NotImplementedError(u'STEP: Then I should see a message with subject <subject> and delayed time <time>')
