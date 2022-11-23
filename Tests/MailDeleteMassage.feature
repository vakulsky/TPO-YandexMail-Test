# Created by grigory at 23/11/2022
Feature: MailDeleteMassage
  # An authorized user should be able to delete unwanted messages

  Scenario Outline: DeleteMessage
    Given I'm authenticated user on inbox page
    And I've just received message with some subject <subject>
    When I sync messages
    And I select message with subject <subject>
    And Click on Delete button
    And I sync messages
    Then I should not see message with subject <subject>

    Examples:
      | subject      |
      | unique subject |
