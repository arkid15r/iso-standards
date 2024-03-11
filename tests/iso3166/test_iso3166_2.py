"""ISO 3166-2 tests."""

from unittest import TestCase

from iso_standards.iso3166.iso3166_2 import Iso3166_2
from iso_standards.iso3166.types import Iso3166_2 as Entity


class TestIso3166_2(TestCase):
    def setUp(self):
        self.iso3166_2 = Iso3166_2()

    def test_get_item(self):
        kyiv = self.iso3166_2.UA_30[0]
        self.assertIsInstance(kyiv, Entity)
        self.assertEqual(kyiv.name, "Kyiv")
        self.assertEqual(kyiv.category, "CITY")
        self.assertEqual(kyiv.language_code, "uk")

    def test_contents(self):
        self.assertGreater(len(self.iso3166_2), 5000)

    def test_str(self):
        self.assertEqual(str(self.iso3166_2), "ISO 3166-2 entities")
        self.assertEqual(str(self.iso3166_2.UA_30[0]), "ISO 3166-2 UA-30")
