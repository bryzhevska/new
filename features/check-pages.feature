Feature: Check pages availability
  In order to use system
  As a registered publisher
  All pages should be available for me

  Scenario Outline: Browse pages
    Given I am logged in as a  publisher
    When I open "<page>"
    Then "<page>" should be available
    Examples:
      | page            |
      | total dashboard |
      | statistics      |
      | sites           |