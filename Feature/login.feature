Feature: Test the c2ta application
#  Feature: Test the c2ta application
#  Scenario: Verify Home Page
#    Given Launch the browser
#    Then verify the page title
#    And close the browser
#
#  Scenario: Verify login functionality
#    Given Launch the App
#    When enter login credentials
#    Then click login
#    Then verify the page title and screenshot
#    And close the App



  Scenario: Verify Home Page
    Given Launch the browser
    Then verify the page title
    And close the browser

  Scenario: Verify login functionality
    Given Launch the App
    When enter key to input login credentials and click button
    Then verify the page title and screenshot
    And close the App
