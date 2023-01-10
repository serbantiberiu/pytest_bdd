Feature:Check if Login Succesfully
  After i Login
  I want to see a message and logout btn
  so i can logout

  Scenario : Login Succesfully
    Given Open Securepage
    When Find succes message
    When Click logout btn
    Then Redirect to Loginpage