Feature: Test the viblo application
  Scenario: Verify Home Page
    Given Launch the browser
    Then verify the page title
    And close the browser

  Scenario: Verify registration function
    Given Launch the App111
    When enter registration credentials111
    Then verify the page title and screenshot111
    And close the App111


