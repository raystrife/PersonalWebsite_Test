import utilities.custom_logger as cl
from base.basepage import BasePage
import logging

class ProjectsPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _projects_navigation = "Projects"
    _chess_project_title = "Chess Project"
    _project2 = "Project 2"
    _project3 = "Project 3"

    def hoverChessProject(self):
        """
        Hover over the chess project box
        :return:
        """
        self.elementHover(locator="//div[contains(text(),'" + self._chess_project_title +
                                  "')]//ancestor::div[@class='project_box']", locatorType="xpath")

    def hoverProject2(self):
        """
        Hover over the project 2 box that is still under development
        :return:
        """
        self.elementHover(locator="//img[@alt='" + self._project2 + "']//parent::div",
                          locatorType="xpath")

    def hoverProject3(self):
        """
        Hover over the project 3 box that is still under development
        :return:
        """
        self.elementHover(locator="//img[@alt='" + self._project3 + "']//parent::div",
                          locatorType="xpath")

    def clickChessProject(self):
        """
        Click the chess project box
        :return:
        """
        self.elementClick(locator="//div[contains(text(),'" + self._chess_project_title +
                                  "')]//ancestor::div[@class='project_box']", locatorType="xpath")

    def clickProject2(self):
        """
        Click the project 2 box that is still under development
        :return:
        """
        self.elementClick(locator="//img[@alt='" + self._project2 + "']//parent::div",
                          locatorType="xpath")

    def clickProject3(self):
        """
        Click the project 3 box that is still under development
        :return:
        """
        self.elementClick(locator="//img[@alt='" + self._project3 + "']//parent::div",
                          locatorType="xpath")

    def verifyChessProjectOpacity(self, hover=False):
        """
        Verify the opacity of the text and the image of the chess project
        :param hover: Boolean that is true if hovering over the chess project box
        :return:
        """
        textOpacity = self.getCSSValue(property="opacity",
                                               locator="//div[contains(text(),'" + self._chess_project_title +
                                                       "')]//parent::div[@class='project_overlay']",
                                               locatorType="xpath")
        imgOpacity = self.getCSSValue(property="opacity",
                                              locator="//img[@alt='" + self._chess_project_title + "']",
                                              locatorType="xpath")
        if hover:
            if (textOpacity == '1') and (imgOpacity == '0.3'):
                return True
            else:
                return False
        else:
            if (textOpacity == '0') and (imgOpacity == "1"):
                return True
            else:
                return False

    def verifyProject2Opacity(self, hover=False):
        """
        Verify the opacity of the text and the image of the project 2
        :param hover: Boolean that is true if hovering over the project 2 box
        :return:
        """
        textOpacity = self.getCSSValue(property="opacity",
                                               locator="//img[@alt='" + self._project2 +
                                                       "']//following-sibling::div",
                                               locatorType="xpath")
        imgOpacity = self.getCSSValue(property="opacity",
                                              locator="//img[@alt='" + self._project2+ "']",
                                              locatorType="xpath")
        if hover:
            if (textOpacity == '1') and (imgOpacity == '0.3'):
                return True
            else:
                return False
        else:
            if (textOpacity == '0') and (imgOpacity == "1"):
                return True
            else:
                return False

    def verifyProject3Opacity(self, hover=False):
        """
        Verify the opacity of the text and the image of the project 3
        :param hover: Boolean that is true if hovering over the project 3 box
        :return:
        """
        textOpacity = self.getCSSValue(property="opacity",
                                       locator="//img[@alt='" + self._project3 +
                                               "']//following-sibling::div",
                                       locatorType="xpath")
        imgOpacity = self.getCSSValue(property="opacity",
                                      locator="//img[@alt='" + self._project3 + "']",
                                      locatorType="xpath")
        if hover:
            if (textOpacity == '1') and (imgOpacity == '0.3'):
                return True
            else:
                return False
        else:
            if (textOpacity == '0') and (imgOpacity == "1"):
                return True
            else:
                return False

    def verifyChessProjectOpened(self):
        """
        Verify clicking the chess project open the correct github page
        :return:
        """
        self.driver.switch_to.window(self.driver.window_handles[1])
        result_chessProjectOpen = self.isElementPresent(locator="//a[contains(text(),'Chess-Project')]",
                                                        locatorType="xpath")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return result_chessProjectOpen

    def verifyInDevelopmentProjectNotOpen(self):
        """
        Verify clicking the "In Development' project doesn't open new tabs
        :return:
        """
        numberWindowOpens = len(self.driver.window_handles)
        if numberWindowOpens == 1:
            return True
        else:
            return False

    def scrollToProjectSection(self):
        """
        Verify scrolling to the project section
        :return:
        """
        self.scrollFindElement("Projects")
