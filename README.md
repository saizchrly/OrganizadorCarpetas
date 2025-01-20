# OrganizadorCarpetas
Este es un pequeño script en python3 con la intencion de organizar las carpetas segun el tipo de archivo

## Instalación
Para la instalación del repositorio vamos a usar 
```
git clone https://github.com/saizchrly/OrganizadorCarpetas.git
```
O se puede descargar como zip, si has elejido este modo, debes descomprimirlo para poder usarlo

###### Nota
Quiero recordar que se debe de tener instalado python3 para poder ejecutar el script

## Ejecución
Una vez descargado para poder cambiar la carpeta que desea ordenar debe abrir el programa con algun editor de texto, y en la linea 13, donde encuentre las siguientes lineas, 
```
# Cambiar en caso de necesitarlo, poner el nombre de la carpeta
CARPETA = str( Path.home() / "Downloads" )
```
debe sustituir "Downloads" por le nombre de la carpeta que desee.

Si desea modificar la organización de los archivos, en el diccionario, 
```
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
```
puede sistituir el nombre que se encuentra entre "", el cual corresponde al nombre que recibira la carpeta, y para modificar el tipo de archivo que va a esa carpeta debe modificar los datos que se encuentran entre [], siempre recuerde mantener el formarto, el tipo de archivo debe ir entre "" y con el ..