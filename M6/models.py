from sqlalchemy import Column, Integer, String
import db


class Persona(db.Base):
    #__tablename nombre de la tabla
    __tablename__ = "persona" 
    # va ha ser un diccionario de diferentes claves y valores con informacion de configuracion de esta tabla 
    # le pones una columna que identifique e incremente
    # seriales
    __table_args__ = {"sqlite_autoincrement": True} # Esto Autoincrementa la Primary Key (PK) de la tabla

    id_persona = Column(Integer,primary_key = True) # indentificador de persona
    nombre = Column(String,nullable = False) # nullable Esto hace que el campo nombre No pueda estar vacio
    edad = Column(Integer) # Edad es un entero y puede o no tener valor
    mail = Column(String,nullable = False) # mail es un str y NO puede estar vacio


    def __init__(self, nombre , apellido, edad, mail):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.mail = mail
    
    def __str__(self):
        return """Persona (Nombre: {} {} 
                            Edad: {} 
                            mail: {})""".format(self.nombre,
                                                self.apellido,
                                                self.edad,
                                                self.mail)
    