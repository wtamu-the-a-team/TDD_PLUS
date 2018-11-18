CONTENTS OF THIS FILE
----------------------
* Introduction
* Requirements
* Project File
* Credits & Contact



Introduction
-----------------
The TDD++ Maintenance project is a manipulation of a simple ABET application form where our code tests simple CRUD (Create, Remove, Update, Delete). We'll adjust Program Educational Objectives and performs the following functions:
    - Add
    - Remove
    - Validate all data in successful form
    - Assert on invalid data in form
    - Assert if no applications exist (DB empty)
    - Retrieve and edit application with validation after manipulation
	

User Stories- Gherkin Notation
-------------------------------

* Selenium Test Cases

Feature: User desires to view existing application (Read and Show Stored Application)
Scenario: 
	User has an existing application stored
	Given the user has a login profile
	And the username and password are correct
	When the user select an application
	The application details are displayed to the user


Feature: Application is stored to database (Add Complete Application) 
Scenario:
	User fills out application
	Given Submit button is clicked on application
	When the form passes all required field validation
	The program will create a record in database with the data from the application


Feature: Application failed to be stored (Fail Adding Incomplete Application)
Scenario:
	User fills out application
	Given submit button is clicked on application
	When the form validation finds an input error
	The program will not store the application 
	And notify the user of the input error

* Functional Test cases

Feature: Add functionality executing correctly (Add Application)
Scenario: 
	Given application was submitted	
	When a new application object is created
	And all data is saved to the database
	The application will be redirected to the details page
	And print “Pass” to the console

Feature: Delete functionality executing correctly (Delete Application)
Scenario:
	Given the application delete button is clicked
	When the application record has been removed from the database
	The application will be redirected to the list of applications created by the user
	And print “Pass” to the console

Feature: Edit functionality executing correctly (Edit Application)
Scenario:
	Given the application is submitted form the edit page
	When the object is retrieved 
	And all fields are saved to the existing record
	The application will be redirected to the details page
	And print “Pass” to the console

Feature: Read functionality executing correctly (Read Application)
Scenario:
Given the application details page is redirected to
	When the object is retrieved 
	And all the data is stored to a variable
	And the variable is rendered to the details page
	The data will be displayed on the details page
	And print “Pass” to the console

* Functional Test cases Non CRUD Related

Feature: (Check Database NO entries)
Scenario:
	Given test method to check database entries is called
	When the method finds no entries
	The method will print “Pass” to the console		

Feature: (Test URL POST Routing)
Scenario:
	Given a new application was submitted
	When the post method directs to the correct URL method
	The method will print “Pass” to the console

Feature: (Test URL GET Routing)
Scenario:
	Given an existing application was selected from the list
	When the get method is called on
	The method will print “Pass” to the console

Feature: (Test Retrieve Invalid Application)
Scenario:
	Given an application is selected for viewing
	When the id of the record retrieved does not match the id of the application selected
	The method will print a notification to the console

Feature: (Test Failing Duplicate Application Add)
Scenario:
	Given an application has been submitted
	When a duplicate application is added to the database
	The method will print a notification to the console
	
	
Requirements
-----------------
This project requires the following software:
Python 3.6 and Programming
Django v1.11
The Firefox web browser
The GIT version control system
A virtualenv with Python 3, Django 1.11, and Selenium 3 in it


Project File
----------------
All our project files are available for download from our GitHub repository:
https://github.com/wtamu-the-a-team/TDD_PLUS/tree/TDD_PLUS_PLUS_SB



Credit & Contact
-------------------
Credit:
We are particularly grateful to Harry J.W. Percival, the author of Test-Driven Development with Python, who makes his book available online for free. The online material is easy to read and it covers a wealth of material.

Current maintainers:
* Jeremy DeBerg
* Flo Indriyani
* Jose Dominguez
* Scott Johnson 
