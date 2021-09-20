# Importar librerias
import os
import sys
import time
import sqlite3
from datetime import date
import hashlib
from pyfiglet import Figlet

# Declaramos varialbes


password = []

# importar funciones
sys.path.append("./src/funciones")
from menues import *


# Declara la funcion LP para limpiar la termianl


def LP():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


# Iniciar la base de datos
con = sqlite3.connect("DataBase.db3")

cur = con.cursor()

try:
    cur.execute(
        " CREATE TABLE banco ( user	TEXT NOT NULL UNIQUE, password	TEXT NOT NULL, tipo	TEXT NOT NULL, saldo FLOAT NOT NULL, interes FLOAT NOT NULL, cuenta TEXT NOT NULL, documento INT NOT NULL, ufech TEXT NOT NULL , promm FLOAT NOT NULL , PRIMARY KEY(user))"
    )
except:
    pass

# Primer Menu
menu("Elije una opcion")
opciones2("Inicio de sesion", "Creacion de cuenta")

while True:
    # Validacion del primer menu
    try:
        a = int(input())
        break
    except:
        menu2("Elije una opcion", "Parametro incorrecto vuelve a intentar")

        while not ((a == 1) or (a == 2)):
            menu2("Elije una opcion", "Parametro incorrecto vuelve a intentar")
            a = int(input())


