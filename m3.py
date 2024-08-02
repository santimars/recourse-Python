''                                              ''' Metodologia Basada en objetos'''


#1. Progrmacion estrucuturada VS POO (Programacion Orientada a Objetos)

"clase teorica"
#cambia todo lo que hemos visto hasta ahora

'''
diferentes formas de programar 
esta la orientada a objetos y orientada a procedimientos

las funciones se llamaban procedimientos antes


 las desventajas de las lenguajes de oriendo
 hay problemas en la programaxion estrucuturada, pero
 era lo que habia...
 
hasta que surge la nesecidad de proyectos software mas grandes y complejos
de esa nesecidad nace la programacion
orientada a objetos 

objetivo de la progrmacion oriendtada a objetos
trasladar la naturaleza de los objetos de la vida real al codigo de programacion

cual es la naturaleza de un objeto de la vida real?
los objetos tienen:
un estado
un compartamiento (Que se puede hacer?)
unas propiedades

en resumen

nuestro mundo es un cojunto de objetos/agentes
colaborando unos con otros

Nuesto software debe representar y organizarse de
acuerdo a la estrucutura del mundo real


vocabukario POO
clases
objetos
instancia de clase
atributos y metodos
abstraccion 
encapsulacion
herencia
polimorfismo

 
'''
''                                                              '''/// Atritutos y metodos de clase'''
'''
Atributos: Hacen referencia a las variables internas de la clase
Metodo : Hacen referencia a las funciones internas de la clase
'''

class galleta():

 pass # instruccion para no hacer nada, ya que en este ejemplo nuestra clase galleta no hace nada por el momento
    
    
una_galleta = galleta()
''                                                        '''DEFINICION DE ATRIBUTOS EN LOS OBJETOS (CUIDADO CON ESTO)'''
una_galleta.sabor = "Salado"
una_galleta.color = "Marron"
# puede ser peligroso hacer esto ya que al ser tan facil puede ser facil dañar nuestro codigo
# la idea de definir clases es que sea homogenea tiene que ser para todos pero en este caso python me deja hacer asignacion de manera rapida

''                                                 '''DEFINICION DE ATRIBUTOS EN LA CLASE'''


class Galletas():
    chocolate = False
    sabor = "Dulce" # estos son atributos globales  todas la variables que tengan la clase Galleta() todos tendran estos atributos por defecto
    
g = Galletas()
print(g.chocolate)

#🍪 estamos haciendo galletas
# estamos cambiado su atributo pordefecto todo lo que yo cree en una variavle va a hacer True

''                                                       '''metodo init() - CONSTRUCTOR'''
'''
Se llama automaticamente al crear una distancia de clase

'''

class Galleta():
    chocolate = False 
    
    def __init__(self):
       print("Se acaba de crear una galleta.")
       
    def chocolatear(self):
        print("Vamos a chocolatear la galleta")
        self.chocolate = True
        
    def tiene_chocolate(self):
        if (self.chocolate == True):
            print("Soy una galleta chocolateada!!!\n (●'◡'●) ")
        
        else:
            print("Soy una galleta sin chocolate...\n (ಥ _ಥ)")
        
print("GALLETA 1")
g = Galleta()
g.tiene_chocolate()
g.chocolatear()
g.tiene_chocolate()

print("\nGALLETA 2")
g2 = Galleta()
g2.tiene_chocolate()            

'''                                                      Parametros ene el Int(argumentos al instalar)                                                     '''


# recomendacion sar siempre el constructor 
# escribirlo desde el principio
'''


'''

class Galleta():

 def __init__(self, sabor = None, forma = None, chocolate = None):
     self.sabor = sabor
     self.forma = forma
     self.chocolate = chocolate

     if self.sabor is not None and self.forma is not None and self.chocolate is not None:
       print("Se acaba de crear una Galleta {}, {} y {}".format(self.sabor,self.forma,self.chocolate))
     else:
       print("Se acaba de crear una Galleta, pero...")
       if self.sabor is None:
           print("> El sabor no se ha definido")
       if self.forma is None:
           print("> La forma no se ha definido")
       if self.chocolate is None:
           print("> El chocolate no se ha definido")

 def chocolatear(self):
  self.chocolate = True

 def tiene_chocolate(self):
  if (self.chocolate):
   print("Soy una galleta chocolateada :D")
  else:
   print("Soy una Galleta sin Chocolate :(")


class Pelicula:
 # constructor de clase (al crear la instancia)
 def __init__(self = None,
             titulo = None,
             duracion = None,
             lanzamiento = None):
     self.titulo = titulo
     self.duracion = duracion
     self.lanzamiento = lanzamiento
     print("Se ha creado la pelicula '{}'".format(self.titulo))
 
 #Destructor de clase (al borrar la instancia)
 def __del__(self):
     print("Se ha borrado la pelicula", self.titulo)

