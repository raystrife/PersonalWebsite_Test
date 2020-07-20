from pages.interest_page import InterestPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.util as util

@pytest.mark.usefixtures("oneTimeSetup", "setUp")
class InterestTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        """
        Run the setup before the test starts
        :return:
        """
        self.interest = InterestPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.util = util.Util()

    @pytest.mark.run(order=1)
    def test_scrollToInterestSection(self):
        """
        Test the default state of interest section
        :return:
        """
        self.interest.scrollToInterestSection()
        resultDefault = self.interest.verifyDefaultInterestSection()
        self.ts.markFinal("test_scrollToInterestSection", resultDefault,
                          "The default state of interest section is incorrect")

    @pytest.mark.run(order=2)
    def test_hoverTabButtons(self):
        """
        Test hovering over a tab button changes the button's background
        :return:
        """
        self.interest.scrollToInterestSection()
        self.interest.hoverTabButtons(button="Video Games")
        self.util.sleep(sec=1)
        resultHoverVideoGames = self.interest.verifyHoveringButtons(button="Video Games")
        self.ts.mark(resultHoverVideoGames, "Background color of video games button is correct")

        self.interest.hoverTabButtons(button="Food Gourmet")
        self.util.sleep(sec=1)
        resultHoverFoodGourmet = self.interest.verifyHoveringButtons(button="Food Gourmet")
        self.ts.mark(resultHoverFoodGourmet, "Background color of food gourmet button is correct")

        self.interest.hoverTabButtons(button="Programming")
        self.util.sleep(sec=1)
        resultHoverProgramming = self.interest.verifyHoveringButtons(button="Programming")
        self.ts.markFinal("test_hoverTabButtons", resultHoverProgramming,
                          "Background color of programming button is correct")

    @pytest.mark.run(order=3)
    def test_clickTabButtons(self):
        """
        Test clicking a tab button displays the correct content
        :return:
        """
        self.interest.scrollToInterestSection()
        self.interest.clickTabButtons(button="Video Games")
        self.util.sleep(sec=1)
        resultClickVideoGames = self.interest.verifyTabOpen(button="Video Games")
        self.ts.mark(resultClickVideoGames, "Video games tab should open")

        self.interest.clickTabButtons(button="Food Gourmet")
        self.util.sleep(sec=1)
        resultClickFoodGourmet = self.interest.verifyTabOpen(button="Food Gourmet")
        self.ts.mark(resultClickFoodGourmet, "Food gourmet tab should open")

        self.interest.clickTabButtons(button="Programming")
        self.util.sleep(sec=1)
        resultClickProgramming = self.interest.verifyTabOpen(button="Programming")
        self.ts.markFinal("test_clickTabButtons", resultClickProgramming, "Programming tab should open")

    @pytest.mark.run(order=4)
    def test_clickGameLink(self):
        """
        Test clicking the game link on the programming tab opens the correct github page
        :return:
        """
        self.interest.scrollToInterestSection()
        self.interest.clickGameLink()
        result_chessProjectOpen = self.interest.verifyChessProjectOpen()
        self.ts.markFinal("test_clickGameLinkButton", result_chessProjectOpen,
                          "Clicking the link open the chess project")

    @pytest.mark.run(order=5)
    def test_playGamesVideo(self):
        """
        Test playing the YouTube video on the video games tab
        :return:
        """
        self.interest.scrollToInterestSection()
        self.interest.playVideo()
        self.util.sleep(sec=4)
        result_videoPlayed = self.interest.verifyVideoPlayed()
        self.ts.markFinal("test_playGamesVideo", result_videoPlayed, "Video played successfully")