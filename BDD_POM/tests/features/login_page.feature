Feature: Check if i can Login
  As a visitor of the page,
  I want to introduce user and password,
  So i can login

  Scenario: Login succesfully
    Given Open LoginPage
    When Introduce user
    When Introduce password
    When Click Login button
    Then Login succesfully
