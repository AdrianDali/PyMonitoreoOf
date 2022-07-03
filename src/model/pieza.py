from mysql import DataBase

class DBPieza():
    def __init__(self, id):
        self.connection = DataBase().connection
        self.cursor = self.connection.cursor()
        pieza = self.select_pieza(id)
        self.id_pieza = pieza[0]
        self.nombre_pieza = pieza[1]
        #self.disponible = pieza[2]
        print('id: ', self.id_pieza)
        print('nombre: ', self.nombre_pieza)
        #print('disponible: ', self.disponible)
        print('\n')



    def select_pieza(self,id):
        sql = 'SELECT id_pieza, nombre_pieza from pieza where id_pieza = {}'.format(id)
        objeto_pieza = []
        try: 
            self.cursor.execute(sql)
            pieza = self.cursor.fetchone()
            objeto_pieza = [pieza[0],pieza[1]]
            return objeto_pieza
        except Exception as e:
            print(e)
            raise
            

    def select_name_piezas(self):
        sql = 'SELECT nombre_pieza from pieza '
        try:
            self.cursor.execute(sql)
            piezas = self.cursor.fetchall()
            lista  = []
            for pieza in piezas:
                lista.append(pieza[0])
            return lista
        except Exception as e:
            print(e)
            raise

maquina  = DBPieza(1)
list = maquina.select_name_piezas()
print(list)