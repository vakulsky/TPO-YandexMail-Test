# Created by grigory at 23/11/2022
Feature: MailSend
  # An authorized user should be able to send and receive messages

  Scenario Outline: SendToSelf
    Given I'm authenticated user on inbox page
    When I click on Write button
    And I fill Email field with user's email
    And I fill Subject field with <subject>
    And I fill Body field with <body>
    And Click Send button
	And I navigate to Sent messages
	Then I should see new message with subject <subject>
	And I navigate to Inbox messages
	And I should see new message with subject <subject>

    Examples:
      |subject       | body    |
      | some subject |some body|

  #  todo close browser

  Scenario Outline: SendWithDelay
    Given I'm authenticated user on inbox page
    When I click on Write button
    And I fill Email field with user's email
    And I fill Subject field with <subject>
    And Click Delay button
	And Fill time field with <time>
    And Click Save button
    And Click Send button
    And I navigate to Outbox messages
	Then I should see a message with subject <subject> and delayed time <time>

    Examples:
      |subject       | time  |
      | some subject | 19:00 |

  #  todo close browser
