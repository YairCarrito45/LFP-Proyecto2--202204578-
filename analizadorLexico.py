import string
from Token import Tokens
from Error import Errores

inst = ['CrearBD', 'EliminarBD', 'CrearColeccion', 'EliminarColeccion',
    'InsertarUnico', 'ActualizarUnico', 'EliminarUnico', 'BuscarTodo', 'BuscarUnico', 'nueva']

global n_linea
global n_columna
global instrucciones
global lista_lexemas
global lista_errores
global cadena
global ultima_posicion
global letras_digitos
global digitos
global letras


n_linea = 1
n_columna = 0
puntero = 0

lista_lexemas = []
instrucciones = []
lista_errores = []
letras_digitos = []
digitos = []
letras = []
letras_digitos += list(string.ascii_letters)
letras_digitos += list(string.digits)
letras_digitos += ['_']
digitos += list(string.digits)
letras += list(string.ascii_letters)


def modificar_archivo(nombreArchivo, contenidoNuevo):
    try:
        with open(nombreArchivo, 'w') as archivo:
            archivo.write(contenidoNuevo)
        print('Contenido modificado')
    except IOError:
        print(f'Error al abrir el archivo con el nombre {nombreArchivo}')

def contenidoNew(tokens, tipo):
        titulo = ''
        if tipo == "tokens":
            nombre_archivo = "TablaTokens.html"
            titulo = "Tabla Tokens"
        else: 
            nombre_archivo = "TablaErrores.html"
            titulo = "Tabla Errpres"
        contenido_tabla = '''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Tabla Errores</title>
            <style>
                .centrado {
                    margin: 0 auto;
                    width: 50%; 
                }
            </style>'''
        contenido_tabla += f'''</head>
        <body>
        <div class="centrado">
            <table border="1">
                <caption>{titulo}</caption>
                <thead>
                    <tr>
                        <th>Token</th>
                        <th>Linea</th>
                        <th>Columna</th>
                    </tr>
                </thead>
                <tbody>'''
        for token in tokens:
            contenido_tabla += f'''
                        <tr>
                            <td>{token.token}</td>
                            <td>{token.linea}</td>
                            <td>{token.columna}</td>
                        </tr>'''
        contenido_tabla += '''
                    </tbody>
                </table>
            </div>
        </body>
        </html>'''
        modificar_archivo(nombre_archivo, contenido_tabla)


def leer_siguiente():
    global n_linea
    global n_columna
    global puntero
    char = entrada[puntero]
    # print(char)
    puntero += 1
    if puntero < ultima_posicion:
        resultado = True
    else:
        resultado = False
    if char == '\n':
        n_linea += 1
        n_columna = 0
    else:
        n_columna += 1
    return resultado, char

def instruccion():
    global entrada
    global ultima_posicion
    ultima_posicion = len(entrada)
    #print(letras_digitos)
    continuar = True
    inicio_lexema = False
    #while cadena:
    while continuar:
        continuar, char = leer_siguiente()
        # PUNTO DE INGRESO DE UN COMENTARIO
        if char == '/':
            print("inicio comentario")
            continuar = leer_comentario()
        # PUNTO DE INGRESO DE UN COMENTARIO DE UNA SOLA LÍNEA
        elif char == '-':
            continuar = leer_comentario_en_linea()
        # PUNTO DE INGRESO DE PALABRAS RESERVADAS
        elif char in letras:
            continuar = leer_funcion(continuar, char)

def leer_identificador(continuar, char):
    global puntero
    identificador = ''
    identificador += char
    if continuar:
        continuar, char = leer_siguiente()
        while continuar:
            if char == '"':
                continuar, char = leer_siguiente()
                if char in letras_digitos:
                    identificador += char
                    continuar, char = leer_siguiente()
                    if char == '"':
                        continuar, char = leer_siguiente()
                        if char == ')':
                            continuar, char = leer_siguiente()
                            if char == ';':
                                continuar = False
            if char == ')':
                continuar, char = leer_siguiente()
                if char == ';':
                    continuar = False
    #print(f"IDENTIFICADOR {identificador}")

