Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open target.com
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown


