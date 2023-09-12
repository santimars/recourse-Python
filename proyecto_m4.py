""                                 """herencia multiple"""


"""

Posibilidad de que una subclase herede multiples superclases.
El problema aparece cuando las superclases tienen atributos o metodos comunes
En estos casos ,Python dará prioridad a las clases mas a izquierda en el momento de 
la declaracion de la sub clase.

asi como la herencia podemos es herendar herencia de otras cosas 
hay casos en que heredamos en tres clades 
hey muchos ejemplos en la vida real que es asi

se le llama herencia multinivel si hay mas padres en las clases 
un ejemplo esta personal universitario con oficina, profesor , alumno Y entre 
profesor y alumno hay un hijo llamado profesor ayudante}


se recomienda no usar herencia multiple 
"""

"""
Poliformismo
(muchas-formas)
es un objeto que tiene un metodo 
nos ayuda a hacer ciertas funcionalidades que van a estar en todas mi clases epero cada una va activarse
de manera diferente 
"""

class A:
    def __init__(self):
        print("soy de clase A")
    def a(self):
        print("Este metodo lo heredo de a")
class B:
    def __init__(self):
        print("soy de clase B")
    def b(self):
        print("Este metodo lo heredo de b")

class C(A,B):#ponemos los padres que nesecita separados por coma ,
    def __init__(self):
        super().__init__()

    def c(self):
        print("Este metodo lo heredo de C")

c = C()#al crear un objeto de la clase c, hereda el constructor de la superclase B
# (porque es la que esta mas a la izquierda)

#COMPROBAMOS QUE DESDE C PODEMOS ACCEDER A METODOS DE A Y B 
c.a()
c.b()
c.c()

#PRUEBAS
"""
- prueba a cambiar el orden de c(b,a) Que contructor se ejecuta?
- pureba a elimiar el constructor de C. Que constructor se ejecuta?
- prueba a eliminar el contructor de C y tambien del padre principal Que constructor se ejecuta?
"""

""                         """ HERENCIA MULTIPLE CON UN EJEMPLO"""

class vehiculos:
    #contructor
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        print("creando objeto de la clase Vehiculos")

    def repostar(self):
        print("repostanto combistible")

class Vehiculos_Electricos:
    #contructor
    def __init__(self):
        self.autonomia = 100
        print("creando objeto de la clase Vehiculos Electricos")

    def cargarEnergia(self):
        '''Metodo cargarEnergia de la clase Vehiculos Electricos. Indica al sistema si el Vehiculo Electrico esta cargado o no.'''
        self.cargando = True
        print("Cargando energia")

class Bicicleta_Electrica(Vehiculos_Electricos,vehiculos):
    '''Metodo Bicicleta Electrica que se hereda de la clase vehiculos y la clase vehiculos electricos, es decir, herencia multiple.'''
    pass

class Quad():
    pass

print("Bicicleta Electrica")

#objeto de la clase bicicleta electrica
# al heredar de 2 clases, tiene disponible 2 constructores.
# cual se ejecuta? cual estara heredando? En este caso el de Vehiculos Electricos
# porque al definir la herencia multiple, Vehiculos Electricos se puso primero

mibici = Bicicleta_Electrica()
print("Automia:", mibici.autonomia)

#comprobaciones
"""vamos a comprobar a que clase pertencece el objeto miBici y quien es su padre"""

#comprovamos si mibici pertenece a mibicicleta
print(isinstance(mibici,Bicicleta_Electrica))
print(isinstance(mibici,Vehiculos_Electricos))
print(isinstance(mibici,vehiculos))

#comprobamos el nombre de la clase a la que pertenence el objeto mibici
print(type(mibici).__name__)

#comprobamos si bicicletaelectrica hereda a vehiculos electricos,vi¿ehiculos y quad
print(issubclass(Bicicleta_Electrica,Vehiculos_Electricos))
print(issubclass(Bicicleta_Electrica,vehiculos))
print(issubclass(Bicicleta_Electrica,Quad))

mibici  = Bicicleta_Electrica()


''              ''' Entendido, en resumen tenemos dos casos cuando hacemos que una clase de multiples clases'''

'''
Si la clase que tiene herencia multiple tiene constructor -> lo ejecuta
si la clase que tiene herencia multiple No tiene contructor -> Ejecuta el constructor del padre principal(el que se encuentra
mas a la izquierda en la visa de herencia)
'''

''             '''Y en el caso de qu ela clase que hereda, tenfa constructor(y lo ejecute),puede aun asi
ejecutar los contructores de sus padres?'''

'''
SI!! Invocaremos desde el constructor de nuestra clasee a todos los contructores de los padres que queramos 
'''
class vehiculos:
    #contructor
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        print("creando objeto de la clase Vehiculos")

    def repostar(self):
        print("repostanto combistible")

class Vehiculos_Electricos:
    #contructor
    def __init__(self):
        self.autonomia = 100
        print("creando objeto de la clase Vehiculos Electricos")

    def cargarEnergia(self):
        '''Metodo cargarEnergia de la clase Vehiculos Electricos. Indica al sistema si el Vehiculo Electrico esta cargado o no.'''
        self.cargando = True
        print("Cargando energia")

class Bicicleta_Electrica(Vehiculos_Electricos,vehiculos):
    '''Metodo Bicicleta Electrica que se hereda de la clase vehiculos y la clase vehiculos electricos, es decir, herencia multiple.'''
    def __init__(self,marca=None,modelo=None,autonomia=None):
        Vehiculos_Electricos.__ini__(self,autonomia) # Equivale a: super().__init__(autonomia)
        vehiculos.__init__(self,marca,modelo)
        print("Hemos creado un objeto de la clase Bicicleta Electrica")
        
    def __str__(self):
        return vehiculos.__str__(self) + "\n" + Vehiculos_Electricos.__sr__(self)
        # Equivale a:
        # return Vehiculos.__str__(self) + super().__str__()
        
mibici = Bicicleta_Electrica(marca="ford",modelo="Xtreme",autonomia=80)

# Si estamo usando herencia multiple procuremos en no usar super() ya que tenemos muchos padres y super()solo nos deja uno
# es mejor acceder de otra manera    