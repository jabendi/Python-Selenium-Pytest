# Python-Selenium-Pytest

Tools used: 
Programming language: Python
Automation tool: Selenium
Testing Framework: Pytest. 
I.D.E: PyCharm(primary) and Visual Studio Code.

Info: 
This project consists of a test automation framework I created for my partner's blog website: https://collectedmagazine.com. I have followed a Page Object Model design structure(POM) that creates an object repository for storing all web elements. It helps reduce code duplication and improves test case maintenance. 

Each web page of an application is a class file. Each class file will contain only corresponding web page elements. Using these elements, I can perform operations on the blog/website under test.

Structure and organization:

The automation framework includes various Directories and Packages. I have organized and structured the project into the following:

Base - This package contains some foundational components and utilities that are shared across multiple test cases or modules. 2 "wait" class functions have been created to handle waiting requests for the page web elements to avoid exception errors in PyCharm.

data - This package is currently empty due to this project being "simple" and not requiring such, currently. Should I expand with more test cases, for example: more search-related tests, then I can create test data files, such as JSON, CSV, or Excel files, to make it easier to manage and update test data independently.

logs - This directory is where the log files are stored, making it easier to manage and access logs alongside other project files.

pages - This package contains page object classes that represent the web pages my tests interact with. Each page object class is responsible for the behaviour and elements of each specific page. There are 2 pages created here: 1-collected_home_page and 2-search_page. The 1st page is the home page of the blog with several interactable web elements. The 2nd page is where the search box functionalities reside. 


reports - This directory contains HTML reports generated by the test framework after test execution. Plugins used and installed: pytest-html 4.1.1.

screenshots - This directory stores screenshots captured during test execution, especially when tests fail. I have set up the framework to take screenshots only when tests fail. This can help debug and investigate test failures.

tests: Includes 8 simple automated tests I created for the following blog: https://collectedmagazine.com. Each of the tests focuses on testing a specific feature or scenario.
Tests are written using Selenium and Pytest's syntax. All tests can be classed as Functional. This is where the "conftest" file is located, which serves as a central location for sharing fixtures, hooks, and other configurations across multiple test files within the same directory or package. The "conftest" is where I have set up the "setup" fixture which is responsible for initializing Selenium's Webdriver, which launches the browser/homepage for each specific test case, and then proceeds with the respective fixture teardown.

utilities - This package contains utility modules that provide commonly used functions and constants across my test suite. Common utilities may include configuration management, helper functions, and constant values, which help reusability and maintainability. This is where my custom logger function is located, which allows the tests to be logged and stored in the project.

