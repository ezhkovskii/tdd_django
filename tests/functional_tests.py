import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class NewVisitorTest(unittest.TestCase):
    """тест нового посетителя"""

    def setUp(self):
        """установка"""
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        """закрытие"""
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """тест: можно начать список и получить его позже"""
        # Эдит слышала про крутое новое онлайн-приложение со
        # списком неотложных дел. Она решает оценить его
        # домашнюю страницу
        self.browser.get('http://localhost:8000')
        # Она видит, что заголовок и шапка страницы говорят о
        # списках неотложных дел
        self.assertIn('To-Do', self.browser.title)
        self.fail('Закончить тест!')
        # Ей сразу же предлагается ввести элемент списка


if __name__ == '__main__':
    unittest.main(warnings='ignore')
