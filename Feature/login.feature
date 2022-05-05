Feature: Test the c2ta application
  Scenario: Verify Home Page
    Given Launch the browser
    Then verify the page title
    And close the browser

  Scenario: Verify login functionality
    Given Launch the App
    When enter login credentials
    Then click login
    Then verify the page title and screenshot
    And close the App
