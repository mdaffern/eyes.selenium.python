import pytest
from selenium.webdriver.common.by import By

from applitools.target import Target


@pytest.mark.skip("Depending on Fluent API. Not implemented yet")
def test_wix_site(eyes, driver):
    eyes.match_timeout = 0
    eyes.force_full_page_screenshot = False
    driver = eyes.open(driver, app_name="Wix", test_name="Wix example")
    # Sign in to the page
    driver.get("https://eventstest.wixsite.com/events-page-e2e/events/ba837913-7dad-41b9-b530-6c2cbfc4c265")
    iframe_id = "TPAMultiSection_j5ocg4p8iframe"
    driver.switch_to().frame(iframe_id)
    # click register button
    driver.find_element(By.CSS_SELECTOR, "[data-hook=get-tickets-button]").click()
    # add one ticket
    driver.find_element(By.CSS_SELECTOR, "[data-hook=plus-button]").click()
    # just an example, where it make us some problems with scrolling to top of the frame.
    # eyes.check_region(By.CSS_SELECTOR, "[data-hook=plus-button]");
    eyes.check("", Target.region(By.CSS_SELECTOR, "[data-hook=plus-button]"))
    eyes.close()