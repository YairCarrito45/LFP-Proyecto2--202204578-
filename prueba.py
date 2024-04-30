global lista_errores 
lista_errores = []


def tabla_errores(nombreArchivo, contenidoNuevo):
    try:
        with open(nombreArchivo, 'w') as archivo:
            archivo.write(contenidoNuevo)
        print('Contenido modificado')
    except IOError:
        print(f'Error al abrir el archivo con el nombre {nombreArchivo}')

def errores(tipo, linea, columna, valorEsperado):
    lista_errores.append(tipo)
    lista_errores.append(linea)
    lista_errores.append(columna)
    lista_errores.append(valorEsperado)
    nombre_archivo = "TablaErrores.html"
    print(f'ERROR {tipo.upper()} \n Linea: {linea} | Columna: {columna} | Valor Esperado: {valorEsperado}')

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
    </style>
</head>
<body>
    <div class="centrado">
        <table border="1">
            <caption>Tabla Errores</caption>
            <thead>
                <tr>
                    <th>Tipo</th>
                    <th>Linea</th>
                    <th>Columna</th>
                    <th>Valor esperado</th>
                </tr>
            </thead>
            <tbody>'''
    i = 0
    while i < len(lista_errores):
        contenido_tabla += f'''
                    <tr>
                        <tr>
                            <td>{lista_errores[i]}</td>
                            <td>{lista_errores[i+1]}</td>
                            <td>{lista_errores[i+2]}</td>
                            <td>{lista_errores[i+3]}</td>
                        </tr>
                    </tr>'''
        i += 4
    contenido_tabla += '''
            </tbody>
        </table>
    </div>
</body>
</html>'''
            
    tabla_errores(nombre_archivo, contenido_tabla)

# Llamada a la función errores
errores("sintactico", 700, 57, "///")
errores("lexxx", 12, 5000, "///")
errores("sintacticooooo", 36, 75, "///")
errores("sintactico", 50, 65, "///")
errores("lexxxtico", 500, 555, "///")
