from mysql import DataBase

class DBProceso():
    def __init__(self, id):
        self.connection = DataBase().connection
        self.cursor = self.connection.cursor()
        maquina = self.select_maquina(id)
        self.id_maquina = maquina[0]
        self.nombre_maquina = maquina[1]
        self.disponible = maquina[2]
        print('id: ', self.id_maquina)
        print('nombre: ', self.nombre_maquina)
        print('disponible: ', self.disponible)
        print('\n')



    def select_maquina(self,id):
        sql = 'SELECT id_maquina, nombre_maquina, disponible from maquina where id_maquina = {}'.format(id)
        objeto_maquina = []
        try: 
            self.cursor.execute(sql)
            maquina = self.cursor.fetchone()
            objeto_maquina = [maquina[0],maquina[1],maquina[2]]
            return objeto_maquina
        except Exception as e:
            print(e)
            raise
            

    def select_name_maquinas_enabled(self):
        sql = 'SELECT nombre_maquina from maquina where disponible = 1 '
        try:
            self.cursor.execute(sql)
            maquinas = self.cursor.fetchall()
            lista  = []
            for maquina in maquinas:
                lista.append(maquina[0])
            return lista
        except Exception as e:
            print(e)
            raise

maquina  = DBMaquina(1)
list = maquina.select_name_maquinas_enabled()
print(list)