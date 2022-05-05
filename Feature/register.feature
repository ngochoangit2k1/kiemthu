Feature: Test the viblo application
  Scenario: Verify Home Page
    Given Launch the browser
    Then verify the page title
    And close the browser

  Scenario: Verify registration function
    Given Launch the App1
    When enter registration credentials1
    Then click register
    Then verify the page title and screenshot1
    And close the App1
