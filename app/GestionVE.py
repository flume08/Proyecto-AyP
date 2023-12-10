from Tickets import Ticket,TicketGeneral,TicketVIP
from Client import Client
import numpy as np
class GestionVE:
    ##Funcion generalizada para obetener data
    def get_data(self,tipo, character):
        if character == 'numero':
                while True:
                    data = input(f'ingrese su {tipo}\n\t===> ')
                    if data.isdigit():
                        break
                    else:
                        print('Dato invalido')

        elif character == 'letra':
            while True:
                data = input(f'ingrese su {tipo}\n\t===> ')
                if data.isalpha():
                    break
                else:
                    print('Dato invalido')  
        else:
            print('Character invalido invalido')
        return data
    # Funcion para obetener la carrera que desea ir el cliente
    def get_race(self,carreras_ob_db):
        i = 1
        for race in carreras_ob_db:
            print(f'==> {i}.{race.name}')
            i+=1
        while True:
            user_input = input('==> ')
            if user_input.isdigit():
                if 0 < int(user_input) < len(carreras_ob_db)+1:
                    carrera = carreras_ob_db[int(user_input)-1]
                    if race.map.vip[0]*race.map.vip[1] - race.puestosvip + race.map.general[0]*race.map.general[1] - race.puestosgeneral > 0:
                            return carrera
                    else:
                        print(f'No quedan asientos disponibles en {carrera.name}')
                else:
                    print('Dato invalido')
            else:
                print(f'Dato invalido')
    #Funcion que crea un objeto de ticker que posee toda la informacion y libertades de pendiendo del ticket
    def get_ticket_type(self,race):
        while True:
            print('Elija el tipo de entrada\t\n1. VIP\t\n2. General')
            user_input = input('==> ')
            if user_input =='1':
                if  0< race.map.vip[0]*race.map.vip[1] - race.puestosvip:
                    ticket = 1
                    break
                else:
                    print('No disponemos de mas puestos')
            elif user_input =='2':
                if 0<race.map.general[0]*race.map.general[1] - race.puestosgeneral:
                    ticket = 2
                    break
                else:
                    print('No disponemos de mas puestos')
            else:
                print('Dato invalido')
        return ticket
    #Funcion para obtener el numero de asientos que desea comprar
    def get_seats_amount(self,race,ticket):
            while True:
                print('Elija el numero de asientos')
                n_seats = input('==> ')
                if n_seats.isdigit():
                    if ticket ==1:
                        if 0< int(n_seats) <= race.map.vip[0]*race.map.vip[1] - race.puestosvip:
                            return int(n_seats)
                        else:
                            print('No queda esa cantidad de asientos disponibles en la categoria VIP')
                    else:
                        if 0< int(n_seats) <= race.map.general[0]*race.map.general[1] - race.puestosgeneral:
                            return int(n_seats)
                        else:
                            print('No queda esa cantidad de asientos disponibles en la categoria General')
                else:
                    print('Debe ser un numero')

    def convert_matrix(self,race,mapa,type):
        clave = {0:'O',1:'X',8:'#'}
        if type =='general':
            row_i = '\t   '
            for i in range(len(mapa[0])):
                str = f' |C{i}|'
                row_i = row_i + str
            print(row_i)
            for i in range(len(mapa)):
                row = f'\t F{i}'
                for j in range(len(mapa[i])):
                        seat = f' |{clave[mapa[i][j]]}| '
                        row = row + seat
                print('\t'+race.map.general[1]*'-----')
                print(row)
        elif type =='VIP':
            row_i = '\t   '
            for i in range(len(mapa[0])):
                str = f' |C{i}|'
                row_i = row_i + str
            print(row_i)
            for i in range(len(mapa)):
                row = f'\t F{i}'
                for j in range(len(mapa[i])):
                        seat = f' |{clave[mapa[i][j]]}| '
                        row = row + seat
                print('\t'+race.map.vip[1]*'------')
                print(row) 
    def get_client_seat(self,mapa,race,ticket,n_seats):
        if ticket == 1:
            i = 1
            list_seats = []
            while i < n_seats+1:
                print('\n')
                self.convert_matrix(race,mapa,'VIP')
                print('Puestos ocupados: X')
                print('Puestos libres: O')
                while True:
                    print(f'Elija el {i}º puesto en el formato de fila/columna')
                    fila = input('Fila ==> ')
                    columna = input('Columna ==> ')
                    if fila.isdigit() and columna.isdigit():
                        if -1< int(fila)  < race.map.vip[0] and -1 < int(columna)  < race.map.vip[1] and [int(fila), int(columna)] not in list_seats:
                            seat = [int(fila), int(columna)]
                            if mapa[int(fila)][int(columna)] != 1:
                                mapa[int(fila)][int(columna)]  = 8
                                self.convert_matrix(race,mapa,'VIP')
                                print('El puesto elegido es un signo #')
                                while True:
                                    print('¿Desea confirmar los puestos? [y/n]')
                                    user_input = input('===> ')
                                    if user_input =='y':
                                        list_seats.append(seat)
                                        mapa[int(fila)][int(columna)] =1
                                        i+=1
                                        break
                                    elif user_input =='n':
                                        print('Elija los puestos de nuevo')
                                        break
                                    else:
                                        print('Dato invalido')
                        else:
                            print('Ese puesto esta fuera de las posibles opciones')
                    else:
                        print('Deben ser numeros')
                    break
            return list_seats, mapa

        else:
            i = 1
            list_seats = []
            while i<n_seats+1:
                print('\n')
                self.convert_matrix(race,mapa,'general')
                print('Puestos ocupados: X')
                print('Puestos libres: O')
                while True:
                    print(f'Elija el {i}º puesto en el formato de fila/columna')
                    fila = input('Fila ==> ')
                    columna = input('Columna ==> ')
                    if fila.isdigit() and columna.isdigit():
                        if -1< int(fila)  < race.map.general[0] and -1< int(columna)  < race.map.general[1]  and [int(fila) , int(columna)] not in list_seats:
                            seat = [int(fila) , int(columna)]
                            if mapa[int(fila)][int(columna)]  != 1:
                                mapa[int(fila)][int(columna)] = 8
                                self.convert_matrix(race,mapa,'general')
                                print('El puesto elegido es un signo #')
                                vali = True
                                while vali:
                                    print('¿Desea confirmar el puesto? [y/n]')
                                    user_input = input('===> ')
                                    if user_input =='y':
                                            seat = list(seat)
                                            list_seats.append(seat)
                                            mapa[int(fila)][int(columna)]= 1
                                            i+=1
                                            break
                                    elif user_input =='n':
                                            print('Elija los puestos de nuevo')
                                            break
                                    else:
                                            print('Dato invalido')
                            else:
                                print('Ese puesto ya esta ocupado')
                        else:
                            print('Ese puesto esta fuera de las posibles opciones')
                    else:
                        print('Deben ser numeros')
                    break
            return list_seats, mapa
    def get_seat(self,race,ticket,n_seats):
        if ticket ==1:
            seats= self.get_client_seat(race.mapvip,race,ticket,n_seats)
        else:
            seats= self.get_client_seat(race.mapgeneral,race,ticket,n_seats)
        return seats
    ##Funcion para obetener si hay descuento
    def is_undulating(self,id):
        if len((id)) > 0:
            for i in range(len((id))-2):
                if id[i] < id[i+1] and id[i+1] > id[i+2]:
                    continue
                elif id[i] > id[i+1] and id[i+1] < id[i+2]:
                    continue
                else:
                    return False
        else:
            return False
        return True
    def create_ticket(self,race,seats,ticket,raceob):
        if ticket ==1:
            ticket = TicketVIP(race,seats,[],False)
        else:
            ticket = TicketGeneral(race,seats,[],False)
        ticket.generate_codes(raceob.codes,len(seats))
        return ticket
    #Calculo de la factura y a su vez confirmacion del pago
    def show_tip(self,name,id,age,race,ticket,ids_db,clients_db,seats):
        if self.is_undulating(id):
            subtotal = ticket.price*len(seats)
            descuento = ticket.price*0.5*len(seats)
            impuesto = ticket.price*0.16*len(seats)
            total =  subtotal + impuesto - descuento
            print('\t"""""""FACTURA""""""')
            print(f'Nombre = {name}\t\nID = {id}\t\nCarrera = {ticket.race}\t\nFecha = {race.date}\t\nLocalizacion = {race.circuit.Location.country}\t\nNumero de entrada/s = {len(seats)}\t\nTipo de entrada/s = {ticket.type}\t\nCodigo = {ticket.codes}\t\nPuesto/s = {seats}\t\nSubtotal = {subtotal}\t\nDescuento = {descuento}\t\nImpuesto = {impuesto}\t\nTotal = {total}')
        else: 
            subtotal = ticket.price*len(seats)
            impuesto = ticket.price*0.16*len(seats)
            descuento = 0
            total =  subtotal + impuesto
            print('\t"""""""FACTURA""""""')
            print(f'Nombre = {name}\t\nID = {id}\t\nCarrera = {ticket.race}\t\nFecha = {race.date}\t\nLocalizacion = {race.circuit.Location.country}\t\nNumero de entrada/s = {len(seats)}\t\nTipo de entrada/s = {ticket.type}\t\nCodigo = {ticket.codes}\t\nPuesto/s = {seats}\t\nSubtotal = {subtotal}\t\nDescuento = No posee\t\nImpuesto = {impuesto}\t\nTotal = {total}')
        while True:
            print('¿Desea confirmar la compra? [y/n]')
            user_input = input('==> ')
            if user_input =='y':
                print('¡Muchas gracias por su compra, lo esperamos en la carrera!')
                cliente = Client(name,id,age,[],[],0,0)
                for code in ticket.codes:
                    race.append_code(code)
                cliente.append_ticket(ticket)
                ids_db.append(cliente.id)
                clients_db.append(cliente)
                cliente.total_gastado += total
                if ticket.type == 'VIP': 
                    for seat in seats:
                        race.puestosvip +=1
                        cliente.total_seat +=1
                        race.monto_compras += 340
                else:
                    for seat in seats:
                        race.puestosgeneral +=1
                        cliente.total_seat +=1
                break
            elif user_input =='n':
                print('Estaremos siempe a la orden')
                if ticket.type =='VIP':
                    for seat in seats:
                        race.mapvip[seat[0]][seat[1]] =0
                else:
                    for seat in seats:
                        race.mapgeneral[seat[0]][seat[1]] = 0
                break
            else:
                print('Dato invalido')
    def show_tip_exsiting(self,name,id,age,race,ticket,ids_db,clients_db,seats,cliente):
        if self.is_undulating(id):
            subtotal = ticket.price*len(seats)
            descuento = ticket.price*0.5*len(seats)
            impuesto = ticket.price*0.16*len(seats)
            total =  subtotal + impuesto - descuento
            print('\t"""""""FACTURA""""""')
            print(f'Nombre = {name}\t\nID = {id}\t\nCarrera = {ticket.race}\t\nFecha = {race.date}\t\nLocalizacion = {race.circuit.Location.country}\t\nNumero de entrada/s = {len(seats)}\t\nTipo de entrada/s = {ticket.type}\t\nCodigo = {ticket.codes}\t\nPuesto/s = {seats}\t\nSubtotal = {subtotal}\t\nDescuento = {descuento}\t\nImpuesto = {impuesto}\t\nTotal = {total}')
        else: 
            subtotal = ticket.price*len(seats)
            impuesto = ticket.price*0.16*len(seats)
            descuento = 0
            total =  subtotal + impuesto
            print('\t"""""""FACTURA""""""')
            print(f'Nombre = {name}\t\nID = {id}\t\nCarrera = {ticket.race}\t\nFecha = {race.date}\t\nLocalizacion = {race.circuit.Location.country}\t\nNumero de entrada/s = {len(seats)}\t\nTipo de entrada/s = {ticket.type}\t\nCodigo = {ticket.codes}\t\nPuesto/s = {seats}\t\nSubtotal = {subtotal}\t\nDescuento = No posee\t\nImpuesto = {impuesto}\t\nTotal = {total}')
        while True:
            print('¿Desea confirmar la compra? [y/n]')
            user_input = input('==> ')
            if user_input =='y':
                print('¡Muchas gracias por su compra, lo esperamos en la carrera!')
                for code in ticket.codes:
                    race.append_code(code)
                cliente.append_ticket(ticket)
                cliente.total_gastado += total
                if ticket.type == 'VIP':
                    for seat in seats:
                        race.puestosvip +=1
                        cliente.total_seat +=1
                else:
                    for seat in seats:
                        race.puestosgeneral +=1
                        cliente.total_seat +=1
                break
            elif user_input =='n':
                print('Estaremos siempe a la orden')
                if ticket.type =='VIP':
                    for seat in seats:
                        race.mapvip[seat[0]][seat[1]] =0
                else:
                    for seat in seats:
                        race.mapgeneral[seat[0]][seat[1]] = 0
                break
            else:
                print('Dato invalido')
    ##Funcion para encontrar si el cliente ya se ha registrado en la base de datos
    def find_cliente(self,db,id):
        for client in db:
            if client.id == id:
                return client
    def existing_client(self,client,id,carreras_ob_db,ids_db,clients_db):
        print(f'Su id {client.id} coincide con unos de los ya registrado en nuestra base de datos\n\t¿Querra agregar una entrada mas {client.name}? [y/n]')
        while True:
            user_input = input('==> ')
            if user_input == 'y':
                race = self.get_race(carreras_ob_db)
                ticket1 = self.get_ticket_type(race)
                n_seats = self.get_seats_amount(race,ticket1) 
                seats,mapa = self.get_seat(race,ticket1,n_seats)
                race1 = race.name
                ticket = self.create_ticket(race1,seats,ticket1,race) 
                self.show_tip_exsiting(client.name,id,client.age,race,ticket,ids_db,clients_db,seats,client)
                break
            elif user_input =='n':
                print('Siempre estaremos a la orden')
                break
            else:
                print('Dato invalido')
    def index_1(self,carreras_ob_db,ids_db,clients_db):
            id = self.get_data('Cedula','numero')
            if id not in ids_db:
                name = self.get_data('Nombre','letra')
                age = self.get_data('Edad','numero')
                race = self.get_race(carreras_ob_db)
                ticket1 = self.get_ticket_type(race)
                n_seats = self.get_seats_amount(race,ticket1) 
                seats,mapa = self.get_seat(race,ticket1,n_seats)
                race1 = race.name
                ticket = self.create_ticket(race1,seats,ticket1,race)
                self.show_tip(name,id,age,race,ticket,ids_db,clients_db,seats)
            else:
                client = self.find_cliente(clients_db,id)
                self.existing_client(client,id,carreras_ob_db,ids_db,clients_db)
    ##Inicializacion del Modulo
    def startgestionVE(self,carreras_ob_db,id_registered_db,cliens_ob_db):
        while True:
            print('Elija una de las siguientes opciones\t\n1. Desea comprar una entrada para una carrera\t\n2. Salir')
            user_input = input('==> ')
            if user_input =='1':
                self.index_1(carreras_ob_db,id_registered_db,cliens_ob_db)
            elif user_input =='2':
                break
            else:
                print('Dato invalido')