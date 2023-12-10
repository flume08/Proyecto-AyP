class Circuit:
    def __init__(self,circuitid,name,Location):
        self.circuitid = circuitid
        self.name = name
        self.Location = Location
    def show_attributes(self):
        print('\n')
        print(f'id ==> {self.circuitid}')
        print(f'Name ==> {self.name}')
        print(f'Location ==>')
        self.Location.show_attributes()
    def dicc(self):
        return{
            'circuitid':self.circuitid,
            'name':self.name,
            'Location': vars(self.Location)
        }
