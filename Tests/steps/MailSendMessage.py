from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from helper import *
from time import sleep

import os
from dotenv import load_dotenv
import traceback

use_step_matcher("re")

Y_MAIL_AUTH_URL = "https://mail.yandex.ru/"
Y_MAIL_URL = "https://mail.yandex.ru/"

time_delayed = ""


@given("I'm authenticated user on inbox page")
def step_impl(context):
    try:
        context.browser.get(Y_MAIL_AUTH_URL)
        find_by_class(context, "PSHeader-NoLoginButton").click()
        find_by_xpath(context, "//div[@class='AuthLoginInputToggle-wrapper']//button[1]").click()
        find_by_id(context, "passp-field-login").send_keys(os.getenv("EMAIL"))
        find_by_id(context, "passp:sign-in").click()
        find_by_id(context, "passp-field-passwd").send_keys(os.getenv("PASS"))
        find_by_id(context, "passp:sign-in").click()

    except Exception as e:
        traceback.print_exc()

        # close modal promo banner if found
        # try:
        #     if(fin)
        #     find_by_class(context, "Button2_pin_circle-circle").click()
        # except:
        #     pass

        # close fullscreen promo banner if found
        # try:
        #     promo_close_button = context.browser.find_element(By.CLASS_NAME, "Button2_pin_circle-circle")
        #     promo_close_button.click()
        # except:
        #     pass


@when("I click on Write button")
def step_impl(context):
    find_by_xpath(context, "//a[@href='#compose']").click()
    # find_by_partial_link(context, "compose").click()


@step("I fill Email field with user's email")
def step_impl(context):
    load_dotenv()
    find_by_xpath(context, "//div[@title='Кому']").send_keys(os.getenv("EMAIL"))


@step("I fill Subject field with (?P<subject>.+)")
def step_impl(context, subject):
    find_by_class(context, "composeTextField").send_keys(subject)


@step("I fill Body field with (?P<body>.+)")
def step_impl(context, body):
    find_by_xpath(context, "//div[@title='Напишите что-нибудь']/div").send_keys(body)


@step("Click Send button")
def step_impl(context):
    find_by_xpath(context, "//div[contains(@class, 'ComposeSendButton')]/button").click()


@step("I navigate to Sent messages")
def step_impl(context):
    find_by_xpath(context, "//div[@class='ComposeDoneScreen-Actions']/a").click()
    find_by_xpath(context, "//a[@href='#sent']").click()


@then("I should see new message with subject (?P<subject>.+)")
def step_impl(context, subject):
    subject_data = find_by_xpath(context,
                                 "//span[@class='mail-MessageSnippet-Item mail-MessageSnippet-Item_subject'][1]/span[1]")
    assert (subject_data.text == subject)


@step("I navigate to Inbox messages")
def step_impl(context):
    find_by_xpath(context, "//a[@href='#inbox']").click()


@step("I sync messages")
def step_impl(context):
    find_by_xpath(context, "//button[contains(@class, 'qa-LeftColumn-SyncButton')]").click()
    sleep(3)


@step("Click Delay button")
def step_impl(context):
    find_by_xpath(context, "//div[contains(@class, 'ComposeDelayedSendingButton')]/button").click()


@step("Click Custom Date button")
def step_impl(context):
    find_by_xpath(context, "//div[contains(@class, 'DelayedSendingOptions-CustomDate')]").click()


@step("Click Save button")
def step_impl(context):
    find_by_xpath(context, "//button[contains(@class, 'ComposeDateTimePicker-Button_save')]").click()


@step("I navigate to Outbox messages")
def step_impl(context):
    find_by_xpath(context, "//div[@class='ComposeDoneScreen-Actions']/a").click()
    find_by_xpath(context, "//a[@href='#outbox']").click()


@then("I should see a message with subject (?P<subject>.+) and delayed time")
def step_impl(context, subject):
    print(time_delayed)
    subject_data = find_by_xpath(context,
                                 "//span[@class='mail-MessageSnippet-Item mail-MessageSnippet-Item_subject'][1]/span[1]")
    time_delay_el = find_by_xpath(context,
                                  "//div[@class=' mail-MessageSnippet-Item mail-MessageSnippet-Item_date']/span")

    assert (subject_data.text == subject and time_delay_el.text.find(time_delayed) != -1)


@step("Click on custom time field")
def step_impl(context):
    find_by_xpath(context, "//div[contains(@class, 'ComposeDateTimePicker-Input_time')]//input").click()


@step("Choose first time")
def step_impl(context):
    global time_delayed
    time_delayed = find_by_xpath(context, "//div[@cls='DelayedDatePicker']//button"
                                          "[contains(@class, 'DelayedTimePicker') and not(contains(@class, 'isDisable'))]/span").text
    find_by_xpath(context, "//div[@cls='DelayedDatePicker']//button"
                           "[contains(@class, 'DelayedTimePicker') and not(contains(@class, 'isDisable'))]").click()
