from logging import FATAL
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pages.matched_page import MatchedPage
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from utils.locators import *


class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = PageLocators
        super(MainPage, self).__init__(driver)

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.TITLE) else False

    def search_footer_first_desc(self):
        element = self.find_element(*self.locator.FOOTER)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        return self.find_element(*self.locator.FIRST_DESC).text

    def search_footer_second_desc(self):
        element = self.find_element(*self.locator.FOOTER)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        return self.find_element(*self.locator.SECOND_DESC).text

    def search_footer_contact_us(self):
        element = self.find_element(*self.locator.FOOTER)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        return self.find_element(*self.locator.CONTACT_US_BUTTON).text

    def search_footer_faq(self):
        element = self.find_element(*self.locator.FOOTER)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        return self.find_element(*self.locator.FAQ_BUTTON).text

    def search_footer_terms_of_use(self):
        element = self.find_element(*self.locator.FOOTER)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        return self.find_element(*self.locator.TERMS_OF_USE_BUTTON).text

    def search_footer_privacy_policy(self):
        element = self.find_element(*self.locator.FOOTER)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        return self.find_element(*self.locator.PRIVACY_POLICY_BUTTON).text

    def search_footer_ca_privacy_notice(self):
        element = self.find_element(*self.locator.FOOTER)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        return self.find_element(*self.locator.CA_PRIVACY_NOTICE_BUTTON).text

    def search_find_my_match(self, zip):
        element = self.find_element(*self.locator.MATCH_SECTION)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.find_element(*self.locator.ZIP_CODE_INPUT).send_keys(zip)

    def click_find_my_match_button(self):
        time.sleep(5)
        self.find_element(*self.locator.FIND_MY_MATCH_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.get_url()

    def click_twitter_button(self):
        self.find_element(*self.locator.TWITTER_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.get_url()

    def click_facebook_button(self):
        time.sleep(5)
        self.find_element(*self.locator.FACEBOOK_BUTTON).click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.get_url()

    def click_first_related_news(self):
        try:
            element = self.find_element(*self.locator.FIRST_RELATED_NEWS_BUTTON)
            if(element.len() > 0):
                return True
        except NoSuchElementException:
            return False

    def click_last_related_news(self):
        try:
            element = self.find_element(*self.locator.LAST_RELATED_NEWS_BUTTON)
            if(element.len() > 0):
                return True
        except NoSuchElementException:
            return False