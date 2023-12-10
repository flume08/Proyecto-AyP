import numpy as np
class Race:
    def __init__(self,round,name,circuit,map,date,restaurants,podium,codes,assistance,puestosvip,puestosgeneral,monto_compras):
        self.round = round
        self.name = name
        self.circuit = circuit
        self.map = map
        self.mapvip = map.get_mapvip()
        self.mapgeneral = map.get_mapgeneral()
        self.date = date
        self.restaurants = restaurants
        self.podium = podium
        self.codes = codes
        self.assistance = assistance
        self.puestosvip = puestosvip
        self.puestosgeneral = puestosgeneral
        self.monto_compras = monto_compras
    def monto(self,monto):
        self.monto_compras += monto
    def get_podium(self,podium):
        self.podium = podium
    def show_attributes(self):
        print('\n')
        print(f'Round ==> {self.round}')
        print(f'Name ==> {self.name}')
        print(f'Circuit ==>')
        self.circuit.show_attributes()
        print(f'Date ==> {self.date}')
        print(f'Restaurats ==>')
        for restaurant in self.restaurants:
            restaurant.show_attributes()
    def show_name(self):
        print(f'Race Name ==> {self.name}')
    def append_clients(self,client):
        self.clients.append(client)
    def append_code(self,code):
        self.codes.append(code)
    def restaurant_dicc(self):
        restaurant_dicc = []
        for restaurant in self.restaurants:
            restaurant_dicc.append(restaurant.dicc())
        return restaurant_dicc
    def client_dicc(self):
        clients_dicc = []
        for client in self.clients:
             clients_dicc.append(client.dicc())
        return clients_dicc
    def compra_dicc(self):
        compras_dicc = []
        for compra in self.compras:
            compras_dicc.append(vars(compra))
    def dicc(self):
        return {
            "round": self.round,
            "name":self.name,
            "circuit":self.circuit.dicc(),
            "map":vars(self.map),
            "mapvip":self.mapvip,
            "mapgeneral":self.mapgeneral,
            "date":self.date,
            "restaurants":self.restaurant_dicc(),
            "podium":self.podium,
            "codes":self.codes,
            "assistance":self.assistance,
            "puestosvip":self.puestosvip,
            "puestosgeneral":self.puestosgeneral,
            "monto":self.monto_compras
        }