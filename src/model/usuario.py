
from mysql import DataBase

class DBUsuario():
    def __init__(self, id):
        self.connection = DataBase().connection
        self.cursor = self.connection.cursor()
        usuario = self.select_usuario(id)
        self.id_usuario = usuario[0]
        self.nombre_usuario = usuario[1]
        self.disponible = usuario[2]
        print('id: ', self.id_usuario)
        print('nombre: ', self.nombre_usuario)
        print('disponible: ', self.disponible)
        print('\n')



    def select_usuario(self,id):
        sql = 'SELECT id_usuario, nombre, disponible from usuarios where id_usuario = {}'.format(id)
        objeto_usuario = []
        try: 
            self.cursor.execute(sql)
            usuario = self.cursor.fetchone()
            objeto_usuario = [usuario[0],usuario[1],usuario[2]]
            return objeto_usuario
        except Exception as e:
            print(e)
            raise
            

    def select_name_usuario_enabled(self):
        sql = 'SELECT nombre from usuarios where disponible = 1 '
        try:
            self.cursor.execute(sql)
            usuarios = self.cursor.fetchall()
            lista  = []
            for usuario in usuarios:
                lista.append(usuario[0])
            return lista
        except Exception as e:
            print(e)
            raise

#usuario  = DBUsuario(2)
#list = usuario.select_name_usuario_enabled()
#print(list)