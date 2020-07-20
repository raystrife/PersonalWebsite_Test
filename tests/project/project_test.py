from pages.projects_page import ProjectsPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.util as util

@pytest.mark.usefixtures("oneTimeSetup", "setUp")
class ProjectTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        self.project = ProjectsPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.util = util.Util()

    @pytest.mark.run(order=1)
    def test_scrollToProjectSection(self):
        self.project.scrollToProjectSection()
        result_chessProjectOpacity = self.project.verifyChessProjectOpacity(hover=False)
        self.ts.mark(result_chessProjectOpacity, "The chess project image is visible and the title is invisible")

        result_project2Opacity = self.project.verifyProject2Opacity(hover=False)
        self.ts.mark(result_project2Opacity, "The project 2 image is visible and the title is invisible")

        result_project3OPacity = self.project.verifyProject3Opacity(hover=False)
        self.ts.markFinal("test_scrollToProjectSection", result_project3OPacity,
                          "The project 3 image is visible and the title is invisible")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=2)
    def test_hoverChessProject(self):
        self.project.scrollToProjectSection()
        self.project.hoverChessProject()
        self.util.sleep(sec=1)

        result_chessProjectOpacity = self.project.verifyChessProjectOpacity(hover=True)
        self.ts.markFinal("test_hoverChessProject", result_chessProjectOpacity,
                          "The chess project image is fading and the title is visible")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=3)
    def test_hoverProject2(self):
        self.project.scrollToProjectSection()
        self.project.hoverProject2()
        self.util.sleep(sec=1)

        result_project2 = self.project.verifyProject2Opacity(hover=True)
        self.ts.markFinal("test_hoverProject2", result_project2,
                          "The project 2 is fading and the title is visible")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=4)
    def test_hoverProject3(self):
        self.project.scrollToProjectSection()
        self.project.hoverProject3()
        self.util.sleep(sec=1)

        result_project3 = self.project.verifyProject3Opacity(hover=True)
        self.ts.markFinal("test_hoverProject3", result_project3,
                          "The project 3 is fading and the title is visible")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=5)
    def test_clickChessProject(self):
        self.project.scrollToProjectSection()
        self.project.clickChessProject()
        result_chessProjectOpen = self.project.verifyChessProjectOpened()
        self.ts.markFinal("test_clickChessProject", result_chessProjectOpen,
                          "Clicking the chess project open the correct page")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=6)
    def test_clickInDevelopmentProject(self):
        self.project.scrollToProjectSection()
        self.project.clickProject2()
        result_projectOpen = self.project.verifyInDevelopmentProjectNotOpen()
        self.ts.mark(result_projectOpen, "Project 2 should not open because it's in development")

        self.project.clickProject3()
        result_projectOpen = self.project.verifyInDevelopmentProjectNotOpen()
        self.ts.markFinal("test_clickInDevelopmentProject", result_projectOpen,
                          "Project 3 should not open because it's in development")
        self.util.sleep(sec=2)