from pyfiglet import Figlet
from limpiarpantalla import LP


# Primer Menu
def opciones2(opcion1,opcion2):
  print("[1]", opcion1)
  print("[2]", opcion2)
  print()

def opcionesfech():
  print("[1] Enero")
  print("[2] Febrero")
  print("[3] Marzo")
  print("[4] Abril")
  print("[5] Mayo")
  print("[6] Junio")
  print("[7] Julio")
  print("[8] Agosto")
  print("[9] Septiembre")
  print("[10] Octubre")
  print("[11] Noviebre")
  print("[12] Diciembre")


def menu(texto):
  LP()
  print(Figlet(font='5lineoblique').renderText("Banco EAN"))

  print((texto).center (round(len(texto)*1.3), '-'))

def menu2(texto1, texto2):

  if ((round(len(texto1)*1.3)) >= (round(len(texto2)*1.3))):
    max = (round(len(texto1)*1.3))
  else:
    max = (round(len(texto2)*1.3))
  LP()
  print(Figlet(font='5lineoblique').renderText("Banco EAN"))
  print((texto1).center (max, '-'))
  print((texto2).center (max, '-'))

  