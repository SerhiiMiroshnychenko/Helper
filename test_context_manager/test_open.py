import unittest
from unittest import TestCase
import logging

from ..task_1.task_1 import Open


class TestOpen(TestCase):
    def setUp(self) -> None:
        while True:
            try:
                with open('test.txt', 'w', encoding='utf-8') as f:
                    f.write('Text for test 1.')
                    break
            except PermissionError as error:
                logging.error(f'IN SETUP: {error.__class__} {error}')
        Open.successful_counter = 0
        Open.failed_counter = 0

    def test_Open_read(self):
        """Перевіряємо читання файлу що існує"""
        logging.info('\n\n---------->. test_Open_read START:')
        with Open('test.txt', 'r') as opened_file:
            result1 = opened_file.read()
        result2 = 'Text for test 1.'
        self.assertEqual(result1, result2, msg='Oops!')
        logging.info('\n---------->. test_Open_read END.\n\n')

    def test_Open_write(self):
        """Перевіряємо перезапис файлу"""
        logging.info('\n\n---------->. test_Open_write START:')
        with Open('test.txt', 'w') as opened_file:
            opened_file.write('Text for test 2.')
        with Open('test.txt', 'r') as opened_file:
            result1 = opened_file.read()
        result2 = 'Text for test 2.'
        self.assertEqual(result1, result2, msg='Oops!')
        logging.info('\n---------->. test_Open_write END.\n\n')

    ...
