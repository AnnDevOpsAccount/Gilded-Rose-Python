class GildedRose(object):

    a = "Backstage passes to a TAFKAL80ETC concert"

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie" or item.name == "Backstage passes to a TAFKAL80ETC concert":
                increment_item_quality(item)
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        increment_item_quality(item)
                    if item.sell_in < 6:
                        increment_item_quality(item)
            else:
                if item.quality > 0 and item.name != "Sulfuras, Hand of Ragnaros":
                    self.decrement_item_quality(item)
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name == "Aged Brie":
                    increment_item_quality(item)                
                else:
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        item.quality = item.quality - item.quality                    
                    else:
                        if item.quality > 0 and item.name != "Sulfuras, Hand of Ragnaros":
                            self.decrement_item_quality(item)

    def decrement_item_quality(self, item):
        item.quality -= 1

def increment_item_quality(item):
    if item.quality < 50:
        item.quality += 1
