class Client:
    def __init__(self,name,id,age,tickets,compras,total_gastado,total_seat):
        self.name = name
        self.id = id
        self.age = age
        self.tickets = tickets
        self.compras = compras
        self.total_gastado = total_gastado
        self.total_seat = total_seat
    def append_ticket(self,ticket):
        self.tickets.append(ticket)
    def tickets_dicc(self):
        tickets_dicc= []
        for ticket in self.tickets:
            tickets_dicc.append(ticket.dicc())
        return tickets_dicc
    def compras_dicc(self):
        compras = []
        for compra in self.compras:
            compras.append(compra.dicc())
        return compras
    
    def sum_different_races(self):
        races = []
        for ticket in self.tickets:
            if ticket.race not in races:
                races.append(ticket.race)
        print(races)
        return len(races)
    def dicc(self):
        return{
            "name":self.name,
            "id":self.id,
            "age":self.age,
            "tickets":self.tickets_dicc(),
            "total seats":self.total_seat,
            "compras":self.compras_dicc(),
            'Total Gastado':self.total_gastado
        }