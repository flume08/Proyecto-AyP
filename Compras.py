class Compra:
    def __init__(self,id,total,items):
        self.id = id
        self.total = total
        self.items = items
    def append_item(self,item):
        self.items.append(item)
    def item_dicc(self):
        items = []
        for item in self.items:
            items.append(item.dicc())
        return items
    def dicc(self):
        return {
            "id":self.id,
            "total":self.total,
            "items":self.item_dicc()
        }