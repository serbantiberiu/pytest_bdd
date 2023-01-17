Feature: Check if i can Login
  As a visitor of the page,
  I want to introduce user and password,
  So i can login

  Scenario: Login successfully
    Given Open LoginPage
    When The user inserts credentials and clicks login button
    Then Login is successful
