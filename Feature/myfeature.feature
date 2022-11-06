 Feature: SQEMYFEATURE
Scenario Outline: Admin is able to create a new User
   Given Chrome Browser is launched and the URL for Metabase
   And The URL http: // localhost: 3000 / is in Use
   When I enter email as "<adminUser>" And password as "<Password>"
   And I click on Sign In
   Then I shall be Logged in as Admin User
   And I click on the Settings Button
   And I click on Admin Settings
   And i click on People
   And I click on Invite Someone Button
   And I enter First Name as "<first_Name>"
   And I enter Last Name as "<last_Name>"
   And I enter Email as "<email>"
   And I click on create
   And i click on Done
   Then a new User will be created

 Examples:
 | adminUser | Password | first_Name | last_Name | email |
 | saadankhokhar21@gmail.com | Saadan@123 | Saadan | Khokhar | saadankhokhar21@gmail.com |