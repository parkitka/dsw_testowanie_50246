Feature: Login
  Scenario Outline: Successful Login
    Given I am on the login page
    When I submit login credentials with email '<email>' and password '<password>'
    Then I am logged in successfully

  Examples:
    |       email       |  password  |
    | eve.holt@reqres.in | cityslicka |

  Scenario: Unsuccessful Login
    Given I am on the login page
    When I submit login credentials with email 'invalid@email.com' and password 'wrongpassword'
    Then I am not logged in
