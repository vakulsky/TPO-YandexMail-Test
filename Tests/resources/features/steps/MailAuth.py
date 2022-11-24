from behave import *
from helper import *
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

import os

use_step_matcher("re")

Y_MAIL_AUTH_URL = "https://mail.yandex.ru/"
Y_MAIL_URL = "https://mail.yandex.ru/"


@given("I'm on the mail page")
def step_impl(context):
    context.browser.get(Y_MAIL_URL)


@step("I enter user's email")
def step_impl(context):
    find_by_id(context, "passp-field-login").send_keys(os.getenv("EMAIL"))


@step("I enter user's password")
def step_impl(context):
    find_by_id(context, "passp-field-passwd").send_keys(os.getenv("PASS"))


@step("I click on login button")
def step_impl(context):
    find_by_id(context, "passp:sign-in").click()


@then("I should see user's Inbox page")
def step_impl(context):
    sleep(5)
    WebDriverWait(context.browser, 10).until(EC.title_contains("Входящие"))
    assert (context.browser.title.find("Входящие") != -1)


@then("I should see NoUserExists message")
def step_impl(context):
    error_hint = find_by_id(context, "field:input-login:hint")

    assert (error_hint.text.find("Такого аккаунта нет") != -1)


@then("I should see WrongPassword message")
def step_impl(context):
    error_hint = find_by_id(context, "field:input-passwd:hint")

    assert (error_hint.text.find("Неверный пароль") != -1)


@step("I select email as login type")
def step_impl(context):
    find_by_xpath(context, "//div[@class='AuthLoginInputToggle-wrapper']//button[1]").click()


@when("I go to login page")
def step_impl(context):
    find_by_class(context, "PSHeader-NoLoginButton").click()


@step("I enter stranger's email (?P<email>.+)")
def step_impl(context, email):
    find_by_id(context, "passp-field-login").send_keys(email)


@step("I enter (?P<something>.+) which is not user's password")
def step_impl(context, something):
    find_by_id(context, "passp-field-passwd").send_keys(something)


@when("I click on my profile picture")
def step_impl(context):
    find_by_xpath(context, "//div[contains(@class, 'PSHeader-User')]").click()


@step("Click on LogOut")
def step_impl(context):
    find_by_xpath(context, "//a[contains(@class, 'legouser__menu-item_action_exit')]").click()


@then("I should not see user's Inbox page")
def step_impl(context):
    sleep(5)
    WebDriverWait(context.browser, 10).until(EC.title_contains("Почта"))
    assert (context.browser.title.find("Входящие") == -1)
