
from analizadorLexico import*
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
