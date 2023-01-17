Feature:Check if the user can successfully logout
  After i Login
  I want to see a message and logout btn
  so i can logout

  Scenario: Logout Successfully
    Given The user in logged into the application
    When the user clicks logout btn
    Then the user is redirected to Login page