# Creamos y liminamos un objeto Ojo si reinstaciamos la misma variable mas de una vez, se crea de nuevo y se borra la anterior       
p = Pelicula("El paddrino",175,1972)
print(p)
del p 
#print(p)
# Chequear si el objeto o variable existe para decidir eliminarlo o no
if "p" in globals():
    print("Como existe, vamos a elimminarlo...")
    del p
else:
    print("No existe nada para elimminar")

''                                       ''' Mostrar informacion de un objeto __dict__ y __str__'''
#Diccionario (__dict__)
'''
Python nos ofrece prederteminada de mostrar la informacion de un objeto.
'''
p = Pelicula("El padrino",175,1972)
peli = p.__dict__
print(p)
'''
podemos ver que ahora se convierte en un diccionario y esto nos permite poder manipular nuestro objeto'''
#ejemplo
print(type(p))
print(peli["duracion"])
peli["duracion"]  = 200
print(peli["duracion"])

#String (__str__)
'''
No obstante, el metodo anterior no nos proporciona ningun tipo de personalizacion. 
Si queremos personalizar una salida por pantalla de la informacion de nuestro objeto
tenemos que usar el metodo __str__ de Python, el cual implementaremos en nuestra clase y lo configuramos a nuestro gusto.
'''
class Movies:
    # Constructor de la clase
    def __init__(self,titulo,duracion,lanzamiento):
       self.titulo = titulo
       self.duracion = duracion
       self.lanzamiento = lanzamiento
       print("Se ha creado la pelicula {} ".format(self.titulo))
       
    # Destructor de la clase   
    def __del__(self):
        print("Se ha borrado la pelicula {}".format(self.titulo))
        
     #creamos mejor nuestas propias funciones si queremos es imprimir algo en concreto
    def mostrar(self):
       opcion = input("Quiere mostrar la durcaion? (s/n)")
       if opcion == "s":
           return "{} lanzada en {} y con una duracion de {} minutos".format(self.titulo,
                                                                             self.lanzamiento,
                                                                             self.duracion)     
       elif opcion == "n":
           return "{} lanzada en {}".format(self.titulo,self.lanzamiento) 
        
    # Redefinimos el metodo string
    def __str__(self):
        return "{} lanzada en {} con una duracion {} minutos".format(self.titulo,
                                                                     self.lanzamiento,
                                                                     self.duracion)
    
p1 = Movies("El padrino",175,1972)
print(p1) # Al hacer print del objeto, se esta invocando el metodo __str__ de nuestra clase    
p2 = Movies("Alicia el pais de las maravillas",300,2010)
print(p2.mostrar)
# Nota 
'''
No hemos eliminado ni cambiado nuestro contructor
hicimos un diccionario con la informacion que teniamos de nuestro constructor y no el estamos manipulando la informacion
'''



''                              '''Bonus: Comprobar si un objeto es una instancia de una clase'''

class Producto:
    pass

class Pedido:
    pass

class Cliente:
    pass
# vamos a comprobar si un objeto pertenece a una clase

p1 = Producto()
pd1 = Pedido()
c1 = Cliente()

print(isinstance(p1,Producto))
print(isinstance(c1,Producto))
# Tambien se puede evaluar si c1 es instancia de alguna de las clases de la tupla
print(isinstance(c1,(Producto,Pedido,Cliente)))
# isinstance nos sirve para asegurarnos si un objeto es una instancia de una clase
# nos servira mas adelante cuando veamos herencias donde habla objetos mas complejos y no sabremos donde esa la instancias 
# nos permite hacer comprobaciones previas antes de seguir con nuestro codigo

''                             '''Bonus 2 Comprobar si un atributo existe en una clase'''
class Producto:
    precio = 0 # atributo global cualquier instacia lo va a tener
    
    def __init__(self,nombre):
       self.nombre = nombre #Nombre asignado a traves de parametro
p1 = Producto("Tablet")
#Comprovamos que las variables precio y nombre si existen como atributos en el objeto p1 
#(auque sean atributos distintos, uno es de instacia y otro de clase)
print(hasattr(p1,"precio"))
print(hasattr(p1, "nombre"))
print(hasattr(p1,"apellidos"))
# rpeguntamos si tiene un atributo si esta definido 


#comp(robar si las caribales precio y nombre son variables de clase en la clase producto
print(hasattr(Producto,"precio"))
print(hasattr(Producto,"nombre"))

''                               '''Bonus 3 Eliminar atributos de una instancia de clase'''

