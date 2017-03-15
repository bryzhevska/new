Feature: Admin functionality
  In order to manage system
  As an admin
  I should have admin access


  Scenario: Admin impersonate as publisher
    Given I am signed in as admin
    When I impersonate as publisher
    Then I should see system as publisher