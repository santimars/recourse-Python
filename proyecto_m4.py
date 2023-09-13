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
    
    def __str__(self):
        return """- marca: {}
                  - modelo: {}""".format(self.marca,self.modelo)

class Vehiculos_Electricos:
    #contructor
    def __init__(self):
        self.autonomia = 100
        print("creando objeto de la clase Vehiculos Electricos")

    def cargarEnergia(self):
        '''Metodo cargarEnergia de la clase Vehiculos Electricos. Indica al sistema si el Vehiculo Electrico esta cargado o no.'''
        self.cargando = True
        print("Cargando energia")
        
    def __str__(self):
        return """- autonomia: {}""".format(self.autonomia)

class Bicicleta_Electrica(Vehiculos_Electricos,vehiculos):
    
    '''Metodo Bicicleta Electrica que se hereda de la clase vehiculos y la clase vehiculos electricos, es decir, herencia multiple.'''
    
    def __init__(self, marca = None, modelo = None, autonomia =100):
        Vehiculos_Electricos.__init__(self) # Equivale a: super().__init__(autonomia)
        vehiculos.__init__(self, marca, modelo)
        print("Hemos creado un objeto de la clase Bicicleta Electrica")
        
        
    def __str__(self):
        return vehiculos.__str__(self) + "\n" + Vehiculos_Electricos.__str__(self)
        # Equivale a:
        # return Vehiculos.__str__(self) + super().__str__()
        
mibici = Bicicleta_Electrica(marca="ford",modelo="Xtreme",autonomia=80)
print(mibici, end="\n\n")
mibici2 = Bicicleta_Electrica(marca="ford",modelo="Xtreme")
print(mibici2, end="\n\n")
mibici3 = Bicicleta_Electrica(marca="ford",modelo="Casual",autonomia=100)
print(mibici3, end="\n\n")

# Si estamo usando herencia multiple procuremos en no usar super() ya que tenemos muchos padres y super()solo nos deja uno
# es mejor acceder de otra manera    ]

class Futbolista():
    def __init__(self,altura,peso):
        self.altura =altura
        self.peso = peso
        print("Creado futbolista")
        
class Nacionalidad():
    def __init__(self,origen):
        self.origen = origen
        print("Nacionalidad creada")

class Defensa(Futbolista,Nacionalidad):
    """Este constructor tiene que recibir todos los parametros, los de Futbolistas y los de Nacionalidad"""
    def __init__(self,altura, peso, origen):
        #super().__init__(def_altura,def_peso)
        Futbolista.__init__(self,altura, peso )
        Nacionalidad.__init__(self,origen)#  el orden aqui no importa pero en herencia multinivel es un problema
        print("Defensa creado")
        """Ojo cuando usamos super(), super es un metodo de Python que hace referencia a la clase padre principal, por lo tanto,
           como es un metodo lleva (), es decir, super().pero cuando accedemos a una clase, no tenemos que usar esos ()
           Nacionalidad.__init__ es suficiente. Otro detalle es que super nos traslada self de manera automatica. pero
           cuando invocamos a una clase manualmente, no, por lo tanto, tenemos que pasar self en el __init__"""
    
d1 = Defensa(altura="1.88",peso=78,origen="Colombia")
print("Altura:",d1.altura)
print("Nacionalidad:",d1.origen)


''                                     '''Herencia Multinivel'''

'''
Ya hemos visto la herencia simple y la herencia multiple, ahora veremos la tercera opcion, la herencia multinivel
podemos heredar de una clase derivada. Esto se llama ferencia multinivel. Puede ser de cualquier profundidad en Python.
En la herencia multinivel, las caracteristicas de la clase base y la clase derivada se heredan en la nueva clase derivada.
vamos a crear la siguiente estructura de clases:  "ABUELO -> PADRE -> HIJO"
'''
class Abuelo:
    def __init__(self,nombreAbuelo=None):
        self.__nombreAbuelo = nombreAbuelo
        print("Abuelo creado")
    
    @property
    def nombreAbuelo (self):
        return self.__nombreAbuelo
    @nombreAbuelo.setter
    def nombreAbuelo(self,new):
        self.__nombreAbuelo = new
    
    def LenguajeDelAbuelo(self):
            print(self.nombreAbuelo, "Programa en Ensalblador")
            
    def __str__(self):
        return "Nombre del Abuelo {}".format(self.nombre)
    
class Padre(Abuelo):
    __nombre = None
    
    def __init__(self, nombreAbuelo=None,nombrePadre =None):
        super().__init__(nombreAbuelo)
        self.__nombre = nombrePadre
    @property
    def nombrePadre (self):
     return self.__nombre
  
    @nombrePadre .setter
    def nombrePadre (self,new):
     self.__nombre = new
     
     
    def __str__(self):
        return super().__str__() + "\nNombre del Padre {}".format(self.nombre)

class Hijo(Padre):
    __nombre = None
    
    def __init__(self, nombrePadre=None,nombreHijo =None):
        super().__init__(nombrePadre)
        self.__nombre = nombreHijo
    @property
    def nombreHijo(self):
     return self.__nombre
  
    @nombreHijo .setter
    def nombreHijo (self,new):
     self.__nombre = new
     
     
    def __str__(self):
        return super().__str__() + "\nNombre del Hijo {}".format(self.nombre)
    
if __name__ == "__main__":
    #creamos un objeto de la clase Abuelo y probamos sus metodos
    print("==ABUELO==")
    abuelo = Abuelo("Fran")
    print(abuelo.nombreAbuelo)
# en python no hay programar mas caminos que los que hay solo debe ser 1
# hay que dibujar el esquema de clases he ir dibujando las herencias y asi detectar que solo halla 1 camino.
