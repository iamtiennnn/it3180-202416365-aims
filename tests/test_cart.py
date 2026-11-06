
import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):

    def test_add_dvd_until_full(self):
        cart = Cart()

        # Them dung 20 DVD
        for i in range(MAX_NUMBERS_ORDERED):
            dvd = DigitalVideoDisc(f"DVD {i}")
            self.assertTrue(cart.add_dvd(dvd))

        # Kiem tra gio hang da co 20 DVD
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)

        # Thu them DVD thu 21
        extra_dvd = DigitalVideoDisc("Extra DVD")

        # DVD thu 21 phai bi tu choi
        self.assertFalse(cart.add_dvd(extra_dvd))

        # Gio hang van chi co 20 DVD
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)


if __name__ == "__main__":
    unittest.main()
