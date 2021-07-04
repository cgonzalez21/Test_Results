from selenium.webdriver.common.by import By

class PageLocators(object):
    TITLE = (By.CLASS_NAME, 'artcl__tlt')
    FOOTER = (By.CSS_SELECTOR, 'footer[class="ca-ft"]')
    FIRST_DESC = (By.CSS_SELECTOR, 'div.ca-ft__ctnt p:first-child')
    SECOND_DESC = (By.CSS_SELECTOR, 'div.ca-ft__ctnt p:nth-of-type(2)')
    CONTACT_US_BUTTON = (By.CSS_SELECTOR, 'div.ca-ft__list a:first-child')
    FAQ_BUTTON = (By.CSS_SELECTOR, 'div.ca-ft__list a:nth-of-type(2)')
    TERMS_OF_USE_BUTTON = (By.CSS_SELECTOR, 'div.ca-ft__list a:nth-of-type(3)')
    PRIVACY_POLICY_BUTTON = (By.CSS_SELECTOR, 'div.ca-ft__list a:nth-of-type(4)')
    CA_PRIVACY_NOTICE_BUTTON = (By.CSS_SELECTOR, 'div.ca-ft__list a:nth-of-type(5)')
    ZIP_CODE_INPUT = (By.CSS_SELECTOR, 'input[class="ca-mt-zip__input ca-form__input ca-form__input--alt"]')
    FIND_MY_MATCH_BUTTON = (By.CSS_SELECTOR, 'div.wzrd-wg__form-wpr > button[class="ca-mt-zip__btn ca-btn ca-btn--thrd gtm-mt-entrance wzrd-wg__link"]')
    MATCH_SECTION = (By.CSS_SELECTOR, 'div[class="h-sect"]')
    TWITTER_BUTTON = (By.CSS_SELECTOR, 'div.ca-authr a:nth-of-type(2)')
    FACEBOOK_BUTTON = (By.CSS_SELECTOR, 'div.ca-authr a:nth-of-type(1)')
    FIRST_RELATED_NEWS_BUTTON = (By.XPATH, '//nav[@class="h-sect--pad-2 h-coll-vert article-links related-links"]//a')
    LAST_RELATED_NEWS_BUTTON = (By.CSS_SELECTOR, 'nav.h-sect--pad-2.h-coll-vert.article-links.related-links a')