def leer_parametros(continuar, char):
    lexema = ''
    tipo = 'DESCONOCIDO'
    salir = False
    if continuar:
        continuar, char = leer_siguiente()
        if char == ')':
            if continuar:
                continuar, char = leer_siguiente()
                if char == ';':
                    tipo = 'CERO PARAMETROS'
                    lexema = '();'
        else:
            #print(f'ASCII: {ord(char)}')
            ascii_char = ord(char)
            if ascii_char == 8220 or ascii_char == 34:
                if continuar:
                    nombre = ""
                    while not salir and continuar:
                        continuar, char = leer_siguiente()
                        #print(char)
                        ascii_char = ord(char)
                        #print(f'ASCII: {char} ---- {ascii_char}')
                        if ascii_char == 8221 or ascii_char == 34:   #   " ahdkjhafdkf  ");   
                            if continuar:
                                continuar, char = leer_siguiente()
                                #print(f'ASCII: {ord(char)}')
                                if char == ')':
                                    if continuar:
                                        continuar, char = leer_siguiente()
                                        #print(char)
                                        if char == ';':
                                            tipo = 'NOMBRE'
                                            print("NOMBRE: -------- ",nombre)
                                            lexema = nombre
                                        else:
                                            tipo = 'DESCONOCIDO'
                                            lexema = ''
                                        #print(f'ASCII: {ord(char)} --- {tipo} ---- {lexema}')
                                        salir = True
                                elif char == ',':   # " ,  
                                    if continuar:
                                        continuar, char = leer_siguiente()
                                        #print(f'ASCII: {ord(char)}')
                                        ascii_char = ord(char)
                                        if ascii_char == 8220:  # " ,   "
                                            if continuar:
                                                parametro = ""
                                                while not salir and continuar:
                                                    continuar, char = leer_siguiente()
                                                    #print(char)
                                                    ascii_char = ord(char)
                                                    #print(f'ASCII: {char} ---- {ascii_char}')
                                                    if ascii_char == 8221:  # " ,   ""
                                                        if continuar:
                                                            continuar, char = leer_siguiente()
                                                            #print(f'ASCII: {ord(char)}')
                                                            if char == ')':
                                                                if continuar:
                                                                    continuar, char = leer_siguiente()
                                                                    #print(char)
                                                                    if char == ';':
                                                                        tipo = 'PARAMETRO'
                                                                        print("NOMBRE----",nombre,"----PARAMETRO----",parametro)
                                                                        lexema = [nombre, parametro]
                                                                    else:
                                                                        tipo = 'DESCONOCIDO'
                                                                        lexema = ''
                                                                    #print(f'ASCII: {ord(char)} --- {tipo} ---- {lexema}')
                                                                    salir = True
                                                            else:
                                                                tipo = 'DESCONOCIDO'
                                                                lexema = ''
                                                                salir = True
                                                    else:
                                                        parametro += char
                                else:
                                    tipo = 'DESCONOCIDO'
                                    lexema = ''
                                    salir = True
                        else:
                            nombre += char
    return continuar, tipo, lexema

def leer_funcion(continuar, char):
    global puntero
    global inst
    l = ''
    lexema = ''
    lexema += char
    if continuar:
        continuar, char = leer_siguiente()
        while continuar:
            if char in letras_digitos:
                lexema += char
                continuar, char = leer_siguiente()
            else:
                continuar = False
                puntero -= 1
        resultado =  True
    else:
        resultado = False
    if lexema in inst:
        #print(f'Palabra reservada: {lexema}')
        return resultado, 'PR', lexema
    else: 
        #print(f'Identificador: {lexema}')
        return resultado, 'ID', lexema

def leer_comentario_en_linea():
    errores = []
    continuar, char = leer_siguiente()
    if char == '-':
        if continuar:
            continuar, char = leer_siguiente()
            if char == '-':
                while continuar:
                    continuar, char = leer_siguiente()
                    if char == '\n':
                        #print(f'comentario en linea leido en columna {n_columna} y fila {n_linea}')
                        return True
            else:
                errores.append(Errores(char, n_linea, n_columna))
    else:
        errores.append(Errores(char, n_linea, n_columna))
    contenidoNew(errores, errores)
    return False

def leer_comentario():
    continuar, char = leer_siguiente()
    if char == '*':
        #inicio de comentario
        while continuar:
            continuar, char = leer_siguiente()
            if char == '*':
                if continuar:
                    continuar, char = leer_siguiente()
                    if char == '/':
                        #no se almacena el comentario
                        #print(f'comentario leido en columna {n_columna} y fila {n_linea}')
                        return True
    return False

def leer_lexema():
    global entrada
    global ultima_posicion
    ultima_posicion = len(entrada)
    #print(letras_digitos)
    continuar = True
    salir = False
    inicio_lexema = False
    tipo = 'ND'
    lexema = ''
    while not salir and continuar:
        continuar, char = leer_siguiente()
        # PUNTO DE INGRESO DE UN COMENTARIO
        #print("continuar ------" ,continuar, "   char --------" ,char)
        if char == '/':
            #print("inicio comentario")
            continuar = leer_comentario()
        # PUNTO DE INGRESO DE UN COMENTARIO DE UNA SOLA LÍNEA
        elif char == '-':
            continuar = leer_comentario_en_linea()
        # PUNTO DE INGRESO DE PALABRAS RESERVADAS
        elif char in letras:
            continuar, tipo, lexema = leer_funcion(continuar, char)
            salir = True
        elif char == '=':
            lexema = char
            tipo = 'IGUAL'
            salir = True
        elif char == '(':
            
            continuar, tipo, lexema = leer_parametros(continuar, char)
            
            if tipo == 'CERO PARAMETROS':
                salir = True
            elif tipo == 'NOMBRE':
                salir = True
            elif tipo == 'PARAMETRO':
                salir = True
        # PUNTO DE INGRESO DE UN IDENTIFICADOR
    #print(f'LISTA ERRORES ---- {lista_errores}')
    #print(f'{tipo}: {lexema}')
    print("Imprimiento TIPOOOO LEER LEXEMA: ", tipo)
    return continuar, tipo, lexema

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