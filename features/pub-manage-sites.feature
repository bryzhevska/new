Feature: In order to keep statistivs
  As a publisher
  I should be able to manage sites

  Scenario: Add new site
    Given I am logged in as publisher
    When I add site to the system
    Then Site should be added on sites page
    And Site should be visible in site list