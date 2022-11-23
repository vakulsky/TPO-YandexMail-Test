from behave import *

use_step_matcher("re")


@step("I've just received message with some unique subject (?P<subject>.+)")
def step_impl(context, subject):
    """
    :type context: behave.runner.Context
    :type subject: str
    """
    raise NotImplementedError(u'STEP: And I\'ve just received message with some unique subject <subject>')


@when("I select message with subject (?P<subject>.+)")
def step_impl(context, subject):
    """
    :type context: behave.runner.Context
    :type subject: str
    """
    raise NotImplementedError(u'STEP: When I select message with subject <subject>')


@step("Click on Delete button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Click on Delete button')


@step("Click on Refresh button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Click on Refresh button')


@then("I should not see message with subject (?P<subject>.+)")
def step_impl(context, subject):
    """
    :type context: behave.runner.Context
    :type subject: str
    """
    raise NotImplementedError(u'STEP: Then I should not see message with subject <subject>')