from behave import *

use_step_matcher("re")
from behave import *
from helper import *
from time import sleep
from selenium.webdriver.common.keys import Keys

import os


@step("I've just received message with some subject (?P<subject>.+)")
def step_impl(context, subject):
    find_by_xpath(context, "//a[@href='#compose']").click()
    find_by_xpath(context, "//div[@title='Кому']").send_keys(os.getenv("EMAIL"))
    find_by_class(context, "composeTextField").send_keys(subject)
    find_by_xpath(context, "//div[contains(@class, 'ComposeSendButton')]/button").click()
    find_by_xpath(context, "//div[@class='ComposeDoneScreen-Actions']/a").click()


@when("I select message with subject (?P<subject>.+)")
def step_impl(context, subject):
    subject_data = find_by_xpath(context,
                                 "//span[@class='mail-MessageSnippet-Item mail-MessageSnippet-Item_subject'][1]/span[1]")

    if subject_data.text.find(subject) != -1:
        find_by_xpath(context,
                      "//div[@class='mail-MessageSnippet-Content']//"
                      "div[contains(@class, 'mail-MessageSnippet-CheckboxNb-Container')]").click()


@step("Click on Delete button")
def step_impl(context):
    try:
        find_by_xpath(context, "//div[contains(@class, 'js-toolbar-item-delete')]").click()
    except:
        pass


@then("I should not see message with subject (?P<subject>.+)")
def step_impl(context, subject):
    subject_data = find_by_xpath(context,
                                 "//span[@class='mail-MessageSnippet-Item mail-MessageSnippet-Item_subject'][1]/span[1]")
    assert(subject_data.text.find(subject) == -1)