import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
class GestionED:
    ##Funcion general para generar un grafico de 2 dimensiones
    def graph(self,db1,db2,nombre):
        fig, ax = plt.subplots(figsize =(16, 9))
        ax.barh(db1, db2)
        for s in ['top', 'bottom', 'left', 'right']:
            ax.spines[s].set_visible(False)
        ax.xaxis.set_ticks_position('none')
        ax.yaxis.set_ticks_position('none')
        ax.xaxis.set_tick_params(pad = 5)
        ax.yaxis.set_tick_params(pad = 10)
        ax.invert_yaxis()
        ax.grid(color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
        for i in ax.patches:
            plt.text(i.get_width()+0.2, i.get_y()+0.5,
                    str(round((i.get_width()), 2)),
                    fontsize = 10, fontweight ='bold',
                    color ='grey')
        
        ax.set_title(nombre,
                    loc ='left', )
        plt.show()
    ## Funcione para elegir la lista de clientes VIP y sacar el promedio
    def get_table_means(self,races):
        pre_df = []
        for race in races:
            if race.puestosvip > 0:
                mean = race.monto_compras/race.puestosvip
            else:
                mean = 0
            pre_df.append([race.name, mean])
        df = pd.DataFrame(pre_df, columns=['Nombre de la carrera', 'Promedio de ingresos por cliente VIP'])
        return df
    def index_1(self,races):
        df = self.get_table_means(races)
        while True:
            print('Elija una de las siguientes opcines\t\n1. Ver el promedio de un cliente\t\n2. Ver un grafico con todos los clientes\t\n3. Salir')
            user_input = input('==> ')
            if user_input == '1':
                print(df.to_markdown(index=False))
            elif user_input =='2':
                self.graph(df['Nombre de la carrera'],df['Promedio de ingresos por cliente VIP'],'PROMEDIO DE INGRESOS POR CLIENTE VIP')
            elif user_input =='3':
                break
            else:
                print('Dato invalido')
    ## Funcion para generar la tabla de pandas que se usara en las proximas estadisticas
    def get_df(self,carreras_ob_db):
        pre_df = []
        for carrera in carreras_ob_db:
            name = carrera.name
            circuit = carrera.circuit.name
            boletos = carrera.puestosvip + carrera.puestosgeneral
            asistencia = carrera.assistance
            if boletos >0:
                relacion = asistencia/boletos
            else:
                relacion = 0
            carrera = [name,circuit,boletos,asistencia,relacion]
            pre_df.append(carrera)
        df = pd.DataFrame(pre_df, columns=['Nombre de la carrera', 'Circuito','Boletos Vendidos','Cantidad de personas que asistieron','Relacion asistencia/venta'])
        return df
    ## Funciones para mostrar la carrera con la especificacion elegida o un grafico de mayor a menor con el referente elegido
    def index_2(self,df):
        df2 = df.sort_values(by=['Cantidad de personas que asistieron'],ascending = False)
        print(df2.to_markdown(index=False))
    def index_3(self,df):
        df3 = df.sort_values(by=['Cantidad de personas que asistieron'],ascending = False)
        while True:
            print('Elija una de las siguientes opciones\t\n1. Ver la carrera con mayor asistencia\t\n2. Ver un grafico con los valores de la asistencia de clientes\t\n3. Salir')
            user_input = input('==> ')
            if user_input == '1':
                print(df3.iloc[0])
                break
            elif user_input =='2':
                self.graph(df3['Nombre de la carrera'],df3['Cantidad de personas que asistieron'],'ASISTENCIA DE LA CARRERA')
                break
            elif user_input =='3':
                break
            else:
                print('Dato invalido')
    def index_4(self,df):
        df4 = df.sort_values(by=['Boletos Vendidos'],ascending = False)
        while True:
            print('Elija una de las siguientes opciones\t\n1. Ver la carrera con mayor asistencia\t\n2. Ver un grafico con los valores de la asistencia de clientes\t\n3. Salir')
            user_input = input('==> ')
            if user_input == '1':
                print(df4.iloc[0])
                break
            elif user_input =='2':
                self.graph(df4['Nombre de la carrera'],df4['Boletos Vendidos'],'CANTIDAD DE BOLETOS VENDIDOS')
                break
            elif user_input =='3':
                break
            else:
                print('Dato invalido')
        print(df4.iloc[0])
    ##Funciones para mostrar los 3 productos mas vendidos en un restaurante
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
                    return restaurant
                else:
                    print('El numero no esta en la lista de opciones')
            else:
                print('Debe ser un numero')
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
    def index_5(self,db):
        carrera = self.get_race(db)
        list_of_items = []
        df = []
        for rest in carrera.restaurants:
                for item in rest.items:
                    item2 = [item.name,item.sell]
                    list_of_items.append(item)
                    df.append(item2)
        list_of_items.sort(key=lambda x:x.sell, reverse=True)
        df = pd.DataFrame(df, columns=['Nombre','Ventas'])
        df2  = df
        df2 = df2.sort_values(by = ['Ventas'], ascending=False)
        df2 = df2.iloc[0:3]
        while True:
            print('Elija una de las siguientes opciones\t\n1. Ver un grafico con las ventas totales de cada restaurante\t\n2. Ver un grafico de la venta de los productos\t\n3. Salir')
            user_input = input('==> ')
            if user_input == '1':
                for x in range(0,3):
                    list_of_items[x].show_attributes()
                break
            elif user_input =='2':
                self.graph(df2['Nombre'],df2['Ventas'],f'ITEMS VENDIDOS EN {carrera.name}')
                break
            elif user_input =='3':
                break
            else:
                print('Dato invalido')
    ## Funcion para ver el top 3 de clientes en toda la base de datos
    def index_6(self,clients_db):
        if len(clients_db) > 2:
            clients = []
            df = []
            for client in clients_db:
                df.append([client.name,client.total_seat])
                clients.append(client)
            clients.sort(key=lambda x:x.total_seat, reverse=True)
            df = pd.DataFrame(df, columns=['Cliente','Total de asientos'])
            while True:
                print('Elija una de las siguientes opciones\t\n1. Ver el top 3 de los productos del restaurante elejido\t\n2. Ver un grafico de la venta de los productos\t\n3. Salir')
                user_input = input('==> ')
                if user_input == '1':
                    for x in range(0,3):
                        print(f'Nombre = {clients[x].name}\n Numero de asientos = {clients[x].total_seat}')
                    break
                elif user_input =='2':
                    self.graph(df['Cliente'],df['Total de asientos'],f'Numero de asientos por client')
                    break
                elif user_input =='3':
                    break
                else:
                    print('Dato invalido')
        else:
            print('No se han registrado mas de 2 distintos clientes')
    ## Metodo start para de este modulo que llama a cada index
    def startED(self,carreras_ob,clients_ob):
        df = self.get_df(carreras_ob)
        while True:
            print('Elija una de las sifguientes opciones\t\n1. Ver el promedio de ingreso por cliente VIP de una carrera\t\n2. Ver una tabla en funcion de la asistencia de todas las carreras\t\n3. Carrera con mayor asistencia\t\n4. Carrera con mayor numero de boletos\t\n5. Top 3 productos de un restaurante en una carrera\t\n6. Top 3 clientes que compraron mas asientos\t\n7. Salir')
            user_input = input('==> ')
            if user_input == '1':
                self.index_1(carreras_ob)
            elif user_input == '2':
                self.index_2(df)
            elif user_input == '3':
                self.index_3(df)
            elif user_input == '4':
                self.index_4(df)
            elif user_input =='5':
                self.index_5(carreras_ob)
            elif user_input == '6':
                self.index_6(clients_ob)
            elif user_input =='7':
                break
            else:
                print('Dato invalido')