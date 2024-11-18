import os

def listar_archivos(directorio):
    try:
        contenido = os.listdir(directorio)
        archivos = [f for f in contenido if os.path.isfile(os.path.join(directorio, f))]
        for archivo in archivos:
            print(archivo)
    except FileNotFoundError:
        print(f"El directorio {directorio} no existe.")
    except PermissionError:
        print(f"No tienes permiso para acceder al directorio {directorio}.")

# Llama a la función con el directorio que quieres listar
listar_archivos('/Users/jeissonnino/Python TAFE')