print(p1.__dict__)  # mostramos el objeto p1 
delattr(p1,"nombre")# Eliminamos el atributo nombre 
print(p1.__dict__)  # Mostramos el objeto p1 

# Lo que no se podria eliminar seria precio,ya que no es un atributo de isntacia 
# delattr(p1,"precio") #Eliminamos el atributo precio
#print(p1.__dict__)# Mostramos el objeto p1

# debemos hacer que nuestros atributos sean homogeneas y puedan  funcionar de la mejor manera '
# cuando ya hacemos mas de un trabajo   4
# no es bueno eliminar informacion es mejor ponerle a cada atributo como None y listo todo va a fluir bien en nuestro codigo

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\
#                                            '''objetos dentro de objetos ''' 


nombres =["cristian",
          "carlos",
          "santiago",
          "Magenta",
          "lucia",
          "michael",
          "dublin",
          "carson",
          "margenta",
          "amber",
          "sofia",
          "julio",
          "serguio",
          "mateo",
          "amanda",
          "cristian",
          "sara"
          
          ]   

edades = [10,20,30]
personas = [nombres,edades]
print(personas)

per1 = {"nombre":"sara",
        "edad":"23"}

per2 = {"nombre":"mateo",
        "edad":"20"}

per3 = {"nombre":"carlos",
        "edad":"31"}
personas = [per1,per2,per3]
print(personas)




''        ''' Recuperemos la clase Pelicula con la que hemos trabajado'''
class Galleta:
    def __init__(self, 
                 forma = "Circular", 
                 sabor = "Vainilla", 
                 chocolate = False, 
                 listaIngredientes = ["Harina","Azucar", "Vainilla","Levadura"]
                 
                 ):
        self.forma = forma
        self.sabor = sabor
        self.chocolate = chocolate
        self.listaIngredientes = listaIngredientes
        print("Galleta creada")

g1 = Galleta(forma = "Cuadrada", 
             sabor = "Vainilla",
             chocolate = False,
             listaIngredientes = ["Harina","Azucar", "Vainilla","Levadura","sal","Huevos","Leche"])
f = g1.forma
print("Forma:",f,"con tipo:",type(f))
c = g1.chocolate
print("Choco:",c,"con tipo:", type(c))
l = g1.listaIngredientes
print("Lista de ingredientes",l,"con tipo: ",type(l))
print(g1.__dict__)

class Director:
    #constructor de clase
    def __init__(self, nombre, apellido, edad = "desconocida"):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        print("Se ha creado El director: ",self.nombre)
    
    def __str__(self):
        return "Director {} {} con edad {}".format(self.nombre,
                                                   self.apellido,
                                                   self.edad)
        
class Pelicula:
    #constructor de clase
    def __init__(self, titulo, duracion, lanzamiento,director):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        self.director = director
        print("Se ha creado la Pelicula: ",self.titulo)
    
    def __str__(self):
        return '{}({}) -> {}'.format(self.titulo,self.lanzamiento,self.director)
       
'''
Tenemos objetos de la clase Director, vamos a reconstruir la clase Pelicula para poder añadir la informacion
del Director a cada pelicula
'''

''                          '''Vamos a crear un directo'''
   
d1 = Director(" Ridley","Scott",84)
d2 = Director(" George","Lucas",)
print(d1)
print(d2)

p_alien = Pelicula(titulo = "Alien el octavo pasajero",
                   duracion = 200,
                   lanzamiento = 1979,
                   director = d1)
#'''Estamos encapculando un objeto dentro de otro'''
print(p_alien)
#comprobacion
print(type(p_alien))
print(p_alien.director)
print(p_alien.duracion)
print(p_alien.lanzamiento)
print(p_alien.titulo)
print(type(d1))
nombre_pelicula = p_alien
print(p_alien.director) 


''                        '''Algo mas avanzado: Creando un catalogo de peliculas '''

