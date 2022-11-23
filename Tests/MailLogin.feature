# Created by grigory at 23/11/2022
Feature: MailLogin
  # In order to use the mail service, a registered user must be able
  # to log in with his account

  Scenario: LoginRegistered
    Given I'm on the mail login page
    When I enter user's email
    And I press next
    And I enter user's password
    And I click on login button
    Then I should see user's Inbox page

#  todo close browser

  Scenario: LoginStranger
    Given I'm on the mail login page
    When I enter stranger's email
    And I press next
    Then I should see NoUserExists message

  #  todo close browser

  Scenario: LoginRegisteredWrongPass
    Given I'm on the mail login page
    When I enter user's email
    And I press next
    And I enter something but not user's password
    And I click on login button
    Then I should see WrongPassword message

  #  todo close browser
