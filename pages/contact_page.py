import utilities.custom_logger as cl
from base.basepage import BasePage
import logging

class ContactPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # methods
    def hoverContactIcon(self, icon="Resume"):
        """
        Hover over an icon in the contact section
        :param icon: a string containing the title of an icon
        :return:
        """
        self.elementHover(locator="//img[@alt='" + icon + "']//parent::a", locatorType="xpath")

    def clickContactIcon(self, icon="Resume"):
        """
        Clicking an icon in the contact section
        :param icon: a string containing the title of an icon
        :return:
        """
        self.elementClick(locator="//img[@alt='" + icon + "']//parent::a", locatorType="xpath")

    def scrollToContactSection(self):
        """
        Scroll to the contact section
        :return:
        """
        self.scrollFindElement("Contact Me")

    def verifyContactIconOpacity(self, icon="Resume", hover=False):
        """
        Verify the icons in the contact section have a proper opacity
        :param icon: a string containing the title of an icon
        :param hover: a bool that is true if hovering over an icon
        :return:
        """
        iconOpacity = self.getCSSValue(property="opacity", locator="//img[@alt='" + icon + "']",
                                       locatorType="xpath")
        if hover:
            if (iconOpacity == '0.3'):
                return True
            else:
                return False
        else:
            if (iconOpacity == "1"):
                return True
            else:
                return False

    def verifyPageOpenAfterClick(self, icon="Resume"):
        """
        Verify that the correct page is open
        :param icon: a string containing the title of an icon
        :return:
        """
        self.driver.switch_to.window(self.driver.window_handles[1])
        result = False

        if icon == "Resume":
            result = self.isElementPresent(locator="/html/head/title",
                                           locatorType="xpath")
        elif icon == "Work Experience":
            result = self.isElementPresent(locator="//title[contains(text(),'20592644_wtr.pdf')]",
                                           locatorType="xpath")
        else:
            result = self.isElementPresent(locator="//img[@alt='LinkedIn']", locatorType="xpath")

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return result