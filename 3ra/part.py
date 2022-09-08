import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
#modelo para selenium
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search(self):
        driver = self.driver
        #Pagina 
        driver.get("https://www.google.com")
        self.assertIn("Google",driver.title)
        elemento = driver.find_element(By.NAME, "q")

        elemento.send_keys("selenium")
        elemento.send_keys(Keys.RETURN)
        time.sleep(5)

        assert "No se enocntro el elmento:" not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()