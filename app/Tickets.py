import random as r
class Ticket:
    def __init__(self,race_name,seats,codes,attendance) -> None:
        self.race = race_name
        self.seats = seats
        self.attendance = attendance
        self.codes = codes
    def generate_codes(self,db,n_sets):
        codes =[]
        i = 0
        while i < n_sets:
            clave = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
            while True:
                code = r.choices(clave, k = 5)
                if code in db:
                    continue
                else:
                    code = ''.join(code)
                    codes.append(code)
                    break
            i +=1
        self.codes =codes
    def change_attendance(self):
        self.attendance = True
    def dicc(self):
        return{
            'type':self.type,
            'price':self.price,
            'race':self.race,
            'seats':self.seats,
            'attendance':self.attendance,
            'codes':self.codes
        }
class TicketGeneral(Ticket):
    type = 'General'
    price = 150
class TicketVIP(Ticket):
    type = 'VIP'
    price = 340

