class GestionR:
    ##Funcion para seleccionar la carrera
    def get_race(self,carreras_ob_db):
        print('Elija la carrera')
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
    ##Funciones para mostrar los productos por nombre

    def get_restaurant(self,carrera):
        i = 1
        for restaurant in carrera.restaurants:
            print(f'==> {i}.{restaurant.name}')
            i+=1
        while True:
            user_input = input('==> ')
            if user_input.isdigit():
                if 0 < int(user_input) < len(carrera.restaurants)+1:
                    restaurant = carrera.restaurants[int(user_input)-1]
                    break
        return restaurant
    def show_items_name(self,restaurant):
        for item in restaurant.items:
            item.show_attributes()
    def index_1(self,carrera):
        restaurant = self.get_restaurant(carrera)
        self.show_items_name(restaurant)
    ##Funciones para mostrar los items por tipo
    def get_types(self,carrera):
        types = set()
        for restaurant in carrera.restaurants:
            for item in restaurant.items:
                types.add(item.type)
        types = list(types)
        return types
    def get_user_type(self,types):
        i = 1
        print('Elija uno de las siguientes nacionalidades disponibles')
        for type in types:
            print(f'{i}. {type}')
            i +=1
        while True:
            user_input = input('==> ')
            if user_input.isdigit():
                if 0 < int(user_input) < len(types)+1:
                    type = types[int(user_input)-1]
                    break
                else:
                    print('Dato invalido')
            else:
                print('Dato invalido')
        return type
    def show_items_type(self,race,type):
        for restaurant in race.restaurants:
           for item in restaurant.items:
                if type == item.type:
                    item.show_attributes()
    def index_2(self,carrera):
        types = self.get_types(carrera)
        type = self.get_user_type(types)
        self.show_items_type(carrera,type)
    ##Funciones para ver items por rango de precio
    def get_range(self):
        while True:
            print('Elija el los extremos del rango de precio que desea buscar')
            cota_inferior = input('Cota Inferior ==> ')
            cota_superior = input('Cota Superior ==> ')
            if cota_inferior.isdigit() and cota_superior.isdigit() and int(cota_inferior) < int(cota_superior):
                return int(cota_inferior), int(cota_superior)
            elif cota_inferior.isdigit() and cota_superior.isdigit() and int(cota_inferior) > int(cota_superior):
                print('Los numeros dados tienen que estar en orden')
            else:
                print('Tienen que ser numeros')
    def show_items_range(self,carrera,cota_inferior,cota_superior):
        for restaurant in carrera.restaurants:
            for item in restaurant.items:
                if cota_inferior < item.price < cota_superior:
                    item.show_attributes()
    def index_3(self,carrera):
        cota_inferior, cota_superior = self.get_range()
        self.show_items_range(carrera,cota_inferior,cota_superior)
    ##Metodo de la clase start para llamarlo en app
    def startR(self,carres_ob_db):
        carrera = self.get_race(carres_ob_db)
        while True:
                    print('Elija una de las siguientes opciones\t\n1. Buscar items por nombre\t\n2. Buscar productos por tipo\t\n3. Buscar productos por rango de precio\t\n4. Salir')
                    user_input = input('==> ')
                    if user_input =='1':
                        self.index_1(carrera)
                    elif user_input =='2':
                        self.index_2(carrera)
                    elif user_input =='3':
                        self.index_3(carrera)
                    elif user_input =='4':
                        break
                    else:
                        print('Dato invalido')