from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Aqui deberia tener la configuracion de la bases de datos
'''
vamos a nesecitas 3 pasos:
- El engine permite a SQLAlchemy comunicarse con la base de datos de un dialecto concreto
. https://docs.sqltalchemy.org/en/14/core/engines.html

- la seccion que podemos realizar operaciones sobre la bases de datos, guardar, hacer una peticion, etc

- base va a hacer la encargada de poder decirles a nuestras clases, que se van a transformar en tablas
'''
# Advertencia: Crear el engine no conecta inmediatamente con la BD
# Eso lo hacemos 

engine = create_engine("sqlite:///database/personas.db") # engine le dice en que idioma hablar
# sqlite es el dialecto

# Ahora creamos la seccion lo que nos permite realizar transacciones (operaciones) dentro de nuesta bd
Session = sessionmaker(bind=engine)  # esto crea una clase especial que es la session
session = Session()

# Ahora vamos al fichero models.py en en los modelos (clases)donde queremos que se transformen en tablas, 
# le añadiremos esta variable y esto se encargara de mapear y vincular cada clase a cada tabla
Base = declarative_base()

