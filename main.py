# Importar librerias
import os
import time
import sqlite3
from datetime import date
import hashlib

# Declaramos varialbes

usuarios = []
password = []


# Declara la funcion LP para limpiar la termianl

def LP():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system ("cls")
            
# Iniciar la base de datos 
con = sqlite3.connect("DataBase.db3")

cur = con.cursor()
#cur.execute(" CREATE TABLE banco ( user	TEXT NOT NULL UNIQUE, password	TEXT NOT NULL, ahorro	REAL, corriente	REAL, interes	INTEGER NOT NULL, cuenta TEXT NOT NULL, documento REAL NOT NULL, PRIMARY KEY(user))")

# Recupera los usuarios de la base de datos
cur.execute("SELECT user FROM banco")
usuarios = cur.fetchall()

# Primer Menu

print(" Elija una opcion")
print("1) inicio de sesion")
print("2) creacion de cuenta")


a = int(input())

# Validacion del primer menu
while (not ((a == 1) or (a == 2))):
  print("Parametro incorrecto vuelve a intentar")
  a = int(input())

  # Opcion creacion de una cuenta bancaria  
if a == 2:
    LP()
    usuarion = str(input("Ingrese Usuario nuevo: "))
     
    
     
     # Validacion del la longitud del uaurio
    while (len(usuarion)) <= 3:
         print("Usuario demaciado corto , intente nuevamente")
         time.sleep(2)
         LP()
         usuarion = str(input("Ingrese Usuario nuevo: "))
      
      
      # Validacion de la ausencia de otros usuarios
    for usuario in usuarios:
        usuariont = usuario[0]
        while usuarion ==  usuariont:
          LP()
          print("El nombre de usuario ya esta registrado")
          print("pruebe con un usuario diferente ")
          usuarion = str(input("Ingrese Usuario nuevo: "))
                




# Ingreso de contraseña
    LP()
    contn = input("Ingrese contraseña: ")
             
                  
             # Validacion del la longitud del uaurio
    while (len(contn) < 7):
        print("La contraseña debe contener minimo 8 caracteres")
        time.sleep(2)
        LP()
        
        contn = input("Ingrese contraseña: ")
          
          
          # Validacion de la contraseña
    contn0 = input("Confierme su contraseña: ")
    while contn != contn0:
        print("Las contraseñas no coinciden , intente nuevamente")
        time.sleep(2)
        LP()
        contn0 = input("Confierme su contraseña: ")
        
        
          #Validacion de edad minima permitida por la ley
    dian = input("dia de nacimiento: ")
    mesn = input("mes de nacimiento: ")
    yearn = input("año de nacimiento: ")
    
    print("su fecha de nacimiento es :", dian, "/", mesn, "/", yearn)
    
    print("1) Confirmar")
    print("2) Cancelar")
    
    a = int(input())
    
    if a == 2:
      con.close()
      exit()
    elif a == 1:
        daten = date(int(yearn), int(mesn), int(dian))
        hoy = date.today()
        datenv = (hoy - daten).days
        if (datenv/365) > 13:
          LP()
# ingreso de documento de identidad
          idn = input("Ingrese su documento de identidad: ")
          while (len(idn) < 7) or (len(contn) > 10):
             if (len(idn) < 7):
              print("El documento debe tener al menos 8 numeros")
             elif (len(idn) > 10):
                print("El documento debe tener maximo 10 numeros")
             time.sleep(2)
             LP()
             idn = input("Ingrese su documento de identidad: ")
        else:
          con.close()
          exit()

        
    # Crear numer de cuenta
    cuidgen = str(usuarion + idn)
    cuid = "bancoean:" + (hashlib.sha256(cuidgen.encode())).hexdigest()


    
    basein = [(usuarion , contn , 0 , 0 , 0.0 ,  cuid , int(idn) )]
#    print(basein)
    cur.executemany("INSERT INTO banco VALUES (?,?,?,?,?,?,?)", basein)
    con.commit()  
    cur.execute("SELECT user FROM banco")
    usuarios = cur.fetchall()


# Opcion inicio de secion 
if a == 1:
  usuariol = input("ingresa tu usuario: ")
  for usuario in usuarios:
      usuariont = usuario[0]
      if usuariol ==  usuariont:
        cur.execute("SELECT password FROM banco WHERE user = ?", [usuario[0]])
        passwr = cur.fetchall()

  passw = input("ingresa contraseña: ")
  if passwr[0][0] == passw :
    print("aceptad")