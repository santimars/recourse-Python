'''
Inserando un registro
'''

import sqlite3

conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()
cursor.execute("INSERT INTO usuarios VALUES('Cristian',30,'cristian@pruebas.es')")
conexion.commit()
'''
commit()
esta hecho para
CREATE
INSERT
REMOVE
basicamente
'''
conexion.close()

# consultar informacion en sql es SELECT 
"""recuperacion el primer registro con .fetchone()"""


conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()
# Recuperamos los registros de la tabla usuarios
cursor.execute("SELECT * FROM usuarios") #aca estamos haciendo una consulta por eso no estamos poniendo un commit()
# Recorremos el primer registros con el metodo fetchone, devuelve una tupla
usuario = cursor.fetchone()
print(usuario)

conexion.close()

'''
Insetando varios registros con .executemany()
'''

conexion = sqlite3.connect("ejemplo.db")
conexion.set_trace_callback(print) 
cursor = conexion.cursor()# vemos lo que la base de datos esta haciendo

# Creamos una lista con varios usuarios
usuarios = [('Mario',61,'mario@pruebas.es'),
            ('Mercedes',45,'mercedes@pruebas.es'),
            ('Juan',13,'juan@pruebas.es'),
            ('sara',34,'sara@purebas.es'),
            ('Valentina',23,'valentina@pruebas.es')
            ]
# Ahora utilizamos el metodo executemany() para insertar varios
cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)",usuarios)

# Guardamos los camobios haciendo un commit
conexion.commit()
# cerramos la conexion
conexion.close()

'''
Recuperando varios registros con .fetchall()
'''

conexion = sqlite3.connect("ejemplo.db")
conexion.set_trace_callback(print) 
cursor = conexion.cursor()# vemos lo que la base de datos esta haciendo

# Recuperamos los registros de la tabla usuarios
cursor.execute("SELECT * FROM usuarios")

#Recorremos todos los registros con fetchall, y los volvamos en una lista de usuarios

usuarios = cursor.fetchall()
print(usuarios)
print(type(usuarios)) # una tupla

# ahora podemos recorrer todos los usuarios 
for usuario in usuarios:
    print(usuario[0],"->", usuario[1])

conexion.close()
