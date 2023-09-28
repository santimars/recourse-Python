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
profesor y alumno hay un hijo llamado profesor ayudante


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
        return "Nombre del Abuelo {}".format(self.nombreAbuelo)
    
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
    
    def LenguajeDelPadre(self):
            print(self.nombrePadre, "Programa en C") 
     
    def __str__(self):
        return super().__str__() + "\nNombre del Padre {}".format(self.nombrePadre)

class Hijo(Padre):
    __nombre = None
    
    def __init__(self,nombreAbuelo = None, nombrePadre=None,nombreHijo =None):
        super().__init__(nombreAbuelo,nombrePadre)
        self.__nombre = nombreHijo
    @property
    def nombreHijo(self):
     return self.__nombre
  
    @nombreHijo .setter
    def nombreHijo (self,new):
     self.__nombre = new
    
    def LenguajeDelHijo(self):
            print(self.nombreHijo, "Programa en Python")  
    
    def __str__(self):
        return super().__str__() + "\nNombre del Hijo {}".format(self.nombreHijo)
    
if __name__ == "__main__":
    #creamos un objeto de la clase Abuelo y probamos sus metodos
    print("==ABUELO==")
    abuelo = Abuelo("Fran")
    print(abuelo.nombreAbuelo) # metodo getter
    abuelo.nombreAbuelo = "Francisco"
    print(abuelo)# Metodo __str__
    
    # Creamos un objeto de la clase Padre u probamos sus metodos
    print("\n==PADRE==")
    padre = Padre("Carlos","Francisco")
    print(padre)
    
    # Creamos un objeto de la clase hijo y probamos sus metodos
    print("\n==HIJO==")
    hijo = Hijo("Pablo","Carlos","Francisco")
    print(hijo)
    
# en python no hay programar mas caminos que los que hay solo debe ser 1

# hay que dibujar el esquema de clases he ir dibujando las herencias y asi detectar que solo halla 1 camino.

# hay que dibujar el esquema de clases he ir dibujando las herencias y asi detectar que solo halla 1 camino

    print("\n=== LENGUAJES DE PROGRAMACION===")
    hijo.LenguajeDelHijo()# Metodo de la clase Hijo
    hijo.LenguajeDelPadre()# Metodo de la clase Padre
    hijo.LenguajeDelAbuelo()# Metodo de la clase Abuelo
    
    
''                      '''MRO (Method Resolution Order)'''
'''
El MRO es el orden en el que python busca un metodo en una jerarquia de clases. Especialmente juega un papel 
vital en el contexto de la herencia multiple, ya que se puede encontrar un metodo unico en multiples superclases.
'''
class Class1:
    def m (self):
        print("En Class 1")

class Class2(Class1):
    def m(self):
        print("En Clase 2")
        super().m()

class Class3(Class1):
    def m(self):
        print("En Clase 3")
        super().m()
        
class Class4(Class2,Class3):
    def m(self):
        print("En Class 4")
        super().m()
        
obj = Class4()
obj.m()

'''
Comprobamos que al crear un objeto de Class4 e invocar a su metodo m() se ejecuta:

1. El metodo m() local de la propia clase Class4
2. El metodo m() del padre principal de Class4: Class2
3. El metodo m() del otro padre de Class4: Class3
4. El metodo m() del padre de Class2 y Class3, es decir, el abuelo de Class4: Class1
'''
# Un truco es poder ver el orden que MRO esta asignado a nuestras clases directamente con el metodo mrc
print(Class4.mro())
# Vemos que le orden es Class4 -> Class3 -> Class2 -> Class1 Object (clase principal de Python de la )
print("Orden:")
for i in Class4.mro():
    print(i)

#asi conocemos la forma que en python entiende a donde vamos en el codigo.

