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
    # Determinar el nombre del archivo y el título según el tipo
    if tipo == "tokens":
        nombre_archivo = "TablaTokens.html"
        titulo = "Tabla Tokens"
    else: 
        nombre_archivo = "TablaErrores.html"
        titulo = "Tabla Errores"

    # Generar el contenido HTML de la tabla
    contenido_tabla = generar_contenido_html(tokens, titulo)

    # Modificar el archivo con el contenido generado
    modificar_archivo(nombre_archivo, contenido_tabla)

def generar_contenido_html(tokens, titulo):
    # Encabezado del documento HTML
    contenido_tabla = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{titulo}</title>
        <style>
            .centrado {{
                margin: 0 auto;
                width: 50%; 
            }}
        </style>
    </head>
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

    # Agregar filas de datos a la tabla
    for token in tokens:
        contenido_tabla += f'''
            <tr>
                <td>{token.token}</td>
                <td>{token.linea}</td>
                <td>{token.columna}</td>
            </tr>'''

    # Cierre del documento HTML
    contenido_tabla += '''
            </tbody>
        </table>
    </div>
    </body>
    </html>'''

    return contenido_tabla



def leer_siguiente():
    global n_linea, n_columna, puntero
    if puntero >= ultima_posicion:
        return False, ''  # No hay más caracteres para leer

    char = entrada[puntero]
    puntero += 1

    if char == '\n':
        n_linea += 1
        n_columna = 0
    else:
        n_columna += 1

    return True, char  # Se leyó un nuevo caracter


def instruccion():
    global entrada, ultima_posicion
    ultima_posicion = len(entrada)
    continuar = True

    while continuar:
        continuar, char = leer_siguiente()

        if char == '/':  # Punto de ingreso de un comentario
            print("Inicio de comentario")
            continuar = leer_comentario()
        elif char == '-':  # Punto de ingreso de un comentario de una sola línea
            continuar = leer_comentario_en_linea()
        elif char in letras:  # Punto de ingreso de palabras reservadas
            continuar = leer_funcion(continuar, char)


def leer_identificador(continuar, char):
    global puntero
    identificador = char

    while continuar:
        continuar, char = leer_siguiente()
        
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
        elif char == ')':
            continuar, char = leer_siguiente()
            if char == ';':
                continuar = False

    # print(f"IDENTIFICADOR {identificador}")


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
            # Procesamiento para parámetros con nombre
            if char == '"' or ord(char) == 8220 or ord(char) == 34:
                nombre = ''
                while not salir and continuar:
                    continuar, char = leer_siguiente()
                    ascii_char = ord(char)
                    
                    if ascii_char == 8221 or ascii_char == 34:  # Cierre de comillas "
                        if continuar:
                            continuar, char = leer_siguiente()
                            if char == ')':
                                if continuar:
                                    continuar, char = leer_siguiente()
                                    if char == ';':
                                        tipo = 'NOMBRE'
                                        lexema = nombre
                                        salir = True
                                    else:
                                        tipo = 'DESCONOCIDO'
                                        lexema = ''
                                        salir = True
                            elif char == ',':  # Coma para separar parámetros
                                if continuar:
                                    continuar, char = leer_siguiente()
                                    if char == '"' or ord(char) == 8220:  # Inicio de nueva comilla "
                                        parametro = ''
                                        while not salir and continuar:
                                            continuar, char = leer_siguiente()
                                            ascii_char = ord(char)
                                            if ascii_char == 8221:  # Cierre de nueva comilla "
                                                if continuar:
                                                    continuar, char = leer_siguiente()
                                                    if char == ')':
                                                        if continuar:
                                                            continuar, char = leer_siguiente()
                                                            if char == ';':
                                                                tipo = 'PARAMETRO'
                                                                lexema = [nombre, parametro]
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
                        # print(f'Comentario en línea leído en columna {n_columna} y fila {n_linea}')
                        return True
            else:
                errores.append(Errores(char, n_linea, n_columna))
        else:
            errores.append(Errores(char, n_linea, n_columna))
    else:
        errores.append(Errores(char, n_linea, n_columna))

    contenidoNew(errores, 'Errores')
    return False


def leer_comentario():
    continuar, char = leer_siguiente()

    if char == '*':  # Verifica el inicio del comentario
        while continuar:
            continuar, char = leer_siguiente()
            if char == '*':
                if continuar:
                    continuar, char = leer_siguiente()
                    if char == '/':
                        # Comentario completo encontrado, se omite su almacenamiento
                        # print(f'Comentario leído en columna {n_columna} y fila {n_linea}')
                        return True
            elif char == '\n':
                # Incrementa el número de línea al encontrar un salto de línea dentro del comentario
                global n_linea
                n_linea += 1
    return False


def leer_lexema():
    global entrada, ultima_posicion
    ultima_posicion = len(entrada)
    continuar = True
    salir = False
    inicio_lexema = False
    tipo = 'ND'  # Tipo por defecto, 'ND' para "No Definido"
    lexema = ''

    while not salir and continuar:
        continuar, char = leer_siguiente()

        if char == '/':
            continuar = leer_comentario()
        elif char == '-':
            continuar = leer_comentario_en_linea()
        elif char in letras:
            continuar, tipo, lexema = leer_funcion(continuar, char)
            salir = True
        elif char == '=':
            lexema = char
            tipo = 'IGUAL'
            salir = True
        elif char == '(':
            continuar, tipo, lexema = leer_parametros(continuar, char)

            if tipo in ('CERO PARAMETROS', 'NOMBRE', 'PARAMETRO'):
                salir = True

    # print(f'{tipo}: {lexema}')
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