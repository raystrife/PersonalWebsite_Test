import utilities.custom_logger as cl
from base.basepage import BasePage
import logging

class InterestPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # methods
    def hoverTabButtons(self, button="Video Games"):
        """
        Hover over the specified tab button
        :param button: a string containing the title of the tab button
        :return:
        """
        self.elementHover(locator="//button[contains(text(),'" + button + "')]", locatorType="xpath")

    def clickTabButtons(self, button="Video Games"):
        """
        Click over the specified tab button
        :param button: a string containing the title of the tab button
        :return:
        """
        self.elementClick(locator="//button[contains(text(),'" + button + "')]", locatorType="xpath")

    def clickGameLink(self):
        """
        Click the game link on the programming tab
        :return:
        """
        self.clickTabButtons(button="Programming")
        self.elementClick(locator="//a[contains(text(),'link')]", locatorType="xpath")

    def playVideo(self):
        """
        Play the YouTube video
        :return:
        """
        self.clickTabButtons(button="Video Games")
        self.elementClick(locator="//iframe", locatorType="xpath")

    def verifyDefaultInterestSection(self):
        """
        Verify the default state of interest section
        :return:
        """
        videoGamesBackground = self.getCSSValue(property="background-color",
                                                locator="//button[contains(text(),'Video Games')]", locatorType="xpath")
        foodGourmetBackground = self.getCSSValue(property="background-color",
                                                 locator="//button[contains(text(),'Food Gourmet')]", locatorType="xpath")
        programmingBackground = self.getCSSValue(property="background-color",
                                                 locator="//button[contains(text(),'Programming')]", locatorType="xpath")

        videoGamesDisplayed = self.isElementDisplayed(locator="//h2[contains(text(),'Video Games')]",
                                                      locatorType="xpath")
        foodGourmetDisplayed = not self.isElementDisplayed(locator="//h2[contains(text(),'Food Gourmet')]",
                                                           locatorType="xpath")
        programmingDisplayed = not self.isElementDisplayed(locator="//h2[contains(text(),'Programming')]",
                                                           locatorType="xpath")

        if (videoGamesBackground == "rgba(204, 204, 204, 1)") and (foodGourmetBackground == "rgba(0, 0, 0, 0)") and \
                (programmingBackground == "rgba(0, 0, 0, 0)") and videoGamesDisplayed and foodGourmetDisplayed and \
                programmingDisplayed:
            return True
        else:
            return False

    def verifyHoveringButtons(self, button="Video Games"):
        """
        Verify hovering over button displays the appropriate background
        :param button: a string containing the title of the tab button
        :return:
        """
        buttonBackground = self.getCSSValue(property="background-color",
                                         locator="//button[contains(text(),'" + button + "')]", locatorType="xpath")
        buttonFont = self.getCSSValue(property="color",
                                         locator="//button[contains(text(),'" + button + "')]", locatorType="xpath")

        if (buttonBackground == "rgba(204, 204, 204, 1)") and (buttonFont == "rgba(0, 0, 0, 1)"):
            return True
        elif (buttonBackground == "rgba(96, 96, 96, 1)") and (buttonFont == "rgba(255, 255, 255, 1)"):
            return True
        else:
            return False

    def verifyTabOpen(self, button="Video Games"):
        """
        Verify the correct tab is open
        :param button: a string containing the title of the tab button
        :return:
        """
        tabDisplayed = self.isElementDisplayed(locator="//h2[contains(text(),'" + button + "')]",
                                               locatorType="xpath")
        buttonBackground = self.getCSSValue(property="background-color",
                                         locator="//button[contains(text(),'" + button + "')]", locatorType="xpath")
        buttonFont = self.getCSSValue(property="color",
                                         locator="//button[contains(text(),'" + button + "')]", locatorType="xpath")

        result = tabDisplayed and (buttonBackground == "rgba(204, 204, 204, 1)") and (buttonFont == "rgba(0, 0, 0, 1)")
        return result

    def verifyChessProjectOpen(self):
        """
        Verify that the correct github project is open
        :return:
        """
        self.driver.switch_to.window(self.driver.window_handles[1])
        result_chessProjectOpen = self.isElementPresent(locator="//a[contains(text(),'Chess-Project')]",
                                                        locatorType="xpath")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return result_chessProjectOpen

    def verifyVideoPlayed(self):
        """
        Verify that the YouTube video plays successfully
        :return:
        """
        iframe = self.getElement(locator="//iframe", locatorType="xpath")
        self.driver.switch_to.frame(iframe)
        result_videoPlayed = self.isElementPresent(locator="//button[@title='Pause (k)']", locatorType="xpath")
        self.driver.switch_to.default_content()
        return result_videoPlayed

    def scrollToInterestSection(self):
        """
        Scroll to the interest section
        :return:
        """
        self.scrollFindElement("Interests")