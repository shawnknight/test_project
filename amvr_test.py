import unittest
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class amvr(unittest.TestCase):
    def setUp(self):
        ''' self.driver = WebDriver() '''
        self.username = os.environ['SAUCE_USERNAME']
        self.key = os.environ['SAUCE_ACCESS_KEY']
        hub_url = "%s:%s@localhost:4445" % (self.username, self.key)
        self.driver = webdriver.Remote(desired_capabilities=self.caps, command_executor="http://%s/wd/hub" % hub_url)    
        self.waiting = WebDriverWait(self.driver, 30)
    
    def test_amvr(self): 
        driver = self.driver
        waiting = self.waiting
        
        driver.get("https://apps.tn.gov/amvr-app/login.html")
        
        waiting.until(expected_conditions.title_is("Log In - Motor Vehicle Records Search"))
        username_textbox = waiting.until(expected_conditions.visibility_of(driver.find_element_by_id("username")))
        password_textbox = waiting.until(expected_conditions.visibility_of(driver.find_element_by_id("password")))
        login_button = waiting.until(expected_conditions.visibility_of(driver.find_element_by_name("login")))
        
        waiting.until(expected_conditions.title_is("Log In - Motor Vehicle Records Search"))
        self.assertIn("amvr-app/login.html", driver.current_url, "Failed to login")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
