from pyfiglet import Figlet
from limpiarpantalla import LP


# Primer Menu
def inicio():
  LP()
  print(Figlet(font='5lineoblique').renderText("Banco EAN"))

  print((" Elija una opcion ").center (45, '-'))
  print("[1] inicio de sesion")
  print("[2] creacion de cuenta")

  