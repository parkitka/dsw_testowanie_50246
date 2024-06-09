Feature: Register
  Scenario Outline: Register User
    Given I am on the registration page
    When I submit registration data with email "<email>" and password "<password>"
    Then I am registered successfully
    And I display the user ID and token
    And User email is "<email>"
    And User password is "<password>"

    Examples:
      |        email         | password |
      | eve.holt@reqres.in   |  pistol  |
