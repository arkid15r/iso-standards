"""ISO 3166 base tests."""

from unittest import TestCase

from iso_standards.base import EntityCollection
from iso_standards.errors import EntityNotFoundError


class TestBase(TestCase):
    def setUp(self) -> None:
        self.dc = EntityCollection()
        self.dc.entities = {"a": 1, "b": 2, "c": 3, "d": 4}

    def test_contains(self):
        for key in ("a", "b", "c", "d"):
            self.assertIn(key, self.dc)

        for key in (None, "", "z", 1):
            self.assertNotIn(key, self.dc)

    def test_getattr(self):
        self.assertEqual(self.dc.a, 1)

        with self.assertRaises(EntityNotFoundError):
            self.dc.z

    def test_iter(self):
        self.assertEqual(tuple(self.dc), (1, 2, 3, 4))

    def test_len(self):
        self.assertEqual(len(self.dc), 4)
