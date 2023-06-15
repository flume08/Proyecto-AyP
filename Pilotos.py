class Pilot:
    def __init__(self,driverId, permanentNumber, code, team, firstName, lastName, dateOfBirth, nationality,points):
        self.driverId = driverId
        self.permanentNumber = permanentNumber
        self.code = code
        self.team = team
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.nationality = nationality
        self.points = points
    def get_placement(self,points):
        self.points += points
    def show_attributes(self):
        print(f'id ==> {self.driverId}')
        print(f'Number ==> {self.permanentNumber}')
        print(f'code ==> {self.code}')
        print(f'Team ==> {self.team}')
        print(f'First Name ==> {self.firstName}')
        print(f'Last Name ==> {self.lastName}')
        print(f'Date of birth ==> {self.dateOfBirth}')
        print(f'Nationality ===>{self.nationality}')
        print(f'Points ==> {self.points}')