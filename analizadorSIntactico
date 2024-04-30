
import string
from Token import Tokens
from Error import Errores
from Lexema import *


def analizador_sintactico(cadena):
    global entrada
    global n_linea
    global n_columna
    global puntero
    entrada = cadena
    instrucciones = []
    tokens = []
    n_linea = 1
    n_columna = 0
    puntero = 0
    continuar = True
    nombre = ''
    salida = ''
    while continuar:
        continuar, tipo, lexema = leer_lexema()
        #print(f'{tipo}: {lexema}')
        if continuar:
            if lexema == 'CrearBD':
                tokens.append(Tokens("CrearBD", n_linea, n_columna))
                continuar, tipo, lexema = leer_lexema()
                if tipo == 'ID':
                    nombre = lexema
                    if continuar:
                        continuar, tipo, lexema = leer_lexema()
                        if lexema == '=':
                            if continuar:
                                continuar, tipo, lexema = leer_lexema()
                                if lexema == 'nueva':
                                    tokens.append(Tokens("nueva", n_linea, n_columna))
                                    if continuar:
                                        continuar, tipo, lexema = leer_lexema()
                                        if lexema == 'CrearBD':
                                            tokens.append(Tokens("CrearBD", n_linea, n_columna))
                                            if continuar:
                                                continuar, tipo, lexema = leer_lexema()
                                                if tipo == 'CERO PARAMETROS':
                                                    print(f"use('{nombre}');")
                                                    instrucciones.append(f"use('{nombre}');")
            if lexema == 'EliminarBD':
                tokens.append(Tokens("EliminarBD", n_linea, n_columna))
                continuar, tipo, lexema = leer_lexema()
                if tipo == 'ID':
                    nombre = lexema
                    if continuar:
                        continuar, tipo, lexema = leer_lexema()
                        if lexema == '=':
                            if continuar:
                                continuar, tipo, lexema = leer_lexema()
                                if lexema == 'nueva':
                                    tokens.append(Tokens("nueva", n_linea, n_columna))
                                    if continuar:
                                        continuar, tipo, lexema = leer_lexema()
                                        if lexema == 'EliminarBD':
                                            tokens.append(Tokens("EliminarBD", n_linea, n_columna))
                                            if continuar:
                                                continuar, tipo, lexema = leer_lexema()
                                                if tipo == 'CERO PARAMETROS':
                                                    print(f'db.dropDatabase()')
                                                    instrucciones.append(f'db.dropDatabase()')
            if lexema == 'CrearColeccion':
                tokens.append(Tokens("CrearColeccion", n_linea, n_columna))
                continuar, tipo, lexema = leer_lexema()
                if tipo == 'ID':
                    nombre = lexema
                    if continuar:
                        continuar, tipo, lexema = leer_lexema()
                        if lexema == '=':
                            if continuar:
                                continuar, tipo, lexema = leer_lexema()
                                if lexema == 'nueva':
                                    tokens.append(Tokens("nueva", n_linea, n_columna))
                                    if continuar:
                                        continuar, tipo, lexema = leer_lexema()
                                        if lexema == 'CrearColeccion':
                                            tokens.append(Tokens("CrearColeccion", n_linea, n_columna))
                                            if continuar:
                                                continuar, tipo, lexema = leer_lexema()
                                                print('PRUEBA   ', tipo, lexema)
                                                if tipo == 'NOMBRE':
                                                    print(f'db.createCollection({lexema})')
                                                    instrucciones.append(f'db.createCollection({lexema})')
            if lexema == 'EliminarColeccion':
                tokens.append(Tokens("EliminarColeccion", n_linea, n_columna))
                continuar, tipo, lexema = leer_lexema()
                if tipo == 'ID':
                    nombre = lexema
                    if continuar:
                        continuar, tipo, lexema = leer_lexema()
                        if lexema == '=':
                            if continuar:
                                continuar, tipo, lexema = leer_lexema()
                                if lexema == 'nueva':
                                    tokens.append(Tokens("nueva", n_linea, n_columna))
                                    if continuar:
                                        continuar, tipo, lexema = leer_lexema()
                                        if lexema == 'EliminarColeccion':
                                            tokens.append(Tokens("EliminarColeccion", n_linea, n_columna))
                                            if continuar:
                                                continuar, tipo, lexema = leer_lexema()
                                                if tipo == 'NOMBRE':
                                                    print(f'db.{lexema}.drop()')
                                                    instrucciones.append(f'db.{lexema}.drop()')
            if lexema == 'InsertarUnico':
                tokens.append(Tokens("InsertarUnico", n_linea, n_columna))
                continuar, tipo, lexema = leer_lexema()
                if tipo == 'ID':
                    nombre = lexema
                    if continuar:
                        continuar, tipo, lexema = leer_lexema()
                        if lexema == '=':
                            if continuar:
                                continuar, tipo, lexema = leer_lexema()
                                if lexema == 'nueva':
                                    tokens.append(Tokens("EliminarColeccion", n_linea, n_columna))
                                    if continuar:
                                        continuar, tipo, lexema = leer_lexema()
                                        if lexema == 'InsertarUnico':
                                            tokens.append(Tokens("InsertarUnico", n_linea, n_columna))
                                            if continuar:
                                                continuar, tipo, lexema = leer_lexema()
                                                print("TIPO DE RETORNO InsertarUnico ---- ",tipo)
                                                if tipo == 'PARAMETRO':
                                                    print(f'db.{lexema[0]}.insertOne({lexema[1]})')
                                                    instrucciones.append(f'db.{lexema[0]}.insertOne({lexema[1]})')
            if lexema == 'ActualizarUnico':
                tokens.append(Tokens("ActualizarUnico", n_linea, n_columna))
                continuar, tipo, lexema = leer_lexema()
                if tipo == 'ID':
                    nombre = lexema
                    if continuar:
                        continuar, tipo, lexema = leer_lexema()
                        if lexema == '=':
                            if continuar:
                                continuar, tipo, lexema = leer_lexema()
                                if lexema == 'nueva':
                                    tokens.append(Tokens("nueva", n_linea, n_columna))
                                    if continuar:
                                        continuar, tipo, lexema = leer_lexema()
                                        if lexema == 'ActualizarUnico':
                                            tokens.append(Tokens("ActualizarUnico", n_linea, n_columna))
                                            if continuar:
                                                continuar, tipo, lexema = leer_lexema()
                                                print("TIPO DE RETORNO ActualizarUnico ---- ",tipo)
                                                if tipo == 'PARAMETRO':
                                                    print(f'db.{lexema[0]}.updateOne({lexema[1]})')
                                                    instrucciones.append(f'db.{lexema[0]}.updateOne({lexema[1]})')
            if lexema == 'EliminarUnico':
                tokens.append(Tokens("EliminarUnico", n_linea, n_columna))
                continuar, tipo, lexema = leer_lexema()
                if tipo == 'ID':
                    nombre = lexema
                    if continuar:
                        continuar, tipo, lexema = leer_lexema()
                        if lexema == '=':
                            if continuar:
                                continuar, tipo, lexema = leer_lexema()
                                if lexema == 'nueva':
                                    tokens.append(Tokens("nueva", n_linea, n_columna))
                                    if continuar:
                                        continuar, tipo, lexema = leer_lexema()
                                        if lexema == 'EliminarUnico':
                                            tokens.append(Tokens("EliminarUnico", n_linea, n_columna))
                                            if continuar:
                                                continuar, tipo, lexema = leer_lexema()
                                                if tipo != 'CERO PARAMETROS':
                                                    print(f'db.{lexema[0]}.deleteOne({lexema[1]})')
                                                    instrucciones.append(f'db.{lexema[0]}.deleteOne({lexema[1]})')
            if lexema == 'BuscarTodo':
                tokens.append(Tokens("BuscarTodo", n_linea, n_columna))
                continuar, tipo, lexema = leer_lexema()
                if tipo == 'ID':
                    nombre = lexema
                    if continuar:
                        continuar, tipo, lexema = leer_lexema()
                        if lexema == '=':
                            if continuar:
                                continuar, tipo, lexema = leer_lexema()
                                if lexema == 'nueva':
                                    tokens.append(Tokens("nueva", n_linea, n_columna))
                                    if continuar:
                                        continuar, tipo, lexema = leer_lexema()
                                        if lexema == 'BuscarTodo':
                                            tokens.append(Tokens("BuscarTodo", n_linea, n_columna))
                                            if continuar:
                                                continuar, tipo, lexema = leer_lexema()
                                                if tipo != 'CERO PARAMETROS':
                                                    print(f'db.{nombre}.find()')
                                                    instrucciones.append(f'db.{nombre}.find()')
            if lexema == 'BuscarUnico':
                tokens.append(Tokens("BuscarUnico", n_linea, n_columna))
                continuar, tipo, lexema = leer_lexema()
                if tipo == 'ID':
                    nombre = lexema
                    if continuar:
                        continuar, tipo, lexema = leer_lexema()
                        if lexema == '=':
                            if continuar:
                                continuar, tipo, lexema = leer_lexema()
                                if lexema == 'nueva':
                                    tokens.append(Tokens("nueva", n_linea, n_columna))
                                    if continuar:
                                        continuar, tipo, lexema = leer_lexema()
                                        if lexema == 'BuscarUnico':
                                            tokens.append(Tokens("BuscarUnico", n_linea, n_columna))
                                            if continuar:
                                                continuar, tipo, lexema = leer_lexema()
                                                if tipo != 'CERO PARAMETROS':
                                                    print(f'db.{nombre}.findOne()')
                                                    instrucciones.append(f"db.{nombre}.findOne()")
    contenidoNew(tokens, "tokens")
    
    return instrucciones


