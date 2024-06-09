Feature: Create User
  Scenario Outline: Create a new user
    Given I am on the user creation page
    When I submit user data with name "<name>" and job "<job>"
    Then The user is created successfully
    And I display the user ID, name, and job

    Examples:
      | name | job  |
      | krz  | chu  |