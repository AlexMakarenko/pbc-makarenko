from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


def test_search(grid):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Remote(
        command_executor="http://192.168.33.10:5555/wd/hub",
        desired_capabilities={"browserName": "firefox"},
        options=options
    )
    try:
        driver.get("http://www.python.org")
        driver.save_screenshot('python.png')
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        driver.save_screenshot('pycon.png')
        driver.get("http://www.python.org")
        assert "No results found." not in driver.page_source
    except Exception as a:
        print a.message
        raise a
    finally:
        print 'close'
        driver.close()
