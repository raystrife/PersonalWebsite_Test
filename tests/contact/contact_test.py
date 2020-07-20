from pages.contact_page import ContactPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.util as util

@pytest.mark.usefixtures("oneTimeSetup", "setUp")
class ContactTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        """
        Run the setup before the test starts
        :return:
        """
        self.contact = ContactPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.util = util.Util()

    @pytest.mark.run(order=1)
    def test_scrollToContactSection(self):
        """
        Test the default state of contact section
        :return:
        """
        self.contact.scrollToContactSection()

        result_resumeOpacity = self.contact.verifyContactIconOpacity(icon="Resume", hover=False)
        self.ts.mark(result_resumeOpacity, "Resume icon is fully visible by default")

        result_workExpOpacity = self.contact.verifyContactIconOpacity(icon="Work Experience", hover=False)
        self.ts.mark(result_workExpOpacity, "Work Experience icon is fully visible by default")

        result_linkedinOpacity = self.contact.verifyContactIconOpacity(icon="LinkedIn", hover=False)
        self.ts.markFinal("test_scrollToContactSection", result_linkedinOpacity,
                          "LinkedIn icon is fully visible by default")

    @pytest.mark.run(order=2)
    def test_hoverResumeIcon(self):
        """
        Test hovering over the resume icon changes its opacity
        :return:
        """
        self.contact.scrollToContactSection()
        self.contact.hoverContactIcon(icon="Resume")
        self.util.sleep(sec=2)
        result_resumeOpacity = self.contact.verifyContactIconOpacity(icon="Resume", hover=True)
        self.ts.markFinal("test_hoverResumeIcon", result_resumeOpacity, "Resume icon should be fading")

    @pytest.mark.run(order=3)
    def test_hoverWorkExpIcon(self):
        """
        Test hovering over the work experience icon changes its opacity
        :return:
        """
        self.contact.scrollToContactSection()
        self.contact.hoverContactIcon(icon="Work Experience")
        self.util.sleep(sec=2)
        result_workExpOpacity = self.contact.verifyContactIconOpacity(icon="Work Experience", hover=True)
        self.ts.markFinal("test_hoverWorkExpIcon", result_workExpOpacity, "Work Experience icon should be fading")

    @pytest.mark.run(order=4)
    def test_hoverLinkedinIcon(self):
        """
        Test hovering over the LinkedIn icon changes its opacity
        :return:
        """
        self.contact.scrollToContactSection()
        self.contact.hoverContactIcon(icon="LinkedIn")
        self.util.sleep(sec=2)
        result_linkedInOpacity = self.contact.verifyContactIconOpacity(icon="LinkedIn", hover=True)
        self.ts.markFinal("test_hoverLinkedinIcon", result_linkedInOpacity, "Linkedin icon should be fading")

    # @pytest.mark.run(order=5)
    # def test_clickResumeIcon(self):
    #     self.contact.scrollToContactSection()
    #     self.contact.clickContactIcon(icon="Resume")
    #     result_pdfOpen = self.contact.verifyPDFOpen(icon="Resume")
    #     self.ts.markFinal("test_clickResumeIcon", result_pdfOpen, "Resume pdf should open")

    # @pytest.mark.run(order=6)
    # def test_clickWorkExpIcon(self):
    #     self.contact.scrollToContactSection()
    #     self.contact.clickContactIcon(icon="Work Experience")
    #     result_pdfOpen = self.contact.verifyPDFOpen(icon="Work Experience")
    #     self.ts.markFinal("test_clickWorkExpIcon", result_pdfOpen, "Work experience pdf should open")

    @pytest.mark.run(order=7)
    def test_clickLinkedinIcon(self):
        """
        Test clicking the LinkedIn Icon opens the correct page
        :return:
        """
        self.contact.scrollToContactSection()
        self.contact.clickContactIcon(icon="LinkedIn")
        result_pdfOpen = self.contact.verifyPageOpenAfterClick(icon="LinkedIn")
        self.ts.markFinal("test_clickLinkedinIcon", result_pdfOpen, "LinkedIn page should open")
