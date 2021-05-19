Feature: Test navigation between pages
  
  Scenario: Homepage can go to Login page
    Given I am on the homepage
    When I click on sign in button
    Then I am on the login page