'''
Vamos a utilizar muy comun, crear listas de objetos, de esta forma podemos almacenar gran catidad de informacion en un siito
y gestionarlo con la facilidad que nos porporcionan las listas
'''   
# retomemos la clase pelicula original
class Pelicula:
    #construccion de clase
    def __init__(self,titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Gracias por registrar su pelicula favorita: ",self.titulo)
        
    def __str__(self):
        return "{}  ({})".format(self.titulo,self.lanzamiento)
    
class Catalogo:
     
    def __init__(self, nombre, peliculas = []):# esto es una lista que contendra objetos de la clase pelicula
        self.peliculas = peliculas
        self.nombre = nombre
        if (len(self.peliculas)== 0): # recordemos que el constructor debe ser lo mas minimo posible en este caso solo revisa si esta en 0 pero que no pase por pas cosas 
            print("Se ha creado el catalogo vacio")# tratemos de hacerlo siempre se la manera mas minima para que cuando tengamos un problema sepamos solucionarlo
        else:
            print("Se ha creado el catalogo con las peliculas asignadas")
            
    def agregar(self,parametro): # parametro sera un objeto pelicula
        self.peliculas.append(parametro)# mi funcion agregar tiene un parametro lo que ewspero que sea un obejto de la clase pelicula esto lo añado a parametro
        print("Se ha agregado al catalogo la pelicula: {}".format(parametro.titulo))
        
    def mostrar(self):
        print("Catalogo {}".format(self.nombre))
        for p in self.peliculas:
            print(">>> ",p) # print toma por defecto str(p)
    '''
    def __str__(self):
        texto = ""
        texto =+ "Catalogo: {}\n".format(self.nombre)
        for p in self.peliculas:
            texto += ">>> \n".format(p)
        return texto #es mas dificil poner in str en esta caso es mas complejo ponerlo por ello lo mejor fue usar el otro formato que esta arriba  el mostrar()
    '''
    # mejor usemos srt asi
    def __str__(self):
        return "El catalogo {} tiene {} peliculas".format(self.nombre,len(self.peliculas))    # asi hacemos un metodo str simple y una funciona que hace lo que yo quiero que yo haga de manera simple 
            
    # si nosotros hacemos esto, solo estamos guardando una lisa de titulos de peliculas
    #Esto no es lo que queremos, nostros dentro del catalogo queremos tener carias peliculas pero con toda su informacion
c = Catalogo(nombre = "Pelis Favoritas", peliculas = ["El padrino", "Alien"])

p1 = Pelicula(titulo = "el padrino",duracion = 175,lanzamiento = 1972)
p2 = Pelicula(titulo = "Alien el octavo pasajero",duracion = 200,lanzamiento = 1979)
listaPeliculas = [p1,p2]
print(type(listaPeliculas))
print(listaPeliculas)# print no puede visualizar los str de unas estructuras complejas como estas 
# print no sabe meterse en esa lista y recorrer esa lista  he ir uno a uno  mostrando su str

# esto lo solucionamos con un for
for peli in listaPeliculas:
    print(peli) # esta variable peli nos deja ver uno por uno lo que tenemos 
# si deseamos es ir a solo uno de los los arhivos guardados evidentemente print puede hacerlo
print(listaPeliculas[0])


           
c = Catalogo(nombre ="Pelis favoritas",peliculas = listaPeliculas) # creamos el catalogo con dos pelicula
print(c)# en este caso no nos muestra nada porque no tenemos el metodo __str__
c.mostrar()
c.agregar(Pelicula(titulo="El padrino: parte 2",duracion=202,lanzamiento=1974)) # Añadimos una pelicula directamente    

# Lo mismo que lo anterior pero en dos pasos    
pelicula_nueva = Pelicula(titulo="El mosquetero",duracion=202,lanzamiento=1982)
c.agregar(pelicula_nueva)

#Alternativa a la linea anterior
p3 = Pelicula(titulo="soy soy",duracion=204,lanzamiento=2011)
c.agregar(p3)

# puedo tabien cuantas peliculas tengo de esta manera
c.mostrar()
# con el metodo str
print(c)
# tambien podemos crear un catalogo vacio
c2 = Catalogo(nombre= "Pelis Pendientes")
c2.mostrar()
#todo junto
pm1 = Pelicula("Matrix",175,1998)
pm2 = Pelicula("Matrix Reloaded",175,2003)
pm3 = Pelicula("Matrix Revolutions",175,2003)
c3 = Catalogo(nombre ="Pelis civi",peliculas = [pm1,pm2,pm3])
c3.mostrar()
#podemos agregar en nuestro primer catalogo la primera pelicula de matrix
c.agregar(pm1)
c.mostrar()
#como vemos matrix la cree en mi tercer catalogo pero puede estar en mi primer catalogo y le puedo meter muchos atrbiutos si quisiera
# para practicar 
# meterle director  y que desde un catalogo y que pudieramos acceder a nuestras pelis favoritas y de cada una de esas pelis favoritas pudieramos ver los datos personales del director 
'''basicamente tendriamos una estructura
donde estaria una funcion dentro de otra dentro de otra'''
'''la idea es amplicar el catalogo y este juego de pelis :star:'''

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


''                                               '''Encapsulacion de atributos y metodos'''

'''
nos dice que esta encerrado esta vinculado en temas de seguiridad una clse es un elemento donde encapsulamos siertos clases de metodos 
es como como una caja cerrada cierta informacion

es una variable que tiene informacion y tiene la capacidad de ejecutar ciertos metodos 
en python las class tienen un ambito publico esto no esta del todo bien ya que no es seguro 
ya que todo lo que le pedimos a python este nos lo devolvera sin ningun tipo de restriccion
'''

'''
la solicitud son tranmiciones de un espacio de problema a otro 
el problema es cuando se los da nos loda tal cual la informacion no esta codificado esta libre

cuando se intenta hakear codigo no es sencillo y leer su hambito de memoria 
es mas facil escuchar las comunicaciones de nuestro programa se comunique entre si 

nada deberia ser publico como es por defecto 
se puede hacer privado 
'''

'''
la solucion es tan facil
tenemoso que evitar a toda cosa que llamar a una variable me responda con su contenido 
'''
'''
debemos hacer privado nuestro atributo hay que decirle a python que nuestro atributo es privado
'''
'''
mi tranmicion no puede tener informacion tiene que tener una funcion ya que ellas no tiene la informacion
ya que ella recupera una posicion de memoria 
'''

'''encapsulacion

Consiste en denegar el acceso a los atributos y metodos de la clase desde el exterior
En python no exeste, pero se puede simular precidiendo atributos y metodos con dos varras bajas __:
'''

'''class Ejemplo:
    __atributo_privado = "Soy un atributo inalcazable desde afuera"
# se pueden hacer atributos privados con las variavbles globales y con las variables unicas     
    def __metodo_privado(self):
        print("Soy un metodo inalcanzable desde afuera")
# El programa principal (fuera de la clase Ejemplo)
e = Ejemplo()


#e.__atributo_privado# esto nos dara un error ya que estamos pidiendo en el main informacion que esta dentro de elemplo y que esta estaa en privado
# nos estamos intentado meter en ese atributo
print(e.__metodo_privado())
'''

'''
cada vez que queramos implementar un atributo privado siemrpe intentemos ponerle GETTERS Y SETTERS
no es obligatior pero es una recomendacion de desarrolladores

siempre hagamos atributos privados 
siempre implementemos el getter y setter en nuestros atributos 

__nombre
__edad

get edad
set edad
get nombre
set nombre

siempre mostrara la informacion de forma individual

 los metodos no nesecitan getter y setter ya que estos siempre estan vinculados a nuestro atributos

'''
''                                                                 '''Como acceder correctamente -> Getters y Setters'''

'''
Internamente la clase si puede acceder a sus atributos encapsulados, el truco consiste en acceder a ellos a traves de los GETTER y SETTER
correspondiente para las variables y crear metodos publicos que realicen internamente la llamada a los metodos privados
'''
class Ejemplo:
     
    __atributo_privado = 'Soy un atributo inalcanzable desde afuera '
    
    def __metodo_privado(self):
        print("Soy un atributo inalcanzable desde afuera")
        
    def metodo_publico(self):
        return self.__metodo_privado()
    #Getters                     nos permite ver lo que tenermos en privado 
    @property # la sintaxis es muy extraña
    def atributo_privado(self):
        print("Estoy en el getter")
        return self.__atributo_privado
    
    # setters                   nos permite modificar nuestra  informacion que esta en privado
    @atributo_privado.setter# el setter esta vinculado al getter vemos que esta con el nombre de la funcion del getter
    def atributo_privado(self,nuevoValor):
        print("Estoy en el setter")
        self.__atributo_privado = nuevoValor

# Programa principal (fuera de la clase Ejemplo)
e = Ejemplo()
#probamos a acceder a un atributo y observamos que se hacer a traves del getter
print(e.atributo_privado)
#python desea que accedamos a la informacion como vemos arriba como si no existiera un metodo getter y setter osea escribir el nombre de nuestra variable sin los dos __
e.atributo_privado  = "Hola he cambiado el atributo privado desde el setter"
print(e.atributo_privado)
# la ventaja de esto que no se ve como si estuviera encapsulada osea que nadie va a saber que algo esta encapsulado osea que se puede trabajar exactamente igual
'''
es este caso podemos ver que python nos permite tener 2 parametros que se llamen igual pero si nos damos cuenta tiene diferentes parametros uno tiene 
solo 1 y el otro tiene 2 y para python ambos son dieferentes por eso podemos llamar nuestra funciones igual pero sus parametros tiene que ser diferente
ya que su firma de su funcion debe ser diferente  osea cada uno original
'''
'''
__nombre
@property
def nombre:
@nombre.setter
def nombre:
nombre = variable nueva
'''
# Encapsulacion
'''
Consiste en denegar el acceso a los atributos internos de la classe desde el exterior.
En Python no existe, pero se puede simular precediendo atributo y metodos con dos barras bajas __:
'''
class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde afuera"
    
    def __metodo_privado(self):
        print("Soy un metodo inalcanzavle desde afuera")
    
    
    #getter
    @property
    def metodo_privado(self):
        return self.metodo_privado
    #setter
    @metodo_privado.setter
    def metodo_privado(self,nuevo_atributo):
         self.metodo_privado= nuevo_atributo
# Programa principal (fuera de la clase Ejemplo)
e = Ejemplo()
#print(e.__atributo_privado)
'''
Como se ve,  hemos asignado el nombre ver_valor al getter de la variable atributo_privado. Ha funcionado, pero ahora
nesecitamos recordar dos nombres de variable para poder acceder a una ... Por eso se utiliza el mismo nombre.
Lo que es importante, es que el nombre del metodo setter tiene que ser el mismo que el de su correspondiente getter.'''

#///////////////////////////////////////////'''''''Ejemplo con la clase persona''''''/////////////////////////////////////////     

class Persona:
    def __init__(self, nombre = None, edad = None):
        self.__nombre = nombre
        self.__edad = edad
        print("Se ha añadido a la persona")
    #Getters
    @property
    def nombre(self):
        print("Estoy en el getter de nombre")
        return self.__nombre
    #Setters
    @nombre.setter
    def nombre(self,nuevoNombre):
        print("Estoy en el setter de nombre")
        self.__nombre = nuevoNombre
    #Getter
    @property
    def edad(self):
        print("Estoy en el getter de edad")
        return self.__edad
    
    @edad.setter
    def edad(self,Edadnueva):
        print("Estoy en el setter de edad")
        self.__edad = Edadnueva

    def __str__(self):
        return 'la  persona es {} tiene  {} años'.format(self.nombre,self.edad)
        '' '''estructura de la Persona'''
'''
-init
-get/set
- metodos propios
-str

'''

p1 = Persona(nombre= "Carlos", edad= 30)
print(p1.nombre)
print(p1.edad)
            
print(p1)  
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#''                                                        '''Herencia'''
'''
Es el mecanismo por el cual un objeto puede adquirir 
propuedades y funcionalidades para las clases de las 
que se hereda (subclases) y de especializacion de las 
clases heredan (subclases)
'''

'''
la herencia nos permite no repetir codigo 
'''
# herencia Estructura paa los productos de una tienda
# ejemplo

# esto es un diagrama uml
'''
Producto
ID Producto
Nombre
Precio
Descripcion
'''
#podemos hacer diagramas de este tipo en Diagramas.net
# a nivel de documentacion siempre mejor poner un Diagrama de clases
class Producto:
    def __init__(self = None,Idprodructo = None,nombre = None,precio = None,descripcion = None):
        self.Idproducto = Idprodructo
        self.nombre = nombre
        self.precio = precio
        self.despcripcion = descripcion
        print("Constructor de la clase Producto")
    def saludar(self):
        print("Hey Dude...")    
    def __str__(self):
        return """-> PRODUCTO <-
    - IDProducto: {}
    - Nombre: {}
    - Precio: {}
    - Descripcion: {}

    """.format(self.Idproducto,self.nombre,self.precio,self.despcripcion)

#SUB CLASE ALIMENTO
class Alimento(Producto):  # esto es lo qye va a generar la herencia de esta clase
    
    def __init__(self,Idprodructo = None,nombre = None,precio = None,descripcion = None,Productor =None,Distribuidor = None):
        super().__init__(Idprodructo,nombre,precio,descripcion)#super hereda lo que esta dentro de nuestra herencia en este caso es Producto
        self.Productor = Productor
        self.Distribuidor = Distribuidor
        super().saludar    # vemos que podemos usar accesos a las funciones que tenga el padre sea lo que tenga padre
        
    def __str__(self):
        return """-> PRODUCTO <-
    - IDProducto: {}
    - Nombre: {}
    - Precio: {}
    - Descripcion: {}
    - Productor: {}
    - Distribuidor: {}""".format(self.Idproducto,
                                 self.nombre,
                                 self.precio,
                                 self.despcripcion,
                                 self.Productor,
                                 self.Distribuidor)
    
alimento1 = Alimento(2056,"aceite",500,"botella de aceite natural","la Aceitera","Distribuiciones Sl")
alimento2 = Alimento(5514,"cuchillo de cocina",600,"cuchillo de acero inoxidable","MASD","Dist SM")
print(alimento1.nombre)
print(alimento2.nombre)

if alimento1 is not None and alimento2 is not None:
    precioTotal = alimento1.precio + alimento2.precio # Esto puede dar error porque suma 5 + None
else:
    print(" > Error de precios")

#Sub clase Libro    
class Libro(Producto):
    isbn = None
    autor = ""
    def __str__(self):
        return  """-> PRODUCTO <-
    - IDProducto: {}
    - Nombre: {}
    - Precio: {}
    - Descripcion: {}
    - isbn {}
    - autor {}""".format(self.Idproducto,
                         self.nombre,
                         self.precio,
                         self.despcripcion,
                         self.isbn,
                         self.autor)
# Subclase ropa    
class Ropa(Producto):
    Talla = ""
    Marca = ""
    def __str__(self):
        return  """-> PRODUCTO <-
    - IDProducto: {}
    - Nombre: {}
    - Precio: {}
    - Descripcion: {}
    - ISBN: {}
    - Autor {}""".format(self.Idproducto,
                         self.nombre,
                         self.precio,
                         self.despcripcion,
                         self.Talla,
                         self.Marca)
    
    
al = Alimento(46687,"Botella de Aceite de Olvia Extra Virgen",5,"250ML")
al.Productor = "La aceitera"
al.Distribuidor= "Distribuidores SA"

li = Libro(23456,"Cocina Japonesa",26,"Recetario de la abuela jimm recetas del oriente")
li.isbn = "36"
li.autor = "La abuela Jim"

ro = Ropa(111334,"Jersey Fit",18,"Jersey de hombre de invierno")
ro.Talla = "Xl"
ro.Marca = "Gucci"

print(al)
print(li)
print(ro)    

productos = [al, li, ro]
for r in productos:
    print(r,"\n")# asi es como mostramos ahora la informacion

#Tendremos que tratar cada subclase de forma distinta, gracias a la funcion isistance()
for p in productos:
    if(isinstance(p,Alimento) ):
        print(p.Idproducto, "-> ",p.nombre, "->", p.Productor )
    elif(isinstance(p,Libro) ):
        print(p.Idproducto, "-> ",p.nombre, "->", p.isbn)
    elif(isinstance(p,Ropa)):
        print(p.Idproducto, "-> ",p.nombre, "->", p.Marca)
                

# tengo que escribir tantos atributos como los tenga en el objeto tenemos que ser consecuientes con lo hacemos si le metemos 6 objetos hago 6 atributos
'Uso de Super'
'''
Hasta ahora, hermos definido las clases hijas sin constructor, de tal modo, cuando un objeto de estas clases
hijas, usan el constructor del padre para construirse. Este mecanismo puede estar bien cuando nuestras clases hijas
no tienen atributos especificos o tienen muy pocos, su forma de crearse difere mucho de la fima de su padre? En este
caso tenemos que utilizar el metodo especial super()

El metodo super() invocado desde una clase hija, hacer referencia al padre. Por lo tanto, super() solo funciona cuando 
tenermos una estructura de herencia.

podemos utilizar super() con el siguiente formato: super().cualquier_metodo_de_la_ckse_padre()

veamos un ejemplo a continuacion, la clase alimenro que hereda producto tuene su propip cosntructor, donde realiza dos tareas
definir sus atributos propios(productor y distribuidor)
invocar al constructor del padre con super.() __init__() y enciale por parametro los atributos comunes que pertenecen a la 
clase del padre(referencia,nombre,pvp y descripcion)

Es muy importante que el numero y orden de los parametros que enciamos desde el hijo(con super().__init__())
al padre, sean los mismos que en numero y orden que los que hau definidos en el contructor del padre.
'''


''                                     '''Bonus: Comprobar si una clase hereda de otra'''

class Vehiculo():
    pass
class Coche(Vehiculo):
    pass
class Gato():
    pass
print(issubclass(Coche,Vehiculo))# Coche hereda de Vehiculo?
print(issubclass(Gato,Vehiculo))# Gato hereda de Vehiculo?

''                                                         ''' Clases, objetos (ejemplos) '''

'Ejemplo Vehiculo'

'''
En este caso veremos una estructura de herencia deonde la clase hija (Furgoneta)
no tiene constructor propio. Esto es asi por una cuestion de diseño de nuestro problema.
En este caso, se ha definido la clase Furgoneta e tal moso que no tiene atributos propios, 
por lo tanto, para su construccion, basta con la uilizacion del constructor del padre(Vehiculo)
'''

class Vehiculo:
    '''
    Clase Vehiculo
    incluye la marca un modelo de un vehiculo. Por defecto el vehiculo no esta marcha,
    ni acelerando ni frenando
    
    args
    - marca: Es un String que compone la marca del vehiculo
    - modelo: Es un Sring que compone el modelo del vehiculo
    - en_marcha: Es un booleano que indica si el vehiculo esta en marcha o no(por defecto a False)
    '''
    #Constructor
    def __init__(self,marca,modelo,en_marcha = False):
        ''' Constructor de la clase vehiculos'''
        self.__marca = marca
        self.__modelo = modelo
        self.__en_marcha = en_marcha
        print("Vehiculo creado")
        
    #Getters y setter    
    @property
    def marca(self):
        '''Metodo getter del atributo marca'''
        return self.__marca
    
    @marca.setter
    def marca(self,nuevo):
        '''Metodo setter del atributo marca'''
        self.__marca = nuevo
    
    @property
    def modelo(self):
        '''Metodo getter del atributo modelo'''
        return self.__modelo
    
    @modelo.setter
    def modelo(self,nuevo):
        '''Metodo setter del atributo modelo'''
        self.__modelo = nuevo
        
    @property
    def en_marcha(self):
        '''Metodo getter del atributo en_marcha'''
        return self.__en_marcha
    
    @en_marcha.setter
    def en_marcha(self,nuevo):
        '''Metodo setter del atributo en_marcha'''
        self.__en_marcha = nuevo
    
    # Metodos de la clase
    def arrancar(self):
        '''Metodo arrancar() del la calse Vehiculos. Indica al sistema que el vehiculo en marcha'''
        self.arrancar = True
    def parar(self):
        '''Metodo parar() de la clase Vehiculo. Indica al sistema que el vehiculo esta parado'''
        self.arrancar = False    
    def __str__(self):
        '''Metodo __str__() de la clase Vehiculos. Indica al sistema el estado del vehiculo'''
        return "> Marca {}\n > Modelo: {}\n > En Marcha: {}".format(self.marca,self.modelo,self.en_marcha)
    
class Furgoneta(Vehiculo):
    '''Clase Furgoneta que hereda de Vehiculos'''
    def cargada(self,estado):
        '''Metodo cargada() de al clase Furgoneta. Indica al sistema si la furgoneta esta cargada o no'''
        if (estado == True):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

# Objeto de la valse Furgoneta
miFurgoneta = Furgoneta("Renult","Kangoo")
# Ejecutamos metodos del padre
print("Marca:",miFurgoneta)
print("Furgoneta en estadon inicial")
print(miFurgoneta)

miFurgoneta.arrancar() # arrancamos la furgoneta
print("Furgoneta tras arrancar")
print(miFurgoneta)

#Ejecutamos metodos del hijo
estadoFurgonetaCargada = miFurgoneta.cargada(True)
print(estadoFurgonetaCargada)

#veamos la documentacion de nuestra clase recien creada
help(Vehiculo)
help(Furgoneta)
''                                                ''' Ejemplo Persona-Empleado'''
'''
Eh este ejemplo veremos una estructura de herencia donde la clase hija(empleado) si tiene constructor propio.Esto es asi por ua cuestion de diseño
de nuestro problema. En este caso, se ha definido la clase Empleado de tal modo que si tiene atributos propios(salario y antiguedad), por lo tanto,
para su construccion, requiere de un constructor propio.
'''
class Persona():
    # constructor
    def __init__(self,nombre,edad,lugar_residencia):
        self.__nombre = nombre
        self.__edad = edad
        self.__lugar_residencia = lugar_residencia
        print("Persona creada")
        
    # Getters Y Setters
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nuevo):
        self.__nombre = nuevo
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self,nuevo):
        self.__edad= nuevo
    @property
    def lugar_residencia(self):
        return self.__lugar_residencia
    @lugar_residencia.setter
    def lugar_residencia(self,nuevo):
        self.__lugar_residencia= nuevo
        
    def __str__(self):
        return """> Nombre: {}\n Apellido: {}\n Lugar de residencia: {}""".format(self.nombre,self.edad,self.lugar_residencia)

