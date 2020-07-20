import utilities.custom_logger as cl
from base.basepage import BasePage
import logging

class NavigationBar(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _me_profile = "Me"
    _projects = "Projects"
    _interests = "Interests"
    _contact = "Contact"

    # methods
    def clickNavigationLink(self, link="Me", dropdown=False):
        """
        Method to click a link on the navigation bar
        :param link: a string for the navigation link
        :param dropdown: a bool to indicate if the dropdown is visible
        :return:
        """
        locator = ""
        if (link == 'Contact'):
            locator = self._contact
        elif (link == 'Projects'):
            locator = self._projects
        elif (link == 'Interests'):
            locator = self._interests
        else:
            locator = self._me_profile

        if dropdown:
            self.elementClick(locator="//ul[@class='options']//a[contains(text(),'" + locator + "')]",
                              locatorType="xpath")
        else:
            self.elementClick(locator="//nav//a[contains(text(),'" + locator + "')]", locatorType="xpath")

    def clickBurgerIcon(self):
        """
        Method to click the burger icon
        :return:
        """
        self.elementClick(locator="dropdown_icon", locatorType="id")

    def resizeWindowToShowBurgerIcon(self):
        """
        Method to resize the window to display the burger icon
        :return:
        """
        self.resizeWindow(960,700)

    # methods that verify whether the navigation is successful
    def verifyNavigateToMyProfile(self):
        """
        Method to verify whether the navigation to my profile section is successful
        :return: bool
        """
        result = self.isElementPresent(locator="//img[@alt='Ray Nugroho']", locatorType="xpath")
        return result

    def verifyNavigateToProjects(self):
        """
        Method to verify whether the navigation to project section is successful
        :return: bool
        """
        result = self.isElementPresent(locator="//h1[contains(text(), 'Projects')]", locatorType="xpath")
        return result

    def verifyNavigateToInterests(self):
        """
        Method to verify whether the navigation to interest section is successful
        :return: bool
        """
        result = self.isElementPresent(locator="//h1[contains(text(), 'Interests')]", locatorType="xpath")
        return result

    def verifyNavigateToContact(self):
        """
        Method to verify whether the navigation to contact section is successful
        :return: bool
        """
        result = self.isElementPresent(locator="//h1[contains(text(), 'Contact Me')]", locatorType="xpath")
        return result

    def verifyNavigationBarPresent(self):
        """
        Method to verify whether the navigation bar is present after the navigation
        :return: bool
        """
        result = self.isElementPresent(locator="header_container", locatorType="class")
        return result

    def verifyBurgerIconDisplayed(self):
        """
        Method to verify whether the burger icon is displayed
        :return: bool
        """
        result = self.isElementDisplayed(locator="dropdown_icon", locatorType="id")
        return result

    def verifyDropDownMenuDisplayed(self):
        """
        Method to verify whether the dropdown menu is displayed
        :return:
        """
        attribute = self.getElementAttribute(attribute="style", locator="dropdown_menu", locatorType="id")
        if attribute == "top: 58px;":
            return True
        else:
            return False
