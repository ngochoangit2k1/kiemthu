Feature: Test the viblo application
  Scenario: Verify Home Page
    Given Launch the browser
    Then verify the page title
    And close the browser

  Scenario: Verify login functionality
    Given Launch  the App
    When enter   login credentials
    Then click   login
#    Then click logout
    Then verify   the   page title and screenshot
    And close  the App
