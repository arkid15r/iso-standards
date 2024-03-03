"""ISO 3166-1 tests."""

from unittest import TestCase

from iso_standards.iso3166.iso3166_1 import Iso3166_1
from iso_standards.iso3166.types import Iso3166_1 as Entity


class TestIso3166_1(TestCase):
    def setUp(self):
        self.iso3166_1 = Iso3166_1()

    def test_get_item(self):
        self.assertTrue(isinstance(self.iso3166_1.UA, Entity))
        self.assertEqual(self.iso3166_1.UA.short_name, "Ukraine")
        self.assertEqual(self.iso3166_1.UA.alpha_2, "UA")
        self.assertEqual(self.iso3166_1.UA.num_3, "804")

    def test_contents(self):
        self.assertGreater(len(self.iso3166_1), 200)
