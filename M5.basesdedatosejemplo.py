import sqlite3

conexion = sqlite3.connect("basededatos.db")
conexion.set_trace_callback(print) 
cursor = conexion.cursor()
#recuperamos los registros de la tabla de usuarios
columna_que_quiero_extraer = "nombre, edad"
nombre_tabla = "usuarios" 
condicion = "edad"
valor_condicion = 25
query = "SELECT {} FROM {} WHERE {}>{}".format(columna_que_quiero_extraer,
                                               nombre_tabla,
                                               condicion,
                                               valor_condicion)

# Recorremos todos los registros con fetchall, y los volvamos en una lista de usuarios
usuarios = cursor.fetchall()

# Ahorra podemos recorrer todos los usuarios
for usuario in usuarios:
    print(usuario)

conexion.close()