class Empleado(Persona):
    def __init__(self,salario,antiguedad, nombre, edad, lugar_residencia):
        super().__init__(nombre, edad, lugar_residencia)
        self.__salario = salario
        self.__antiguedad = antiguedad
        print("Empleado creado")
    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self,nuevo):
        self.__salario = nuevo
    @property
    def antiguedad(self):
        return self.__antiguedad
    @antiguedad.setter
    def antiguedad(self,nuevo):
        self.__antiguedad= nuevo
    
    def __str__(self):
        return super().__str__() + "\n Salario: {}\n Antiguedad: {}".format(self.__salario,self.__antiguedad)
    
# creamos objeto de la clase hija Empleado
e1 = Empleado(nombre="Ana",edad="45",lugar_residencia="Barcelona",salario=456675,antiguedad="20 años")
print(e1)

e2 = Empleado(nombre="santiago",edad="21",lugar_residencia="Madrid",salario=5000,antiguedad="22 años")
print(e2)
# comprobacion de qu eun objeto es una instancia de una clase determinada
print(isinstance(e1,Persona))
print(isinstance(e1,Empleado))

#terminamos modulo 3 

b= int(input("Escriba una valor para base"))
a =int(input("Escriba un valor para altura"))
print("Su perimetro es",p=b*a)



