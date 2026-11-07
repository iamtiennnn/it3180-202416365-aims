
import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearch(unittest.TestCase):

    def test_search_by_title_case_insensitive(self):
        items = [
            DigitalVideoDisc("The Lion King"),
            DigitalVideoDisc("Star Wars"),
        ]

        result = search_by_title(items, "lion")

        titles = [dvd.title for dvd in result]

        self.assertEqual(
            titles,
            ["The Lion King"]
        )


if __name__ == "__main__":
    unittest.main()
