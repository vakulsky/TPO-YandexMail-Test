# Created by grigory at 23/11/2022
Feature: MailLogin
  # In order to use the mail service, a registered user must be able
  # to log in with his account

  Scenario: RegisteredLogin
    Given I'm on the mail page
    When I go to login page
    And I select email as login type
    And I enter user's email
    And I click on login button
    And I enter user's password
    And I click on login button
    Then I should see user's Inbox page


  Scenario Outline: LoginStranger
    Given I'm on the mail page
    When I go to login page
    And I select email as login type
    And I enter stranger's email <email>
    And I click on login button
    Then I should see NoUserExists message

    Examples:
      |email  |
      |exalebnle94p95b9mple|


  Scenario Outline: LoginRegisteredWrongPass
    Given I'm on the mail page
    When I go to login page
    And I select email as login type
    And I enter user's email
    And I click on login button
    And I enter <something> which is not user's password
    And I click on login button
    Then I should see WrongPassword message

    Examples:
    |something|
    |12345678 |
