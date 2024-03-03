"""Country utils tests."""

from unittest import TestCase

from iso_standards.utils import countries


class TestCountries(TestCase):
    def test_countries(self):
        ua = countries.UA

        self.assertEqual(ua.alpha_2, "UA")
        self.assertGreater(len(ua.subdivisions), 25)
