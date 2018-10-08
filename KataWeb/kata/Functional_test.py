__author__ = 'asistente'
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
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

    def test_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        self.browser.implicitly_wait(1)

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Juan Daniel')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Arevalo')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Independiente']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3173024578')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jd.patino1@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        img = os.path.join(os.path.abspath('persona.png'))

        if platform.system() == 'Windows':
            img = img.replace("\\", "\\\\")
        else:
            img = img.replace("\\", "/")
        imagen.send_keys(img)

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('juan645')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()

        self.browser.implicitly_wait(3)
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', span.text)

    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span=self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()

        h2=self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', h2.text)

    def test_logIn(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        self.browser.implicitly_wait(1)

        nombre = self.browser.find_element_by_id('id_username')
        nombre.send_keys('admin')

        apellidos = self.browser.find_element_by_id('id_password')
        apellidos.send_keys('villegas')

        botonLogin = self.browser.find_element_by_id('id_login')
        botonLogin.click()

        self.browser.implicitly_wait(5)

        nombre = self.browser.find_element_by_id('id_name')
        self.assertIn('Juan Villegas', nombre.text)
        self.assertIn('BuscoAyuda', self.browser.title)

    def test_edit(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        self.browser.implicitly_wait(1)

        nombre = self.browser.find_element_by_id('id_username')
        nombre.send_keys('pedro')

        apellidos = self.browser.find_element_by_id('id_password')
        apellidos.send_keys('villegas')

        botonLogin = self.browser.find_element_by_id('id_login')
        botonLogin.click()

        self.browser.implicitly_wait(5)

        botonEdit = self.browser.find_element_by_id('id_editar')
        botonEdit.click()

        self.browser.implicitly_wait(5)

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('1234567')

        botonEdit = self.browser.find_element_by_id('id_save')
        botonEdit.click()

        self.browser.implicitly_wait(5)

        telefono = self.browser.find_element_by_id('id_telefono')
        self.assertIn('1234567', telefono.text)
