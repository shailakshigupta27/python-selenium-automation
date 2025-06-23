Feature: Tests for Target App page

  Scenario: User is able to open Privacy Policy
    Given Open Target App page
    And Store original window
    When Click Privacy Policy link
    And Switch to new window
    Then Verify Privacy Policy page opened
    And Close current page
    And Return to original window

  Scenario: User is able to open Terms Conditions
    Given Open Target App page
    And Store original window
    When Click Target Terms Condition link
    And Switch to new window
    Then Verify Terms Condition page opened
    And Close current page
    And Return to original window