# Opcion creacion de una cuenta bancaria
if a == 2:
    menu("Ingresa tu nuevo usuario")
    usuarion = str(input())
    # Validacion del la longitud del uaurio
    while (len(usuarion)) <= 3:
        menu("Usuario demaciado corto , intente nuevamente")
        usuarion = str(input())

    # Validacion de la ausencia de otros usuarios
    cur.execute("SELECT user FROM banco")
    usuarios = cur.fetchall()
    for usuario in usuarios:
        usuariont = usuario[0]
        while usuarion == usuariont:
            menu2(
                "Ese nombre de usuario ya esta registrado",
                "pruebe con un usuario diferente",
            )
            usuarion = str(input())

    # Ingreso de contraseña
    menu("Ingresa tu nueva contraseña")
    contn = input()

    # Validacion del la longitud del uaurio
    while len(contn) < 7:
        menu2(
            "Ingresa tu nueva contraseña",
            "La contraseña debe contener minimo 8 caracteres",
        )
        contn = input("")

        # Validacion de la contraseña
    menu("Confirma tu contraseña")
    contn0 = input("")
    while contn != contn0:
        menu2(
            "Confirma tu contraseña",
            "Las contraseñas no coinciden - intenta nuevamente",
        )
        contn0 = input("")

    # Validacion de edad minima permitida por la ley
    a = 2
    while a == 2:
        while True:
            try:
                menu("Dijita tu dia de nacimiento")
                dian = int(input())
                while (dian > 31) or dian < 0:
                    menu2(
                        "Dijita tu dia de nacimiento",
                        "Verifica que el dato introducido sea un dia del calendario",
                    )
                    dian = int(input())
                break
            except:
                pass

        while True:
            try:
                menu("Dijita tu mes de nacimiento")
                opcionesfech()
                mesn = int(input())
                while (mesn > 12) or mesn < 0:
                    menu2(
                        "Dijita tu mes de nacimiento",
                        "Verifica que el dato introducido sea un mes del calendario",
                    )
                    opcionesfech()
                    mesn = int(input())
                break
            except:
                pass

        while True:
            try:
                menu("Dijita tu año de nacimiento")
                yearn = int(input())
                while yearn < 1903:
                    menu2(
                        "Dijita tu año de nacimiento",
                        "Verifica que el dato introducido sea un año del calendario",
                    )
                    yearn = int(input())
                break
            except:
                pass

        menu2(
            "Verifica que tu fecha de nacimiento sea la correcta",
            str(str(dian) + "/" + str(mesn) + "/" + str(yearn)),
        )
        opciones2("Los datos son correctos", "Los datos no son correctos")
        a = int(input())

    if a == 1:
        daten = date(int(yearn), int(mesn), int(dian))
        hoy = date.today()
        datenv = (hoy - daten).days
        if (datenv / 365) > 13:

            # ingreso de documento de identidad
            menu("Ingresa tu numero de documento de identidad")
            while True:
                try:
                    idn = int(input())
                    while (len(str(idn)) < 7) or (len(str(idn)) > 10):
                        if len(str(idn)) < 7:
                            menu2(
                                "Ingresa tu numero de documento de identidad nuevamente",
                                "El documento debe tener al menos 8 numeros",
                            )
                            idn = int(input())
                        elif len(str(idn)) > 10:
                            menu2(
                                "Ingresa tu numero de documento de identidad nuevamente "
                                "El documento debe tener maximo 10 numeros"
                            )
                            idn = int(input())
                    break
                except:
                    menu2(
                        "Ingresa tu numero de documento de identidad nuevamente ",
                        "El documento debe ser un numero",
                    )
        else:
            menu()
            print(
                "Gracias por tu interes en nuestros servicos pero necesitas tener mas de 13 años para poder tener acceaso a este servicio"
            )
            print()
            exit()

    # TIpo de cuenta para el usuario nuevo

    while True:
        try:
            menu("Elige tu tipo de cuenta")
            opciones2("Ahorros", "Corriente")
            tipob = int(input())

            while not ((tipob == 1) or (tipob == 2)):
                menu2(
                    "Elige tu tipo de cuenta",
                    "Verifica que el dato introducido sea una opcion valida",
                )
                opciones2("Ahorros", "Corriente")
                tipob = int(input())

            if tipob == 1:
                tipo = "AHORROS"
            elif tipob == 2:
                tipo = "CORRIENTE"

            break
        except:
            pass

    # Crear numer de cuenta
    cuidgen = str(usuarion + str(idn))
    cuid = "bancoean:" + (hashlib.sha256(cuidgen.encode())).hexdigest()

    basein = [(usuarion, contn, tipo, 0, 0.0, cuid, int(idn), date.today(), 0.0)]
    #    print(basein)
    cur.executemany("INSERT INTO banco VALUES (?,?,?,?,?,?,?,?,?)", basein)
    con.commit()

    del usuarion
    del contn
    del tipo
    del cuid
    del idn

    # Le preguntamos al usuario si quiere terminar el programa o iniciar seccion
    menu("Usuario Registrado Exitosamente")
    while True:
        try:
            opciones2("Iniciar secion", "Cerrar Programa")
            a = int(input())
            while not (a == 1 or a == 2):
                menu2(
                    "Usuario Registrado Exitosamente",
                    "Paramtro invalida, intenta otravez",
                )
                opciones2("Iniciar Seccion", "Cerrar Programa")
                a = int(input())
            break
        except:
            menu2(
                "Usuario Registrado Exitosamente", "Paramtro invalida, intenta otravez"
            )

    if a == 2:
        menu("Gracias por usar nuestros servicios")
        exit()

