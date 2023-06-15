class Restaurant:
    def __init__(self,name,items):
        self.name = name
        self.items = items
    def show_attributes(self):
        print('\n')
        print(f'Name ==> {self.name}')
        for item in self.items:
            item.show_attributes()
    def items_dicc(self):
        items = []
        for item in self.items:
            items.append(item.dicc())
        return items
    def dicc(self):
        return{
            "name":self.name,
            "items":self.items_dicc()
        }
