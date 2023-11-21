import os
import pandas as pd
import numpy as np
import sqlalchemy

def convertirxlacsv(ruta): # Esta funcion convierte todos los archivos .xl a .csv dando como input la ruta de acceso a la carpeta
    def pasaracsv(lista_entrada,lista_salida):
        file = pd.DataFrame(pd.read_excel(ruta+lista_entrada))
        file.to_csv(ruta+lista_salida+'.csv',index=False)
    
    lista = os.listdir(ruta)
    lista_salida = []
    lista_entrada = []
    lista_intermedia = []

    for i in lista:
        lista_intermedia.append(i.split('.')[0])

    for i in range(len(lista)):
        if not '.xl' in lista[i]:
            continue
        if lista_intermedia.count(lista_intermedia[i]) > 1:
            continue
        x = lista[i]
        lista_entrada.append(lista[i])
        lista_salida.append(x.split('.')[0])

    for i in range(len(lista_entrada)):
        pasaracsv(lista_entrada[i],lista_salida[i])

def obtenernombrescsv(ruta): #obtiene los nombres de los arhivos .csv
    lista = os.listdir(ruta)
    for i in lista:
        if not '.csv' in i:
            lista.remove(i)
    return lista

def pasaradf(lista,ruta): # pasa todos los .csvs a dataframes
    nombres = [i.split('.')[0] for i in lista]
    dfs = [i.split('.')[0] for i in lista]
    for i in range(len(nombres)):
        try:
            dfs[i] = (pd.read_csv(ruta+lista[i]))
        except:
            dfs[i] = (pd.read_csv(ruta+lista[i],sep=';',decimal=',',thousands='.'))
        if dfs[i].shape[1] == 1:
            dfs[i] = (pd.read_csv(ruta+lista[i],sep=';',decimal=',',thousands='.'))
    return nombres, dfs

def obtenercolumnas(dataframes): # obtiene los nombres y tipos de las columnas de cada dataframe en dos listas de listas
    namecol = [i.columns.to_list() for i in dataframes]
    return namecol

def creardb(con,nombre,eliminar): # crea la base de datos en mysql
    if eliminar:
        con.execute(f'DROP DATABASE IF EXISTS {nombre};')
        con.execute(f'CREATE DATABASE {nombre};')
    con.execute(f'USE {nombre}')

def insertardatos(con,nomtab,df,accion): # exporta los datos de un dataframe
    df.to_sql(con=con,if_exists=accion,name=nomtab,index=False)

def primarykey(con,tabla,primary_key): # vuelve a indicar las primary keys como la primer columna
    con.execute(f'ALTER TABLE {tabla} ADD PRIMARY KEY ({primary_key});')

def foreignkeys(con,nomtablas,nombrecol): # relaciona las foreign keys
    combinaciones = []
    dic = dict(zip(nomtablas,nombrecol))
    for i in dic: # en este for generas un listado de combinaciones en donde i[0][0] es la tabla a generar la combinacion, i[0][1] es la clave origen, i[1][0] es la tabla donde esta la primary y i[1][1] es la clave primaria 
        for j in dic:
            if dic[i] == dic[j]:
                continue
            else:
                for k in dic[j]:
                    if k.lower() == dic[i][0].lower():
                        continue
                    if k.lower() in [z.lower() for z in dic[i]] and 'id' in k[0:2].lower():
                        combinaciones.append([[i,dic[i][[z.lower() for z in dic[i]].index(k.lower())]],[j,k]])
    for i in combinaciones: # aca generas el codigo y ejecutas por sentencia
        if i[1][1] != dic[i[1][0]][0]:
            continue
        string = f'ALTER TABLE {i[0][0].lower()} ADD CONSTRAINT'
        string += f' FOREIGN KEY ({i[0][1]}) REFERENCES {i[1][0].lower()}({i[1][1]})'
        string += ';'
        con.execute(string)

def ejecutar(nombre,ruta,my_con,eliminar=True,accion='replace'):
    archivos = obtenernombrescsv(ruta) #ejecuta la funcion
    nombretablas, dfs = pasaradf(archivos,ruta) # ejecuta la funcion
    nombre_columnas = obtenercolumnas(dfs) # ejecuta la funcion
    creardb(my_con,nombre,eliminar) # ejecuta la creacion de la base de datos
    consqla = sqlalchemy.create_engine(f'mysql+pymysql://root:root1234@localhost:3306/{nombre}') #genera conexion para exportar dataframes
    
    for i in range(len(nombretablas)): # ejecuta la exportacion de datos para todos los dataframes
        insertardatos(consqla,nombretablas[i].lower(),dfs[i],accion)
    
    for i in range(len(nombretablas)): # ejecuta la funcion anterior para todas las tabla
        if list(dfs[i][nombre_columnas[i][0]][dfs[i][nombre_columnas[i][0]].duplicated()].values) == []:
            primarykey(my_con,nombretablas[i],nombre_columnas[i][0])
        else: # si la primer columna tiene valores repetidos no setea como primary key y devuelve un mensaje de error
            print(f'{nombretablas[i]} tiene valores repetidos en la columna {nombre_columnas[i][0]} (primer columna)')
    foreignkeys(my_con,nombretablas,nombre_columnas)
