from pages.navigation_bar import NavigationBar
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.util as util

@pytest.mark.usefixtures("oneTimeSetup", "setUp")
class NavigationTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        """
        Run the setup before the test starts
        :return:
        """
        self.navigation = NavigationBar(self.driver)
        self.ts = TestStatus(self.driver)
        self.util = util.Util()

    @pytest.mark.run(order=4)
    def test_navigateToMyProfile(self):
        """
        Test the navigation process to my profile
        :return:
        """
        self.navigation.clickNavigationLink(link="Me", dropdown=False)
        result_navigation = self.navigation.verifyNavigateToMyProfile()
        self.ts.mark(result_navigation, "Reached my profile section")
        result_navigationBar = self.navigation.verifyNavigationBarPresent()
        self.ts.markFinal("test_navigateToMyProfile", result_navigationBar, "Navigation bar was present")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=1)
    def test_navigateToProjects(self):
        """
        Test the navigation process to the project section
        :return:
        """
        self.navigation.clickNavigationLink(link="Projects", dropdown=False)
        result_navigation = self.navigation.verifyNavigateToProjects()
        self.ts.mark(result_navigation, "Reached projects section")
        result_navigationBar = self.navigation.verifyNavigationBarPresent()
        self.ts.markFinal("test_navigateToProjects", result_navigationBar, "Navigation bar was present")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=2)
    def test_navigateToInterests(self):
        """
        Test the navigation process to the interest section
        :return:
        """
        self.navigation.clickNavigationLink(link="Interests", dropdown=False)
        result_navigation = self.navigation.verifyNavigateToInterests()
        self.ts.mark(result_navigation, "Reached interests section")
        result_navigationBar = self.navigation.verifyNavigationBarPresent()
        self.ts.markFinal("test_navigateToProjects", result_navigationBar, "Navigation bar was present")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=3)
    def test_navigateToContact(self):
        """
        Test the navigation process to the contact section
        :return:
        """
        self.navigation.clickNavigationLink(link="Contact", dropdown=False)
        result_navigation = self.navigation.verifyNavigateToContact()
        self.ts.mark(result_navigation, "Reached contact section")
        result_navigationBar = self.navigation.verifyNavigationBarPresent()
        self.ts.markFinal("test_navigateToContact", result_navigationBar, "Navigation bar was present")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=5)
    def test_burgerIconDisplayed(self):
        """
        Test the burger icon is displayed when the window is minimized
        :return:
        """
        self.navigation.resizeWindowToShowBurgerIcon()
        self.util.sleep(sec=3)
        result_burgerIcon = self.navigation.verifyBurgerIconDisplayed()
        self.ts.markFinal("test_burgerIconDisplayed", result_burgerIcon, "Burger icon was displayed")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=5)
    def test_clickBurgerIcon(self):
        """
        Test clicking the burger icon displays a dropdown containing the navigation links
        :return:
        """
        self.navigation.resizeWindowToShowBurgerIcon()
        self.util.sleep(sec=3)
        self.navigation.clickBurgerIcon()
        result_dropDown = self.navigation.verifyDropDownMenuDisplayed()
        self.ts.markFinal("test_clickBurgerIcon", result_dropDown, "Dropdown displayed")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=6)
    def test_clickDropdownOptions(self):
        """
        Test clicking the navigation links on the dropdown
        :return:
        """
        self.navigation.resizeWindowToShowBurgerIcon()

        # verify navigation to project section
        self.util.sleep(sec=3)
        self.navigation.clickBurgerIcon()
        self.navigation.clickNavigationLink(link="Projects", dropdown=True)
        result_navigateToProjects = self.navigation.verifyNavigateToProjects()
        self.ts.mark(result_navigateToProjects, "Reached project section")
        result_dropdownHidden = not self.navigation.verifyDropDownMenuDisplayed()
        self.ts.mark(result_dropdownHidden, "Dropdown menu is hidden after the navigation process")

        # verify navigation to interest section
        self.util.sleep(sec=3)
        self.navigation.clickBurgerIcon()
        self.navigation.clickNavigationLink(link="Interests", dropdown=True)
        result_navigateToInterests = self.navigation.verifyNavigateToInterests()
        self.ts.mark(result_navigateToInterests, "Reached interest section")
        result_dropdownHidden = not self.navigation.verifyDropDownMenuDisplayed()
        self.ts.mark(result_dropdownHidden, "Dropdown menu is hidden after the navigation process")

        # verify navigation to contact section
        self.util.sleep(sec=3)
        self.navigation.clickBurgerIcon()
        self.navigation.clickNavigationLink(link="Contact", dropdown=True)
        result_navigateToContact = self.navigation.verifyNavigateToContact()
        self.ts.mark(result_navigateToContact, "Reached contact section")
        result_dropdownHidden = not self.navigation.verifyDropDownMenuDisplayed()
        self.ts.mark(result_dropdownHidden, "Dropdown menu is hidden after the navigation process")

        # verify navigation to mmy profile section
        self.util.sleep(sec=3)
        self.navigation.clickBurgerIcon()
        self.navigation.clickNavigationLink(link="Me", dropdown=True)
        result_navigateToProfile = self.navigation.verifyNavigateToMyProfile()
        self.ts.mark(result_navigateToProfile, "Reached my profile section")
        result_dropdownHidden = not self.navigation.verifyDropDownMenuDisplayed()
        self.ts.markFinal("test_clickDropdownOptions" , result_dropdownHidden, "Dropdown menu is hidden after the navigation process")
        self.util.sleep(sec=2)