# Opcion inicio de secion
if a == 1:
    cur.execute("SELECT user FROM banco")
    usuarios = cur.fetchall()

    menu2("Bienvenido", "Por favor ingresa tu usuario")
    usuariol = input()
    for usuario in usuarios:
        usuariont = usuario[0]
        if usuariol == usuariont:
            cur.execute("SELECT password FROM banco WHERE user = ?", [usuario[0]])
            passwr = cur.fetchall()

    while len(passwr) == 0:
        menu2(
            "Bienvenido - ingresa tu usuario",
            "parece que ese usuario no exite - intenta otra vez",
        )
        usuariol = input()
        for usuario in usuarios:
            usuariont = usuario[0]
            if usuariol == usuariont:
                cur.execute("SELECT password FROM banco WHERE user = ?", [usuario[0]])
                passwr = cur.fetchall()

    passw = input("ingresa contraseña: ")
    if not passwr[0][0] == passw:
        while (not passwr[0][0] == passw and not passw == str("1")) or (
            not (not passwr[0][0] == passw and passw == str("1"))
        ):
            LP()
            print("Si olvidaste tu contraseña dijita 1")
            print("Puedes volver a intentar ")
            passw = input("ingresa contraseña: ")
        if passw == "1":
            LP()
            print(
                "para recuperar su contraseña dirijase a uno de nuestros puntos de atencion para validacion humana, gracias por su colaboracion"
            )
            print("gracias por confiar en nostros")
            print()
            print("Banco")
            exit()
    elif passwr[0][0] == passw:
        menu("Acceso correcto para " + usuariol)
        time.sleep(2)
        while True:
            cur.execute("SELECT saldo FROM banco WHERE user = ?", [usuariol])
            saldo = cur.fetchall()[0][0]
            cur.execute("SELECT tipo FROM banco WHERE user = ?", [usuariol])
            tipo = cur.fetchall()[0][0]
            cur.execute("SELECT interes FROM banco WHERE user = ?", [usuariol])
            interes = cur.fetchall()[0][0]
            cur.execute("SELECT cuenta FROM banco WHERE user = ?", [usuariol])
            cuenta = cur.fetchall()[0][0]
            cur.execute("SELECT ufech FROM banco WHERE user = ?", [usuariol])
            ufech = cur.fetchall()[0][0]
            cur.execute("SELECT promm FROM banco WHERE user = ?", [usuariol])
            promm = cur.fetchall()[0][0]

            # Calculo de interes

            if tipo == "AHORROS":

                if promm == 0:
                    cur.executemany(
                        "UPDATE banco SET promm = ? WHERE user = ?",
                        [(saldo, usuario[0])],
                    )
                    con.commit()
                    cur.executemany(
                        "UPDATE banco SET ufech = ? WHERE user = ?",
                        [(date.today(), usuario[0])],
                    )
                    con.commit()
                else:
                    promm = (promm + saldo) / 2
                    cur.executemany(
                        "UPDATE banco SET promm = ? WHERE user = ?",
                        [(promm, usuario[0])],
                    )
                    con.commit()
                    cur.executemany(
                        "UPDATE banco SET ufech = ? WHERE user = ?",
                        [(date.today(), usuario[0])],
                    )
                    con.commit()

                # Calculo del interes

                datei = date(
                    int(ufech.split("-")[0]),
                    int(ufech.split("-")[1]),
                    int(ufech.split("-")[2]),
                )
                hoy = date.today()
                dias = (hoy - datei).days
                if dias < 30:
                    data = (interes / 100 / 30 * dias * promm) + saldo
                    cur.executemany(
                        "UPDATE banco SET saldo = ? WHERE user = ?",
                        [(data, usuario[0])],
                    )
                    con.commit()
                else:
                    data = (interes / 100 / 30 * dias * saldo) + saldo
                    cur.executemany(
                        "UPDATE banco SET saldo = ? WHERE user = ?",
                        [(data, usuario[0])],
                    )
                    con.commit()
                    cur.execute(
                        "UPDATE banco SET promm = 0 WHERE user = ?", [usuario[0]]
                    )
                    con.commit()

                # Interfaz del suario

            break

        # Opción de eliminar cuenta

        while True:
            menu("Elije una opción")
            opciones = ["Realizar una transferencia", "Retirar dinero", "Revisar saldo" , "Eliminar cuenta", "Salir"]
            multiples_opciones(opciones)

            try:
                opcion = int(input())
            except:
                continue

            if opcion == 1:
                # Opción de hacer transferencias
                menu("Ingresa el monto a transferir")
                while True:
                    print("Tu saldo:", saldo)
                    try:
                        monto = float(input())
                    except Exception:
                        menu2(
                            "Monto invalido", "Ingresa nuevamente el monto a transferir"
                        )
                        continue

                    # Verificar que el monto a enviar sea menor al sado
                    if monto > saldo:
                        menu2(
                            "El monto excede el saldo en tu cuenta",
                            "Ingresa nuevamente el monto a transferir",
                        )
                        continue

                    if monto < 1:
                        menu2(
                            "Monto invalido",
                            "Ingresa nuevamente el monto a transferir",
                        )
                        continue

                    menu(
                        "Selecciona el tipo de cuenta del receptor de la transferencia"
                    )
                    while True:
                        opciones2("Ahorros", "Corriente")
                        opcion = input()
                        if opcion not in ("1", "2"):
                            menu2(
                                "Selecciona el tipo de cuenta del receptor de la transferencia",
                                "Selección incorrecta, selecciona nuevamente",
                            )
                            continue

                        tipo_cuenta_receptor = (
                            "AHORROS" if opcion == "1" else "CORRIENTE"
                        )

                        menu("Ingresa el numero de cuenta del receptor")
                        while True:
                            cuenta_destino = input()
                            cuid_input = cuenta_destino
                            cur.execute(
                                "SELECT tipo, saldo FROM banco WHERE cuenta = ?",
                                [cuid_input],
                            )
                            cuid_receptor = cur.fetchone()
                            if not cuid_receptor:
                                menu2(
                                    "Ingresa el numero de cuenta del receptor",
                                    "Número de cuenta invalido",
                                )
                                continue
                            if tipo_cuenta_receptor != cuid_receptor[0]:
                                menu(
                                    f"El receptor de la transferencia no tiene una cuenta de tipo {tipo_cuenta_receptor}"
                                )
                                break

                            # validación final
                            while True:
                                menu("Escriba `si` para confirmar su transacción")
                                cur.execute(
                                    "SELECT documento FROM banco WHERE user = ?",
                                    [usuariol],
                                )
                                documento_usuario = cur.fetchone()[0]

                                print(
                                    f"Su cuenta: {usuariol}{documento_usuario} - {tipo}"
                                )
                                print(
                                    f"Cuenta destino: {cuenta_destino} - {cuid_receptor[0]}"
                                )
                                print(f"Monto transacción: ${monto}")
                                confirmacion_transaccion = input("> ")
                                if confirmacion_transaccion.lower() == "si":

                                    # Actualiza los montos en ambas cuentas
                                    saldo_receptor = cuid_receptor[1]
                                    saldo_receptor += monto
                                    cur.execute(
                                        "UPDATE banco SET saldo = ? WHERE cuenta = ?",
                                        [saldo_receptor, cuid_input],
                                    )

                                    saldo -= monto
                                    cur.execute(
                                        "UPDATE banco SET saldo = ? WHERE cuenta = ?",
                                        [saldo, cuenta],
                                    )
                                    con.commit()
                                    menu("Transferencia realizada exitosamente.")
                                    time.sleep(2)
                                    break
                            break
                        break
                    break

            elif opcion == 2 :
                menu("Cuanto dinero desea retirar:")
                opciones=[20, 40, 60, 80]
                multiples_opciones(opciones)
                if retirar>saldo:
                  print("No tiene esa cantidad de dinero:(")
                else:
                  saldo -= retirar
                  print("Dinero en la cuenta:"+str(saldo))
                      

            elif opcion == 3 :
                 print("Dinero en la cuenta:"+str(saldo))
		

           ##Recargar la cuenta
            elif opcion == 4 :
                # Confirmación de remover cuenta
                menu(
                    "Estas seguro de que deseas eliminar tu cuenta? Escribe `si` para confirmar"
                )
                confirmacion = input()
                if confirmacion.lower() == "si":
                    intentos = 0
                    menu("Ingresa tu contraseña")
                    while True:
                        if intentos >= 3:
                            menu(
                                "Máximo de intentos (3) alcanzados. Volviendo al menú."
                            )
                            time.sleep(2)
                            break
                        password_ = input()
                        if passwr[0][0] != password_:
                            intentos += 1
                            menu2(
                                "Ingresa tu contraseña",
                                f"Contraseña inválida. Intento # {intentos}",
                            )

                        else:
                            cur.execute("DELETE FROM banco WHERE user=?;", [usuariol])
                            con.commit()
                            print(
                                "Cuenta eliminada exitosamente. Saliendo del sistema..."
                            )
                            exit()

            elif opcion == 5:
                LP()
                print("Saliendo del sistema...")
                exit()


con.close()
