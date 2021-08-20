# pylint: disable=no-member
from django.test import TestCase

class TestTheTest(TestCase):
    """Test string"""

    def setUp(self) -> None:
        self.we_need_this_in_all_our_fnx = "CI deployment"
        return super().setUp()
    
    def test_name(self):
        self.assertEqual(
            self.we_need_this_in_all_our_fnx,
            "CI deployment"
            )
