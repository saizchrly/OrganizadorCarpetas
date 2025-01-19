import os
import shutil
from pathlib import Path
"""
Con este pequeño script tengo la intencion de organizar la carpeta de descargas de mi computadora
en subcarpetas basadas en las extensiones de los archivos.

En caso de querer cambiar la carpeta a organizar simplemente se debe cambiar la siguiente linea, con
la ruta de la carpeta deseada.

"""
# Cambiar en caso de necesitarlo, poner el nombre de la carpeta
CARPETA = str( Path.home() / "Downloads" )

# Diccionario de organizacion

ORGANIZACION = {"imagenes": [".jpg", ".jpeg", ".png", ".gif", ".drawio"], 
                "documentos": [".docx", ".txt", ".pptx", ".xlsx", ".csv", ".odt", ".ods", ".odp", ".doc", ".ppt", ".xls"],
                "pdfs": [".pdf"],
                "videos": [".mp4", ".avi", ".mov"],
                "musica": [".mp3", ".wav", ".aac"],
                "archivos_comprimidos": [".zip", ".rar", ".tar.gz", ".7z"],
                "instaladores": [".exe", ".msi", ".deb", ".bat"],
                "SO": [".iso"],
                "maquinas_virtuales": [".vdi", ".vmdk", ".ova"],
                "python": [".py", ".ipynb"],
                "java": [".jar", ".java"],
                "c#": [".cs"],
                "3d": [".stl", ".obj", ".fbx"],
                "borrar": [".nbt", ".gexf", ".log", ".properties", ".dat", ".toml"],
                
                
                }

def colocar_en_carpeta(carpeta_organizar, archivo):
    errores = []
    
    # Obtenemos la extensión del archivo
    extension = Path(archivo).suffix.lower()
    
    for key, value in ORGANIZACION.items():
        if extension in value:
            #creamos la subcarpeta, si no existe
            subcarpeta = os.path.join(carpeta_organizar, key)
            os.makedirs(subcarpeta, exist_ok=True)
            
            # Movemos el archivo a la subcarpeta correspondiente
            try:
                shutil.move(os.path.join(carpeta_organizar, archivo), os.path.join(subcarpeta, archivo))
            except shutil.Error as e:
                errores.append((archivo, str(e)))
            return errores
    return errores
   


# Definimos la función principal del programa
def organizar_descargas(carpeta_organizar):
    """
    Organiza los archivos de la carpeta requerida en subcarpetas basadas en sus extensiones.

    Args:
        carpeta_organizar (str): Ruta de la carpeta de Descargas.
    """
    # Definimos una lista para registrar los errores encontrados
    errores = []
    erroresColocar = []
    
    # Buscamos la carpeta, si no exisite finalizamos el programa
    if not os.path.exists(carpeta_organizar):
        print(f"Error: La carpeta '{carpeta_organizar}' no existe.")
        input("Presiona Enter para continuar...")
        return

    # Recorremos todos los archivos de la carpeta de Descargas
    for archivo in os.listdir(carpeta_organizar):
        ruta_archivo = os.path.join(carpeta_organizar, archivo)

        # Continuamos solo si es un archivo
        if not os.path.isfile(ruta_archivo):
            # si no es un archivo, saltamos el codigo y continuamos con el siguiente archivo
            continue

        # Colocamos el archivo en la subcarpeta correspondiente, y registramos los errores si los hubo
        erroresColocar = colocar_en_carpeta(carpeta_organizar, archivo)
        if erroresColocar != []:
            for x in erroresColocar:
                errores.append(x)

    # Informamos sobre los errores, si los hubo
    if errores:
        print("Errores encontrados:")
        for archivo, error in errores:
            print(f"- No se pudo mover {archivo}: {error}")
        input("Presiona Enter para continuar...")
    else:
        print("Organización completada sin errores.")
        input("Presiona Enter para continuar...")

if __name__ == "__main__":
    carpeta_organizar = CARPETA

    print(f"Organizando archivos en la carpeta: {carpeta_organizar}")

    try:
        organizar_descargas(carpeta_organizar)
    except PermissionError:
        print("Error: No tienes permisos suficientes para organizar esta carpeta.")
        input("Presiona Enter para continuar...")
    except Exception as e:
        print(f"Error inesperado: {e}")
        input("Presiona Enter para continuar...")