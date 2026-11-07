
import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class TestSearchCategory(unittest.TestCase):

    def setUp(self):
        self.items = [
            DigitalVideoDisc("The Lion King", "Animation"),
            DigitalVideoDisc("Star Wars", "Science Fiction"),
            DigitalVideoDisc("Aladdin", "Animation"),
        ]

    def test_search_animation(self):
        result = search_by_category(
            self.items, "Animation"
        )

        titles = [dvd.title for dvd in result]

        self.assertEqual(
            titles,
            ["The Lion King", "Aladdin"]
        )

    def test_search_no_match(self):
        result = search_by_category(
            self.items, "Horror"
        )

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
