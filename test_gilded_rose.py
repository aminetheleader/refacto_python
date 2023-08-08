# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fixme", items[0].name)

    def test_aged_brie_quantity(self):
        items = [Item(name="Aged Brie", sell_in=4, quality=30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()


if __name__ == '__main__':
    unittest.main()
