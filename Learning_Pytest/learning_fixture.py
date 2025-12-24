#Description of fixture
# A fixture is a function that is run before each test case to set up any state or context needed for the tests.For example before running a test case we want to open a browser and navigate to a specific URL.
# After the test case is done we want to close the browser.
#We can also write what to do after the test case is done using yield keyword in fixture.

#Syntax to create fixture
import pytest


@pytest.fixture()
def setup():
    #code to set up the test environment
    print("Opening Browser")
    yield
    #code to tear down the test environment
    print("Closing Browser")

# Or watch video 266  of udemy's course of my testing