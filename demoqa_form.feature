Feature: Fill Form on DemoQA
    Scenario: Fill Correct input on Automation Practice Form
        Given Launch chrome browser
        When I go to automation practice form
        And I fill the First Name and Last Name
        And I fill the Email
        And I fill the mobile number
        And I choose gender randomly
        And I choose DOB randomly
        And I pick any subject randomly
        And I tick any hobbies randomly
        And I upload my profile picture
        And I type my current address
        And I choose my State and my City
        And I click Submit button
        Then Verify that