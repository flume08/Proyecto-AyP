from Compras import Compra
class GestionVdR:
    ##Funcion para obtener la carrera
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
                    if len(carrera.restaurants) > 0:
                        return carrera
                    else:
                        print('Esa carrera no posee restaurantes')
                        break
    ## Funciones que sirven para validar y obtener la info del cliente VIP de la carrera
    def get_id(self):
        while True:
            print('Ingrese su id')
            id = input('==> ')
            if id.isdigit():
                return id
            else:
                print('Deben ser numeros')
    def validate_id(self,clients_db,id):
        for client in clients_db:
            if client.id == id:
                return client
        return False 
    def validate_VIP(self,client):
        tickets = []
        for ticket in client.tickets:
            if ticket.type =='VIP':
                tickets.append(ticket)
        if len(tickets) > 0:
            return tickets
        else:
            return False
    def validate_race(self,tickets,race):
        for ticket in tickets:
            if ticket.race ==race.name:
                return ticket
        return False
    def validate_age(self,client):
        if int(client.age) > 18:
            return True
        else:
            return False
    ## Funcion que valida todo lo anterior
    def validate_all(self,carrera,id,clients_db):
                if self.validate_id(clients_db,id):
                    client = self.validate_id(clients_db,id)
                    if self.validate_VIP(client):
                        tickets = self.validate_VIP(client)
                        if self.validate_race(tickets,carrera):
                            ticket = self.validate_race(tickets,carrera)
                            return carrera,client,ticket
                        else:
                            print('Posee un ticket VIP pero no es de esta carrera')
                            return False
                    else:
                        print('Ese ID no tiene ninguna entrada VIP asociada en esta carrera')
                        return False
                else:
                    print('Ese id no esta registrado en la carrera|LLAMAREMOS A SEGURIDAD')
                    return False
    ##Funcion que muestra la lista de restaurantes disponibles en la carrera
    def get_restaurant(self,carrera):
        i = 1
        for restaurant in carrera.restaurants:
                print(f'==> {i}.{restaurant.name}')
                i+=1
        while True:
                print('Elija el restaurante que desea ver sus items, si desea retirarse presione "n"')
                user_input = input('==> ')
                if user_input.isdigit():
                    if 0 < int(user_input) < len(carrera.restaurants)+1:
                        restaurant = carrera.restaurants[int(user_input)-1]
                        return True, restaurant
                elif user_input =='n':
                    return False, None
    ## Funcion que muestra y da la opcion de elegir 1 o mas items en el restaurante
    def get_items(self,restaurant,client):
        vali = True
        items_comprados = []
        while True:
            i = 1
            for item in restaurant.items:
                print(f'==> {i}. Nombre: {item.name} - Precio: {int(item.price)} - Tipo: {item.type} - Stock {item.stock}')
                print('\n')
                i+=1
            print('Elija el item que desea comprar, si no desea nada de aca escriba "n"')
            item = input('==> ')
            if item.isdigit():
                if 0 < int(item) < len(restaurant.items)+1:
                    item = restaurant.items[int(item)-1]
                    if item.stock > 0:
                        if item.type == 'Bebida Alcoholica':
                            if self.validate_age(client):
                                items_comprados.append(item)
                                item.stock -=1
                            else:
                                print('Debes ser mayor de edad para poder comprar bebidad alcoholicas')
                        else:
                            items_comprados.append(item)
                            item.stock -=1
                    else:
                        print('No queda stock de ese item')
                    while True:
                        print('Desea comprar otro item [y/n]')
                        user_input = input('==> ')
                        if user_input =='y':
                                break
                        elif user_input =='n':
                            print('Gracias por su compra!')
                            return False,items_comprados
                        else:
                            print('Dato invalido')
            elif item == 'n':
                return True,items_comprados
    ## Funcion para revisar si el subtotal de la compra es un numero feliz para asignar descuento
    def is_happy_number(self,num):
        seen = set()
        while num not in seen:
            seen.add(num)
            num = sum(int(digit)**2 for digit in str(num))
            if num == 1:
                return True
        return False
    ##Funciones que obtienen el total, subtotal y descuento si existe y confirman la compra del cliente
    def get_price(self,items):
        price = 0 
        for item in items:
            price += item.price
        return price
    def show_tip(self,carrera,client,items,price,ticket,id,carreras_db,cliente):
        if self.is_happy_number(int(client.id)):
            descuento = price*0.15
            total = int(price) - descuento
            print('\t"""""""FACTURA""""""')
            print(f'Posee descuento\t\nNombre = {client.name}\t\nID = {client.id}\t\nNumero de producto/s = {len(items)}\t\nSubtotal = {price}\t\nDescuento = {descuento}\t\nTotal = {total}')
        else:
            descuento = 0
            total = price - descuento
            print('\t"""""""FACTURA""""""')
            print(f'Nombre = {client.name}\t\nID = {client.id}\t\nNumero de producto/s = {len(items)}\t\nSubtotal = {price}\t\nDescuento = {descuento}\t\nTotal = {total}')
        while True:
            print('¿Desea confirmar la compra? [y/n]')
            user_input = input('==> ')
            if user_input =='y':
                print('¡Muchas gracias por su compra, lo esperamos en la carrera!')
                compra = Compra(id,total,items)
                for item in items: 
                    item.add_sell()
                client.compras.append(compra)
                carrera.monto(total)
                cliente.total_gastado += total
                break
            elif user_input =='n':
                print('Estaremos siempe a la orden')
                for item in items:
                    item.stock +=1
                break
            else:
                print('Dato invalido')
    ##Metodo para iniciar el modulo en app
    def startVdR(self,carreras_ob_db,clients_db):
        carrera = self.get_race(carreras_ob_db)
        id = self.get_id()
        if self.validate_all(carrera,id,clients_db):
            carrera,client,ticket = self.validate_all(carrera,id,clients_db)
            while True:
                print(f'Bienvenido {client.name} a la zona de restaurantes de la carrera, elija una de las siguientes opciones\n1. Comprar en una de los restaurantes disponibles en la carrera\n 2. Salir')
                user_input = input('==> ')
                if user_input == '1':
                    list_items = []
                    vali = True
                    while vali:
                        vali,restaurant = self.get_restaurant(carrera)
                        if not vali:
                            break
                        else:
                            vali,items = self.get_items(restaurant,client)
                            for item in items:
                                list_items.append(item)
                    if len(list_items) > 0:
                        price = self.get_price(list_items)
                        self.show_tip(carrera,client,list_items,price,ticket,id,carreras_ob_db,client)
                    else:
                        print('Siempre a la orden')
                elif user_input =='2':
                    break
                else:
                    print('Dato invalido')