''                      ''' Preparemonos par el Polimorfismo. Ejemplo Productos'''
'''
es un pedazo de codigo que hace una tarea que cambia por la clase en el que este 
hacer funciones de las cuales que traten hacer una funcion que acepte contipo de datos completamente diferentes y mi funcion
se adapte crear una fucnion que resiva y la funcion que siga trabajando'''
class Producto:
    def __init__(self,referencia,nombre,pvp,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
        
    def __str__(self):
        return """\
            referencia\t{}
            Nombre\t{}
            Pvp\t{}
            Descripcion\t{}
            """.format(self.referencia,self.nombre,self.pvp,self.descripcion)
    
class Adorno(Producto):
    pass

class Alimento(Producto):
    productor = ""
    distribuidor = ""
    
    def __Str__(self):
        return"""\
            referencia\t{}
            Nombre\t{}
            Pvp\t{}
            Descripcion\t{}
            Productor\t{}
            Distribuidor\t{}
            """.format(self.referencia,self.nombre,self.pvp,self.descripcion,self.productor,self.distribuidor)
            
class Libro(Producto):
    isbn = ""
    autor = ""
    
    def __str__(self):
        return"""\
            referencia\t{}
            Nombre\t{}
            Pvp\t{}
            Descripcion\t{}
            Isbn\t{}
            Autor\t{}
            """.format(self.referencia,self.nombre,self.pvp,self.descripcion,self.isbn,self.autor)
# creamos alfunos objetos
ad = Adorno(2034,"Vaso adornado",15,"Vaso de porcelana adornado con arboles")

al = Alimento(2035,"Botella de Aceite de Oliva",5,"250ML")
al.productor = "La aceitera"
al.distribuidor = "Distribuciones SA"

li = Libro(2036,"Cocina Mediterranea",9,"Recetas sanas y buenas")
li.autor = "Dona juana"
li.isbn = "3-124655-78-4"
  
# lista de productos
Producto = [ad,al,li]
for p in Producto:
    print(p) 

''                              '''Poliformismo'''

'''
Se refiere a un propuedad de la herencia por la que objetos de distintas sub clases pueden responder a una misma accion
'''
def rebajar_producto(p,rebaja):
    """rebaja un producto en porcentaje de su precio"""
    print(type(p))
    
    p.pvp =  p.pvp - (p.pvp/100 * rebaja)

print("ANTES DE LAS REBAJAS:",end="")
print(li.pvp)
rebajar_producto(li,10)
print("DESPUES DE LAS REBAJAS:",end="")
print(li.pvp)

'''
El metodo rebajar_producto() es capaz de tomar objeos de distintas subclases y manipular el atributo pvp
la accion de manipular el pvp funcionara siempre que los objetos tengan ese atributo. pero en el caso de no ser asi, darla error.
'''
'''
suelen ser funcionese en el main funciones que no tiene dueño, ya que va a trabajar con todas las clases
para ello en el ejemplo pvp esta en todas las cosas eso nos hace ver que para que funciones esta funcion poliformica debe estar la variable
que vamos a ejecutar en todas nuestras clases
'''

''              '''Poliformismo Ejemplo de vehiculos'''
# es importante    que la funciones que este en mis clases se llamen igual obviamente claro porque comparte el mismo 
class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")
        
class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")
        
class Camion():
    def desplazamiento(self):
        print("Me despazo utilizando seis ruedas")
        
# Prgrama principal, fuera de als clases

print("USO NORMAL POLIFORMISMO")
# cada objeto instanciado de cada una de las 3 clases accede a su metodo desplazamiento

miVehiculo = Moto()
miVehiculo.desplazamiento()

miVehiculo2 = Coche()
miVehiculo2.desplazamiento()

miVehiculo3 = Camion()
miVehiculo3.desplazamiento()

# Ahora usemos el poliformismo. Vamos a crear un metodo que recibira por parametro un objeto del tipo vehiculo a

def desplazamientoVehiculo(v):
    print("Objeto resivido de tipo: ",type(v).__name__)
    v.desplazamiento()

print("\nUSO DE POLIFORMISMO")
miVehiculo4 = Camion()
desplazamientoVehiculo(miVehiculo4)
miVehiculo5 = Moto()
desplazamientoVehiculo(miVehiculo5)
    
lista = [miVehiculo,miVehiculo2,miVehiculo3,miVehiculo4,miVehiculo5]
for i in lista:
    desplazamientoVehiculo(i)

#un metodo poliformico nos aporta cuanto tenemos muchos datos un ejemplo 3000 mil tipos de vehiculos
'''
si notamos que estamos hacieno un mismo codigo siempre habra una solucion mejor
'''
''                                  ''' METODOS APLICADOS'''

# ALGORITMOS APLICADOS
lista.sort()# sort nos ordena la lista 
# los metodos que hay en python que pueden cambiar es su actualizaciones siempre estan en constante cambio 
# en varias formas en el que aparece
# antes de hacer algo preguntemonos si python ya lo tiene
# esto ahorra mucho tiempo al programe



# punto de partida
# podemos ver que habra metodos que tendran ciertos parametros
#(iterable)si esta la palabra iterable signigica que es obligatorio
#(widh[,fillchar]) si tiene estas palabras dentro de corchetes [] significa que  es opcional
#para saber si algo esta en mayuscuslas o es una copia es ver la documentacion
texto = "Hola mundo tel:4655516155 adios"
posicion = texto.find("tel:")

if (posicion != -1):
    print(texto[posicion+4:posicion+13])

"hola mundo".find("mundo")
# https://www.notion.so/Metodos-Aplicados-1599f3a7ef4d41968477df81e5105e48?pvs=4

"isdigit(): Devuelve True si la cadena es toso numeros(False en caso contrario)"
c= "100"
if c.isdigit()==True:
    c= int(c)
    print(c+7)
else:
    print("No se puede convertir a numero porque c tiene letras")
#c.isdigit()
'isalnum(): Devuelve True si la cadena es todo numeros o caracteres algabeticos'

c2 = "ABC10034po"
c2.isalnum()

"isalpha(): Devuelve True si la cadena es todo caracteres alfabeticos"
c2.isalpha()