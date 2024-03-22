# Este sera una estructura perfecta que es muy abitual para nuestras aplicaciones y paginas web
# vamos a poner un sistemas de datos 
#ventajas
'''
podemos cambiar de gestor de bases de datos 
si es que crecen 
vamos a ver que el trabajo que estamos viendo esta
muy alineada con la programacion orientada a objetos
todos de esto vamos a reutilizarlo al 100%
vamos a empezar con la base de datos.

main.py ->
venv -> 
models.py ->
db.py ->
database ->

son nombres de convenio donde se llamaran nuestros siguientes projectos futuros

'''
class Persona():
    def __init__(self, nombre , apellido, edad, mail):
        self.nombre = nombre
        self.apellido = apellido