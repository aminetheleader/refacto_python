
class GildedRose:
    def __init__(self, items: list):
        self.items = []
        for item in items:
            item_class = ITEMS_MAPPING.get(item.name, Item)
            self.items.append(item_class(item.name, item.sell_in, item.quality))

    def update_quality(self) -> None:
        for item in self.items:
            item.update()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update(self):
        self.sell_in -= 1
        if self.quality > 0:
            self.quality -= 1 if (self.sell_in > 0) else min(2, self.quality)

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"


class AgedBrie(Item):
    def update(self):
        self.sell_in -= 1
        if self.quality < 50:
            self.quality += 1


class Sulfuras(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
        self.quality = 80
        self.sell_in = None

    def update(self):
        """
        Nothing happens to Sulfuras
        """
        pass


class BackstagePasses(Item):

    def update(self):
        """
        Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
        Quality drops to 0 after the concert
        """
        self.sell_in -= 1
        if 5 < self.sell_in <= 10:
            self.quality += 2
        elif 0 < self.sell_in <= 5:
            self.quality += 3
        elif self.sell_in <= 0:
            self.quality = 0
        elif self.quality < 50:
            self.quality += 1


ITEMS_MAPPING = {
    "Aged Brie": AgedBrie,
    "Sulfuras, Hand of Ragnaros": Sulfuras,
    "Backstage passes to a TAFKAL80ETC concert": BackstagePasses,
}
