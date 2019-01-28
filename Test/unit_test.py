# Unit test

import unittest

from test_function_1 import get_formatied_name

class NamesTestCase(unittest.TestCase):
    """Tests for the test_function_1.py"""

    def test_first_last_name(self):
        """Test first and last name"""

        formatted_name = get_formatied_name('rene', 'cortez')
        self.assertEqual(formatted_name, 'Rene Cortez')

    unittest.main()
