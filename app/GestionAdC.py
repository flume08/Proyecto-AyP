class GestionAdC:
    ##Obetener el la carrera que desea verificar el admin
    def get_race(self,carreras_ob_db):
        i = 1
        for race in carreras_ob_db:
            print(f'==> {i}.{race.name}-{race.date}')
            i+=1
        while True:
            user_input = input('==> ')
            if user_input.isdigit():
                if 0 < int(user_input) < len(carreras_ob_db)+1:
                    carrera = carreras_ob_db[int(user_input)-1]
                    break
        return carrera
    def get_code(self):
                print('Ingrese el codigo de la entrada que desea verifica.')
                code = input('==> ')
                return code
   ##Verificar si existe un cliente con ese codigo de entrada
    def validate_code(self,race,codigo):
        for code in race.codes:
            if codigo == code:
                return code
        return False
    def get_tickets(self,race,clients_db,code):
        lis_tickets = []
        for client in clients_db:
            for ticket in client.tickets:
                for codigo in ticket.codes:
                    if code == codigo and ticket.race ==race.name:
                        lis_tickets.append(ticket)
                        return client,lis_tickets
        return False
    ## Realizar todas las operaciones y ademas poder cambiar el at4rbuto attendance del cliente
    def index_1(self,db,clients_db):
        race = self.get_race(db)
        code = self.get_code()
        if self.validate_code(race,code):
            if self.get_tickets(race,clients_db,code):
                code = self.validate_code(race,code)
                client,list_tickets = self.get_tickets(race,clients_db,code)
                if not list_tickets[0].attendance:
                    print(f'El/Los boleto/s de pertenece a: ')
                    print(f'Nombre = {client.name}\n C.I = {client.id}\n Carrera = {race.name}')
                    while True:
                        print('Desea marcar la asistencia de este boleto [y/n]')
                        user_input = input('==> ')
                        if user_input == 'y':
                            for ticket in list_tickets:
                                ticket.change_attendance()
                                for seat in ticket.seats:
                                    race.assistance +=1
                            break
                        elif user_input == 'n':
                            break
                        else:
                            print('Dato invalido')
                else:
                    print(f'El/Los boleto/s  pertenece a: ')
                    print(f'Nombre = {client.name}\n C.I = {client.id}')
                    print('Y ya ha entrado a las instalaciones')
            else:
                print('Ese codigo esta en la base de datos pero no esta en esta carrera')
        else:
            print('Ese codigo no existe')
    def start_gestionAdC(self,carreras_ob_db,clients_db):
        while True:
            print('Elija una de las siguientes opciones\t\n1. Veriificar la veracidad de una entrada\t\n2. Salir')
            user_input = input('==> ')
            if user_input == '1':
                self.index_1(carreras_ob_db,clients_db)
            elif user_input =='2':
                break
            else:
                print('Dato invalido')