class Constructor:
    def __init__(self,id,name,nationality,pilotos,points =0):
        self.id = id
        self.name = name
        self.nationality = nationality
        self.pilotos = pilotos
        self.points = points
    def show_attributes(self):
        print('\n')
        print(f'id ==> {self.id}')
        print(f'Name ==> {self.name}')
        print(f'Nationality ==> {self.nationality}')
        print(f'Pilotos ==>')
        for p in self.pilotos:
            print('\n')
            p.show_attributes()
    def sum_points(self):
        for pilot in self.pilotos:
            self.points += pilot.points
    def dicc(self):
        return{
            "id": self.id,
            "name":self.name,
            "nationality" : self.nationality,
            "points": self.points
        }