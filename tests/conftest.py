import os.path
import time
import pytest
import pytest_html
from selenium import webdriver
#
driver = None


# bellow is the main setup and teardown fixture for launching a url page with any of the 3 browsers below.
@pytest.fixture(autouse=True)
def setup(request, browser, url):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


# allows me to run the tests in the command line and choose which browser and url to be used.
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")


# allows me to run the tests in the command line and choose which browser to be used.
@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


# allows me to run the tests in the command line and choose which url to be used.
@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")


# allows me to generate html reports and take a screenshot in case of test failure.
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url("http://www.collectedmagazine.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = str(int(round(time.time() * 1000))) + ".png"
            # file_name = report.nodeid.replace("::", "_") + ".png"
            destination_file = os.path.join(report_directory, file_name)
            driver.save_screenshot(destination_file)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extras.append(pytest_html.extras.html(html))
        report.extras = extras


#  changes the title of my generated reports.
def pytest_html_report_title(report):
    report.title = "Collected Magazine Automation Report"
