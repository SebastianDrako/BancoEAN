import os

# Declara la funcion LP para limpiar la termianl

def LP():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system ("cls")