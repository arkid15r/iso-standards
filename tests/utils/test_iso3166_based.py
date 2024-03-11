"""ISO 3166 based utils tests."""

from unittest import TestCase

from iso_standards.utils import ISO_3166_BASED_ENTITIES


class TestIso3166Entities(TestCase):
    def test_iso3166_entities(self):
        ua = ISO_3166_BASED_ENTITIES.UA

        self.assertEqual(ua.alpha_2, "UA")
        self.assertGreater(len(ua.subdivisions), 25)
