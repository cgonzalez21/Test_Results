import unittest

from selenium.webdriver.support.expected_conditions import url_changes, url_contains
from tests.base_test import BaseTest
from urllib.parse import urlparse
from pages.main_page import *
from utils.test_cases import test_cases

class TestFooterSection(BaseTest):

    def test_page_load(self):
        print("\n" + str(test_cases(0)))
        page = MainPage(self.driver)
        self.assertTrue(page.check_page_loaded())

    def test_search_footer_first_desc(self):
        print("\n" + str(test_cases(1)))
        page = MainPage(self.driver)
        search_result = page.search_footer_first_desc()
        self.assertIn('ConsumerAffairs is not a government agency. Companies displayed may pay us to be Authorized or when you click a link, call a number or fill a form on our site. Our content is intended to be used for general information purposes only. It is very important to do your own analysis before making any investment based on your own personal circumstances and consult with your own investment, financial, tax and legal advisers.', search_result)
   

    def test_search_footer_second_desc(self):
        print("\n" + str(test_cases(2)))
        page = MainPage(self.driver)
        search_result = page.search_footer_second_desc()
        self.assertIn('Copyright © 2021 Consumers Unified LLC. All Rights Reserved. The contents of this site may not be republished, reprinted, rewritten or recirculated without written permission.', search_result)

    def test_search_footer_contact_us(self):
        print("\n" + str(test_cases(3)))
        page = MainPage(self.driver)
        search_result = page.search_footer_contact_us()
        self.assertIn('Contact Us', search_result)

    def test_search_footer_faq(self):
        print("\n" + str(test_cases(4)))
        page = MainPage(self.driver)
        search_result = page.search_footer_faq()
        self.assertIn('FAQ', search_result)

    def test_search_footer_terms_of_use(self):
        print("\n" + str(test_cases(5)))
        page = MainPage(self.driver)
        search_result = page.search_footer_terms_of_use()
        self.assertIn('Terms of Use', search_result)

    def test_search_footer_privacy_policy(self):
        print("\n" + str(test_cases(6)))
        page = MainPage(self.driver)
        search_result = page.search_footer_privacy_policy()
        self.assertIn('Privacy Policy', search_result)

    def test_search_footer_ca_privacy_notice(self):
        print("\n" + str(test_cases(7)))
        page = MainPage(self.driver)
        search_result = page.search_footer_ca_privacy_notice()
        self.assertIn('CA Privacy Notice', search_result)

    def test_find_my_match_with_valid_zip_code(self):
        print("\n" + str(test_cases(8)))
        page = MainPage(self.driver)
        page.search_find_my_match('74119')
        result = page.click_find_my_match_button()
        self.assertEqual("https://my.consumeraffairs.com/home-warranty/?element_label=in_content_mt_cta&zip=74119", result)

    def test_find_twitter_link(self):
        print("\n" + str(test_cases(9)))
        page = MainPage(self.driver)
        result = page.click_twitter_button()
        self.assertEqual("https://twitter.com/intent/tweet/?text=Liberty%20Mountain%20recalls%20Birdie%20Belay%20devices&via=ConsumerAffairs&url=https://www.consumeraffairs.com/recalls/liberty-mountain-recalls-birdie-belay-devices-032921.html", result)

    def test_find_facebook_link(self):
        print("\n" + str(test_cases(10)))
        page = MainPage(self.driver)
        result = page.click_facebook_button()
        self.assertIn("https://www.facebook.com/login.php", result)

    def test_related_news(self):
        print("\n" + str(test_cases(11)))
        page = MainPage(self.driver)
        self.assertFalse(page.click_first_related_news())