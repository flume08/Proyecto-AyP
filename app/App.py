import json
import requests
from Constructores import Constructor
from Pilotos import Pilot
from Items import Item, DrinkAlcohol, DrinkNonAlcoholic, FoodFast, FoodRestaurant
from Restaurantes import Restaurant
from Location import Location
from Circuitos import Circuit
from Map import Map
from Carreras import Race
from Tickets import Ticket, TicketVIP, TicketGeneral
from Client import Client
from Compras import Compra
from GestionCyE import GestionCyE
from GestionVE import GestionVE
from GestionAdC import GestionAdC
from GestionR import GestionR
from GestionVdR import GestionVdR
from GestionED import GestionED
import os 
class App:
    ##  Incializacion de las bases de datos
    pilotos_db = []
    constructores_db = []
    carreras_db = []
    pilotos_db_ob = []
    constructores_db_ob = []
    carreras_db_ob = []
    carreras_sin_terminar_ob = []
    carreras_terminadas_ob = []
    clients_ob_db = []
    id_registered_db = []
    ## Get data de la API y creacion de objetos
    def load_api(self):
        url_pilotos = 'https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/drivers.json'
        url_constructores = 'https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/constructors.json'
        url_carreras = 'https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json'
        resp_pilotos = requests.get(url_pilotos)
        resp_constructores = requests.get(url_constructores)
        resp_carreras = requests.get(url_carreras)
        db_pilotos = json.loads(resp_pilotos.text)
        db_constructores = json.loads(resp_constructores.text)
        db_carreras = json.loads(resp_carreras.text)
        return db_pilotos,db_constructores,db_carreras
    def create_obs(self,db_pilotos,db_constructores,db_carreras):
        for p in db_pilotos:
            piloto = Pilot(p['id'],p['permanentNumber'],p['code'],p['team'],p['firstName'],p['lastName'],p['dateOfBirth'],p['nationality'],0)
            self.pilotos_db_ob.append(piloto)
        for c in db_constructores:
            pilotos = []
            for p in self.pilotos_db_ob:
                if c['id'] == p.team:
                    pilotos.append(p)
            constructor = Constructor(c['id'],c['name'],c['nationality'],pilotos)
            self.constructores_db_ob.append(constructor)
        i = 0
        for carrera in db_carreras:
            location = Location(carrera['circuit']['location']['lat'],carrera['circuit']['location']['long'],carrera['circuit']['location']['locality'],carrera['circuit']['location']['country'])
            circuit = Circuit(carrera['circuit']['circuitId'],carrera['circuit']['name'],location)
            map = Map(carrera['map']['general'],carrera['map']['vip'])
            restaurants = []
            for r in carrera['restaurants']:
                items = []
                for item in r['items']:
                    if item['type'] == 'food:restaurant':
                        item_ob = FoodRestaurant(item['name'],item['price'])
                        items.append(item_ob)
                    elif item['type'] == 'food:fast':
                        item_ob = FoodFast(item['name'],item['price'])
                        items.append(item_ob)
                    elif item['type'] == 'drink:alcoholic':
                        item_ob = DrinkAlcohol(item['name'],item['price'])
                        items.append(item_ob)
                    elif item['type'] == 'drink:not-alcoholic':
                        item_ob = DrinkNonAlcoholic(item['name'],item['price'])
                        items.append(item_ob)
                restaurant_ob = Restaurant(r['name'],items)
                restaurants.append(restaurant_ob)
            carrera_ob = Race(carrera['round'],carrera['name'],circuit,map,carrera['date'],restaurants,[],[],0,0,0,0)
            self.carreras_db_ob.append(carrera_ob)
            self.carreras_sin_terminar_ob.append(i)
            i +=1
    ## Creacion de las instacias de los modulos
    def gestionEyC(self):
        EyC = GestionCyE()
        EyC.start_gestionEyC(self.pilotos_db_ob,self.constructores_db_ob,self.carreras_db_ob,self.carreras_terminadas_ob,self.carreras_sin_terminar_ob)
    def gestionVE(self):
        VyE = GestionVE()
        VyE.startgestionVE(self.carreras_db_ob,self.id_registered_db,self.clients_ob_db)
    def gestionAdC(self):
        AdC = GestionAdC()
        AdC.start_gestionAdC(self.carreras_db_ob,self.clients_ob_db)
    def gestionRE(self):
        Re = GestionR()
        Re.startR(self.carreras_db_ob)
    def gestionVdR(self):
        VdR = GestionVdR()
        VdR.startVdR(self.carreras_db_ob,self.clients_ob_db)
    def gestionED(self):
        ED = GestionED()
        ED.startED(self.carreras_db_ob,self.clients_ob_db)
    ## Cargar la data obtenida en una corrida del programa al formato JSON y luego subirla al txt
    def upload_txt(self):
        pilotos_db_dicc = []
        constructores_db_dicc = []
        carreras_db_dicc = []
        clients_ob_dicc = []
        id_registered = []
        for pilot in self.pilotos_db_ob:
            pilotos_db_dicc.append((vars(pilot)))
        for constructor in self.constructores_db_ob:
            constructores_db_dicc.append((constructor.dicc()))
        for carrera in self.carreras_db_ob:
            carreras_db_dicc.append((carrera.dicc()))
        for client in self.clients_ob_db:
            clients_ob_dicc.append(client.dicc())
        for id in self.id_registered_db:
            id_registered.append(id)
        db = {
            "Pilotos Db":pilotos_db_dicc,
            "Constructores Db":constructores_db_dicc,
            "Carreras Db" : carreras_db_dicc,
            "Carreras sin terminar Db": self.carreras_sin_terminar_ob,
            "Carreras terminadas Db":self.carreras_terminadas_ob,
            "Clientes Db": clients_ob_dicc,
            "IDs":id_registered
        }
        with open('database.txt', 'w') as file:
            file.write(str(json.dumps(db)))
    ## Borrar la data del txt
    def delete_db(self):
        with  open('database.txt', 'w') as file:
            file.write('')
    ## Cargar la data del txt
    def load_txt(self):
        with open('database.txt', 'r') as file:
            db = json.loads(file.read())
            for p in db['Pilotos Db']:
                    p = Pilot(p['driverId'],p['permanentNumber'],p['code'],p['team'],p['firstName'],p['lastName'],p['dateOfBirth'],p['nationality'],p['points'])
                    self.pilotos_db_ob.append(p)
            for c in db['Constructores Db']:
                pilotos = []
                for p in self.pilotos_db_ob:
                    if c['id'] == p.team:
                        pilotos.append(p)
                constructor = Constructor(c['id'],c['name'],c['nationality'],pilotos)
                self.constructores_db_ob.append(constructor)
            for carrera in db['Carreras Db']:
                location = Location(carrera['circuit']['Location']['lat'],carrera['circuit']['Location']['long'],carrera['circuit']['Location']['locality'],carrera['circuit']['Location']['country'])
                circuit = Circuit(carrera['circuit']['circuitid'],carrera['circuit']['name'],location)
                map = Map(carrera['map']['general'],carrera['map']['vip'])
                restaurants = []
                for r in carrera['restaurants']:
                    items = []
                    for item in r['items']:
                        if item['type'] == 'Comida de restaurant':
                            item_ob = FoodRestaurant(item['name'],item['price'],item['sell'])
                            items.append(item_ob)
                        elif item['type'] == 'Comida Rapida':
                            item_ob = FoodFast(item['name'],item['price'],item['sell'])
                            items.append(item_ob)
                        elif item['type'] == 'Bebida Alcoholica':
                            item_ob = DrinkAlcohol(item['name'],item['price'],item['sell'])
                            items.append(item_ob)
                        elif item['type'] == 'Bebida no alcoholica':
                            item_ob = DrinkNonAlcoholic(item['name'],item['price'],item['sell'])
                            items.append(item_ob)
                    restaurant_ob = Restaurant(r['name'],items)
                    restaurants.append(restaurant_ob)
                carrera_ob = Race(carrera['round'],carrera['name'],circuit,map,carrera['date'],restaurants,carrera['podium'],carrera['codes'],carrera['assistance'],carrera['puestosvip'],carrera['puestosgeneral'],carrera['monto'])   
                carrera_ob.mapvip = carrera['mapvip']
                carrera_ob.mapgeneral = carrera['mapgeneral']
                self.carreras_db_ob.append(carrera_ob)
            for client in db['Clientes Db']:
                tickets = []
                compras = []
                for ticket in client['tickets']:
                    if ticket['type'] == 'VIP':
                        ticket_ob = TicketVIP(ticket['race'],ticket['seats'],ticket['codes'],ticket['attendance'])
                        tickets.append(ticket_ob)
                    else:
                        ticket_ob = TicketGeneral(ticket['race'],ticket['seats'],ticket['codes'],ticket['attendance'])
                        tickets.append(ticket_ob)
                for compra in client['compras']:
                    items=[]
                    for item in compra['items']:
                        if item['type'] == 'Comida de restaurant':
                            item_ob = FoodRestaurant(item['name'],item['price'],item['sell'])
                            items.append(item_ob)
                        elif item['type'] == 'Comida Rapida':
                            item_ob = FoodFast(item['name'],item['price'],item['sell'])
                            items.append(item_ob)
                        elif item['type'] == 'Bebida Alcoholica':
                            item_ob = DrinkAlcohol(item['name'],item['price'],item['sell'])
                            items.append(item_ob)
                        elif item['type'] == 'Bebida no alcoholica':
                            item_ob = DrinkNonAlcoholic(item['name'],item['price'],item['sell'])
                            items.append(item_ob)
                    compra = Compra(compra['id'],compra['total'],items)
                    compras.append(compra)
                client_ob = Client(client['name'],client['id'],client['age'],tickets,compras,client['Total Gastado'],client['total seats'])
                self.clients_ob_db.append(client_ob)
            for id in db['IDs']:
                self.id_registered_db.append(id)
            self.carreras_sin_terminar_ob = db['Carreras sin terminar Db']
            self.carreras_terminadas_ob = db['Carreras terminadas Db']
    ## Incializcion de la app revisando que exista o no txt y si hay conexion al WIFI
    def start(self):
        if os.path.exists('database.txt'):
            with open('database.txt', 'r') as file:
                n = len(file.read())
            if n>1:
                self.load_txt()
            else:
                try:
                    request = requests.get( 'https://www.google.com',timeout=5)
                except (requests.ConnectionError, requests.Timeout):
                            print("Sin conexión a internet.")
                            exit()
                else:
                    db_pilotos,db_constructores,db_carreras = self.load_api()
                    self.create_obs(db_pilotos,db_constructores,db_carreras)
        else:
            db_pilotos,db_constructores,db_carreras = self.load_api()
            self.create_obs(db_pilotos,db_constructores,db_carreras)
            try:
                request = requests.get( 'https://www.google.com',timeout=5)
            except (requests.ConnectionError, requests.Timeout):
                print("Sin conexión a internet.")
                exit()
        str =  "                                     d88b"
        str2 = "                     _______________|8888|_______________"
        str3 = "                    |_____________ ,~~~~~~. _____________|"
        str4 = "  _________         |_____________: mmmmmm :_____________|         _________"
        str5 = " / _______ \   ,----|~~~~~~~~~~~,'\ _...._ /`.~~~~~~~~~~~|----,   / _______ \ "
        str6 = "| /       \ |  |    |       |____|,d~    ~b.|____|       |    |  | /       \ |"
        str7 = "||         |-------------------\-d.-~~~~~~-.b-/-------------------|         ||"
        str8 = "||         | |8888 ....... _,===~/......... \~===._         8888| |         ||"
        str9 = "||         |=========_,===~~======._.=~~=._.======~~===._=========|         ||"
        str10 ="||         | |888===~~ ...... //,, .`~~~~'. .,\ \       ~~===888| |         ||"
        str11 ="||        |===================,P'.::::::::.. `?,===================|        ||"
        str12 ="||        |_________________,P'_::----------.._`?,_________________|        ||"
        str13 ="`|        |-------------------~~~~~~~~~~~~~~~~~~-------------------|        |'"
        str14 ="  \_______/                                              _ Louis _  \_______/"
        print(str)
        print(str2)
        print(str3)
        print(str4)
        print(str5)
        print(str6)
        print(str7)
        print(str8)
        print(str9)
        print(str10)
        print(str11)
        print(str12)
        print(str13)
        print(str14)
        str =  "  __                           _       __ "
        str2 = " / _|                         | |     /  |"
        str3 = "| |_ ___  _ __ _ __ ___  _   _| | __ _`| |"
        str4 = "|  _/ _ \| '__| '_ ` _ \| | | | |/ _` || |"
        str5 = "| || (_) | |  | | | | | | |_| | | (_| || |_"
        str6 = "|_| \___/|_|  |_| |_| |_|\__,_|_|\__,_\___/"
        print(str)
        print(str2)
        print(str3)
        print(str4)
        print(str5)
        print(str6)
        print('\n')
        print('Bienvendios a la base de datos de la temporada 2023 de la Fórmula 1')
        print('\n')
        print('\n')
        while True:
            print('Elija uno de los siguientes modulos de gestion\t\n1. Gestión de carreras y equipo\t\n2. Gestión de venta de entradas\
                  \t\n3. Gestión de asistencia a las carreras\t\n4. Gestión de restaurantes\t\n5. Gestión de venta de restaurantes\t\n6. Indicadores de gestion\t\n7. Cargar datos a la db\t\n8.Borrar datos de la db y salir\t\n9. Salir')
            user_input = input('==> ')
            if user_input =='1':
                self.gestionEyC()
            elif user_input =='2':
                self.gestionVE()
            elif user_input =='3':
                self.gestionAdC()
            elif user_input =='4':
                self.gestionRE()
            elif user_input =='5':
                self.gestionVdR()
            elif user_input =='6':
                self.gestionED()
            elif user_input =='7':
                self.upload_txt()
            elif user_input =='8':
                self.delete_db()
                break
            elif user_input =='9':
                self.upload_txt()
                break
            else:
                print('Dato invalido')