entrada = '''
    /* 
        ARCHIVO DE PRUEBAS 
        CON COMENTARIOS
    */


    --- CREAR BASE DE DATOS
    CrearBD temp1 = nueva CrearBD();

    --- ELIMINAR BASE DE DATOS
    EliminarBD Ramirez = nueva EliminarBD();

    /* 
        BASE DE DATOS DE  LITERATURAS
    */

    --- CREAR BASE DE DATOS
    CrearBD Pame = nueva CrearBD();

    --- CREAR COLECCION DE LITERATURAS
    CrearColeccion colec = nueva CrearColeccion(“literaturas”);

    --- CREAR COLECCION TEMPORAL
    CrearColeccion Pameeee = nueva CrearColeccion(“colectemp”);

    --- ELIMINAR COLECCION TEMPORAL
    EliminarColeccion eliminacolec = nueva EliminarColeccion(“colectemp”);

    /* 
        INSERTAR DATOS
    */
    InsertarUnico insert1 = nueva InsertarUnico(“literaturas” ,
    “
        {
            "nombre" : "Obra Literaria",
            "autor" : "Jorge Luis"
        }
    ”);

    InsertarUnico insert2 = nueva InsertarUnico(“literaturas” ,
    “
        {
            "nombre" : "El Principito",
            "autor" : "Antoine de Saint"
        }
    ”);

    InsertarUnico insert3 = nueva InsertarUnico(“literaturas” ,
    “
        {
            "nombre" : "Moldavita. Un Visitante Amigable",
            "autor" : "Norma Munioz Ledo"
        }
    ”);

    ---- ACTUALIZAR DATO DE COLECCION LITERATURA
    ActualizarUnico actualizadoc = nueva ActualizarUnico(“literaturas”,
    “
        {
            "nombre" : "Obra Literaria"
        },
        {
            $set: {"autor" : "Mario Vargas"}
        }
    ”);

    --- ELIMINAR DATO DE LA COLECCION LITERATURA
    EliminarUnico eliminadoc = nueva EliminarUnico(“literaturas”,
    “
        {
            "nombre" : "Obra Literaria"
        }
    ”);

    --- BUSCAR TODOS LOS DATOS DE LA COLECCION
    BuscarTodo todo = nueva BuscarTodo(“literaturas”);

    --- BUSCAR UN DATO POR COLECCION
    BuscarUnico todo = nueva BuscarUnico(“literaturas”);
'''
#instruccion()
#analizador_sintactico()