import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BaseTest(unittest.TestCase):

    def setUp(self):
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path = PATH)
        driver = self.driver
        driver.get("https://www.consumeraffairs.com/recalls/liberty-mountain-recalls-birdie-belay-devices-032921.html")
        self.assertIn("Liberty Mountain recalls Birdie Belay devices", driver.title)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()