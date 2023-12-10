import random as r
class GestionCyE:

## Funciones para la opcion de mostrar las constructoras por pais

    def get_countries(self,db):
        countries = set()
        for constructor in db:
            countries.add(constructor.nationality)
        countries = list(countries)
        return countries
    def get_user_countrie(self,countries):
        i = 1
        print('Elija uno de las siguientes nacionalidades disponibles')
        for country in countries:
            print(f'{i}. {country}')
            i +=1
        while True:
            user_input = input('==> ')
            if user_input.isdigit():
                if 0 < int(user_input) < len(countries)+1:
                    countrie = countries[int(user_input)-1]
                    break
                else:
                    print('Dato invalido')
            else:
                print('Dato invalido')
        return countrie
    def show_cosntructures_countrie(self,db,countrie):
        for constructor in db:
            if constructor.nationality == countrie:
                constructor.show_attributes()
    def index_1 (self,db1):
            countries = self.get_countries(db1)
            countrie = self.get_user_countrie(countries)
            self.show_cosntructures_countrie(db1, countrie)
##Funciones para mostrar los pilotos por constructora

    def get_user_constructor(self,constructores):
        i = 1
        print('Elija uno de las siguientes escuderas disponibles')
        for constructor in constructores:
            print(f' {i}.{constructor.name}')
            i+=1
        while True:
            user_input = input('==> ')
            if user_input.isdigit():
                if 0 < int(user_input) < len(constructores)+1:
                    constructor = constructores[int(user_input)-1]
                    break
                else:
                    print('Dato invalido')
            else:
                print('Dato invalido')
        return constructor
    def show_pilot_constructure(self,constructor):
        for pilot in constructor.pilotos:
            print('\n')
            pilot.show_attributes()

    def index_2(self,db1):
            constructor = self.get_user_constructor(db1)
            self.show_pilot_constructure(constructor)

##Funciones para mostrar las carreras por pais

    def get_countries2(self,db):
        countries = set()
        for race in db:
            countries.add(race.circuit.Location.country)
        countries = list(countries)
        return countries

    def get_user_countrie_race(self,countries):
        print('Elija una de las siguientes localidades disponibles')
        i = 1
        for countrie in countries:
                print(f' {i}.{countrie}')
                i+=1
        while True:
            user_input = input('==> ')
            if user_input.isdigit():
                if 0 < int(user_input) < len(countries)+1:
                    countrie = countries[int(user_input)-1]
                    break
                else:
                    print('Dato invalido')
            else:
                print('Dato invalido')
        return countrie
        
    def show_race_countrie(self,db,countrie):
        for race in db:
            if race.circuit.Location.country == countrie:
                race.show_name()

    def index_3(self,db1):
            countries = self.get_countries2(db1)
            countrie = self.get_user_countrie_race(countries)
            self.show_race_countrie(db1,countrie)
## Funciones de msotrar las carreras por un mes elegido

    
    def get_dates(self,db):
        dates = set()
        for race in db:
            dates.add(race.date)
        dates = list(dates)
        return dates
    def get_user_dates(self,dates):
        i = 1
        month_dict = {
            '01': "Enero",
            '02': "Febrero",
            '03': "Marzo",
            '04': "Abril",
            '05': "Mayo",
            '06': "Junio",
            '07': "Julio",
            '08': "Agosot",
            '09': "Septiembre",
            '10': "Octubre",
            '11': "Noviembre",
            '12': "Diciembre"
                }
        print('Elija uno de las siguientes fechas disponibles')
        for date in dates:
            mes = month_dict[date[5:7]]
            print(f'{i}. Año:{date[0:4]}-Mes:{mes}-Dia:{date[8:]}')
            i +=1
        while True:
            user_input = input('==> ')
            if user_input.isdigit():
                if 0 < int(user_input) < len(dates)+1:
                    date = dates[int(user_input)-1]
                    break
                else:
                    print('Dato invalido')
            else:
                print('Dato invalido')
        return date
    def show_race_date(self,db,date):
        for race in db:
            if race.date == date:
                print(f'{race.name} - {race.circuit.Location.country}')
    def index_4 (self,db1):
            dates = self.get_dates(db1)
            date = self.get_user_dates(dates)
            self.show_race_date(db1, date)
