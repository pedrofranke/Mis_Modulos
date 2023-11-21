# Modulos propios

La idea de estos modulos fue crearlos en funcion a mi necesidad, debajo detallare el uso y condiciones de cada uno de ellos:

### Actualizar_tablas.sql

Como dice el titulo, el fin del modulo es actualizar tablas, dando como input el nombre de la tabla a actualizar (tabla1) y el nombre de la tabla que contiene los registros actualizados (tabla2).
Para usar el script se deben modificar las dos primeras lineas y la ultima, dejando en evidencia que base de datos y tablas se desean utilizar.
IMPORTANTE: las tablas deben ser iguales y asi tambien los nombres de sus respectivas columnas.

### Cambiar_Texto_a_Fecha.sql

Se ejecuta en una base de datos y lo que hace es cambiar el tipo de dato a "Date" de todas las columnas que contengan en su nombre la referencia "Fecha" o "Date" incluida.
IMPORTANTE: cambiar la primer linea donde indica el nombre de la base de datos a utilizar.

### Extractor_Traductor.ipynb

Extrae el texto de un archivo .ipynb, lo traduce y genera otro archivo .ipynb.
IMPORTANTE: cambiar el nombre del archivo a extraer: archivo_ipynb, y cambiar el idioma inicial que por defecto es 'ru'.

### Registros_Nulos.sql

Una formula que, modificando las primeras 2 filas de la query, te devuelve todos los registros de la tabla indicada que cuentan con algun valor nulo.

### Insertar_dato_en_campo_Nulo.sql

Ahora usamos esta query para insertar un valor (un valor unico, no variable), en todos aquellos registros vacios detectados anteriormente.

### insertar_registros_nuevos.sql

Cambiando las primeras dos lineas, puedo usar el codigo para actualizar una tabla pero esta vez para que se inserten los registros inexistentes de la tabla 2 en la 1. Seria el complemento de la primera query.

### ListasEnlazadas.py

Archivo con el desarrollo de listas doblemente likeadas, listas linkeadas simples, con multiples funciones de eliminacion, adicion y busqueda sumada la clase nodo para su funcionamiento.

### Probabilidad.py

Funciones basicas de probabilidad como la binomial, hipergeometrica, poisson y la normalizacion, con un detalle explicado de cada input y sus usos frecuentes.

### PySQL.py

Quizas el modulo mas completo, contiene multiples funciones:
    - convertirxlacsv: toma como input una ruta de una carpeta y convierte todos los archivos .xl[...] en archivos .csv
    - obtenernombrescsv: obtiene los nombres de los archivos .csv de una ruta dada
    - pasaradf: genera dataframes de todos los .csv existentes en una ruta
    - creardb: crea una database en mySQL dada una conexion de pymysql, un nombre de base de dato y da la opcion de eliminar la base de datos existente si coincide el nombre o unicamente anexar.
    - primarykey: genera primary keys de las tablas de la conexion dada.
    - foreignkeys: si dos columnas se llaman igual en dos tablas las vincula como foreign keys.
    - <b> ejecutar </b>: ejecuta las funciones anteriores de modo tal que, dado un nombre de base de dato, una ruta a una carpeta que contenga archivos .xl[...] y/o .csv y una conexion a pymysql, genera dicha base de datos con toda la informacion existente en las tablas, incluyendo primary keys (primer columna de cada tabla) y foreign keys (nombres iguales entre columnas de dos tablas).
