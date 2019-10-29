from unittest import TestCase

import task6


class TestTask6(TestCase):

    def setUp(self):
        """Init"""

    def test_SplitStr(self):
        """Test for SplitStr"""
        self.assertEqual(task6.SplitStr('the first string'), ['the', 'first', 'string'])
        self.assertEqual(task6.SplitStr('Prosto dlinnaya stroka'), ['Prosto', 'dlinnaya', 'stroka'])
        self.assertEqual(task6.SplitStr(''), [''])
        self.assertEqual(task6.SplitStr('SingleWord'), ['SingleWord'])

    def test_ReversList(self):
        self.assertEqual(task6.ReversList(['the', 'first', 'string']), 'eht tsrif gnirts')
        self.assertEqual(task6.ReversList(['Prosto', 'dlinnaya', 'stroka']), 'otsorP ayannild akorts')
        self.assertEqual(task6.ReversList(['']), '')
        self.assertEqual(task6.ReversList(['SingleWord']), 'droWelgniS')

    def tearDown(self):
        """Finish"""
