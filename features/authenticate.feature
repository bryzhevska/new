Feature: Authenticate
  In order to use system
  As a publisher
  I should be able to authenticate

  #Scenario: Sign up
   # Given I am unregistered user
    #When I sign up to the system
    #Then I should be signed up successfully

  Scenario Outline: Sign in
    Given I am registered "<user>"
    When I sign in to system as "<user>"
    Then I should be signed in as "<user>" successfully
    Examples:
      | user      |
      | admin     |
    #  | publisher |
@si
  Scenario: Sign out
    Given I am signed in to system as "admin"
    When I signed out from the system
    Then I should be signed out successfully


  #Scenario: Forgot password
   # Given I am registered user
   # When I forgot password
   # And I follow restore password instructions
   # Then I should get my new password
