__author__ = 'asistente'
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import platform


class FunctionalTest(TestCase):

    def setUp(self):
        if platform.system() == 'Windows':
            driver = 'D:\\Python\\chromedriver.exe'
        else:
            driver = '/Users/juanvillegas/Documents/Ingenieria de Software/ProcesosAgiles/katas/kata-web/chromedriver'
        self.browser = webdriver.Chrome(driver)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('BuscoAyuda', self.browser.title)