## Funciones para poder realizar la accion de terminar la carrera

    def pilotos_sin_puesto(self,pilotos_db):
        pilotos_sin_puesto = []
        for pilot in pilotos_db:
            pilotos_sin_puesto.append(pilot.permanentNumber)
        return pilotos_sin_puesto
    def get_race(self,carreras_sin_terminar,carreras_db):
        races = []
        print('Elija la carrera que desea asignar el podium')
        i = 1
        for race in carreras_sin_terminar:
            races.append(carreras_db[race])
        for race1 in races:
            print(f'==> {i}.{race1.name}')
            i+=1
        while True:
            user_input = input('==> ')
            if user_input.isdigit():
                if 0 < int(user_input) < len(races)+1:
                    carrera = races[int(user_input)-1]
                    break
                else:
                    print('Dato invalido')
            else:
                print('Dato invalido')
        return carrera
    def genearate_podium(self,pilotos_sin_puesto):
            r.shuffle(pilotos_sin_puesto)
            return pilotos_sin_puesto
    def show_podium(self,podium,pilotos_db):
        i=1
        for number in podium:
            for pilot in pilotos_db:
                if pilot.permanentNumber == number:
                    print(f'{i}º puesto: ')
                    pilot.show_attributes()
                    print('\n')
                    i +=1
    def get_points_pilot(self,race,pilotos_db):
        points = [25,18,15,12,10,8,6,4,2,1,0,0,0,0,0,0,0,0,0,0]
        for position in race.podium:
                index = race.podium.index(position)
                for pilot in pilotos_db:
                    if pilot.permanentNumber == position:
                        pilot.get_placement(points[index])
    def get_points_constructor(self,construcotres_db):
        for constructor in construcotres_db:
            constructor.sum_points()
    def get_firts_place_pilot(self,pilotos_db):
        pilots = []
        for pilot in pilotos_db:
            pilots.append(pilot)
        pilots.sort(key=lambda x:x.points,reverse=True)
        return pilots[0]
    def get_first_place_constructor(self,construcotres_db):
        cnst = []
        for const in construcotres_db:
            cnst.append(const)
        cnst.sort(key=lambda x:x.points,reverse=True)
        return cnst[0]
    def index_5(self,pilotos_db,carreras_terminadas,carreras_sin_terminar,constructores_db,carreras_db):
        pilotos_sin_puesto = self.pilotos_sin_puesto(pilotos_db)
        carrera = self.get_race(carreras_sin_terminar,carreras_db)
        podium = self.genearate_podium(pilotos_sin_puesto)
        carrera.get_podium(podium)
        index = carreras_db.index(carrera)
        carreras_sin_terminar.remove(index)
        carreras_terminadas.append(index)
        self.get_points_pilot(carrera,pilotos_db)
        self.show_podium(podium,pilotos_db)
        if len(carreras_sin_terminar) > 0:
            print(f'Quedan {len(carreras_sin_terminar)} carreras sin terminar')
        else:
            pilot1= self.get_firts_place_pilot(pilotos_db)
            self.get_points_constructor(constructores_db)
            constructora1= self.get_first_place_constructor(constructores_db)
            print('YA SE HA TERMINADO LA LIGA 2023 DE FORMULA 1')
            print('EL piloto que obtuvo mas puntos en la temporada fue:')
            pilot1.show_attributes()
            print('\n')
            print('La constructora con mas puntos fue:')
            constructora1.show_attributes()

## Funciones para poder visualizar la tabla de posiciones de las carreras

    def show_points(self,db2):
            i = 1
            pilots=[]
            for pilot in db2:
                pilots.append(pilot)
            pilots.sort(key=lambda x:x.points,reverse=True)
            for pilot in pilots:
                print(f'{i}º puesto: ')
                pilot.show_attributes()
                print('\n')
                i +=1
    def index_6(self,pilotos_db):
        self.show_points(pilotos_db)
    #Funcion para mostrar nuevamente los resultados finales
    def index_7(self,piltos_db,constuc_db):
        pilot1= self.get_firts_place_pilot(piltos_db)
        constructora1= self.get_first_place_constructor(constuc_db)
        print('YA SE HA TERMINADO LA LIGA 2023 DE FORMULA 1')
        print('EL piloto que obtuvo mas puntos en la temporada fue:')
        pilot1.show_attributes()
        print('\n')
        print('La constructora con mas puntos fue:')
        constructora1.show_attributes()
    ##Incializacion del modulo
    def start_gestionEyC(self,pilotos_db_ob,constructores_db_ob,carreras_db_ob,carreras_terminadas_db,carreras_sin_terminar_db):
        print('Bienvendio al modulo de gestion de carreras')
        while True:
            print('Elija una de las siguientes opciones\t\n1. Buscar a los constructores por pais\t\n2. Buscar a los pilotos por constructor\
                  \t\n3. Buscar a las carreras por pais de circuito\t\n4. Buscar a las carreras que ocurran por fecha\t\n5. Cargar resultados de carrera\t\n6. Ver la tabla de puntaje de las carreras ya realizadas\t\n7. Ver los resultados finales\t\n8. Salir')
            user_input = input('==> ')
            if user_input =='1':
                self.index_1(constructores_db_ob)
            elif user_input =='2':
                self.index_2(constructores_db_ob)
            elif user_input =='3':
                self.index_3(carreras_db_ob)
            elif user_input =='4':
                self.index_4(carreras_db_ob)
            elif user_input=='5':
                if len(carreras_sin_terminar_db)>0:
                    self.index_5(pilotos_db_ob,carreras_terminadas_db,carreras_sin_terminar_db,constructores_db_ob,carreras_db_ob)
                else:
                    print('Ya la temporada se cargo, elija la opcion 6 para poder visualizar la tabla de puntos')
                    print(carreras_sin_terminar_db)
            elif user_input =='6':
                if len(carreras_terminadas_db) > 0:
                    self.index_6(pilotos_db_ob)
                else:
                    print('No se ha registrado ninguna carrera')
            elif user_input =='7':
                if len(carreras_sin_terminar_db) != 0:
                    print('La temporada aun no se ha terminado')
                else:
                    self.index_7(pilotos_db_ob,constructores_db_ob)
            elif user_input =='8':
                break
            else:
                print('Input invalido')