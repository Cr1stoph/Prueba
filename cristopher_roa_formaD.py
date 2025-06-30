#Comprar entrada a “los Fortificados” en Concepción.
#Comprar entrada a “los Fortificados” en Puente Alto.
#Comprar entrada a “los Fortificados” en Muelle Barón en Valparaíso.
#Comprar entrada a “los Fortificados” en Muelle Vergara en Viña del Mar.
#Salir
data = {
    'comprador':[
        {
            'nombre': 'Juan',
            'codigo' : '12SD34'
        }
    ]
}
def validar_numero_entero_positivo(mensaje_input:str):
    while True:
        try:
            numero = int(input(mensaje_input))
            if numero <= 0:
                print('✖️ERROR✖️ El numero ingresado debe ser mayor a 0')
                continue
        except ValueError:
            print('✖️ERROR✖️ El numero ingresado debe ser entero')
            continue
        return numero

def validar_texto_codigo(codigo:str):
    letra = 'abcdefghijklmnñopqrstuvxyz'
    for i in codigo:
        for j in letra:
            if i == j:
                return True
    return False
def validar_numero_codigo(codigo:str):
    numeros = '1234567890'
    for i in codigo:
        for j in numeros:
            if i == j:
                return True
    return False
def longitud_codigo(codigo:str):
    codigo = codigo.upper()
    if len(codigo) >= 6:
        return True
    else:
        return False
def codigo_unico(codigo):
    """Valida codigo unico"""
    for i in data['comprador']:
        if i['codigo'] == codigo:
            return True #existe
    return False

def nombre_unico(nombre:str):
    """valida nombre unico"""
    for i in data['comprador']:
        if i['nombre'] == nombre:
            return True #existe
    return False #no existe

def comprar_entrada_concepcion():

    while True:
        stock = 500
        nombre = input('Ingresa el nombre del comprador').capitalize()
        nombre_unico(nombre)
        if nombre_unico(nombre) == True:
            print('El nombre no se debe repetir')
            continue
        codigo = input('Ingrese el codigo verificador').replace(' ','')
        longitud_codigo(codigo)
        if longitud_codigo(codigo) == False:
            print('El codigo debe tener 6 caracteres')
            continue
        validar_numero_codigo(codigo)
        if validar_numero_codigo == False:
            print('El codigo debe tener almenos 1 numero')
            continue
        validar_texto_codigo(codigo)
        if validar_texto_codigo(codigo) == False:
            print('El codigo debe tener al menos 1 letra')
            continue
        if codigo_unico(codigo) == True:
            print('El codigo no se puede repetir')
            continue
        stock -= 1
        compra_exitosa = {
            'nombre':nombre,
            'codigo': codigo
        }
        data['comprador'].append(compra_exitosa)
        
        print('--Compra en Concepción---')
        print(f'Nombre de comprador: {nombre}\nCodigo de confirmación: {codigo}')
        print(f'Stock : {stock}')
        break

def compra_entrada_puentealto():
    stock = 1300
    while True:
        nombre = input('Ingrese el nombre del comprador').capitalize()
        nombre_unico(nombre)
        if nombre_unico(nombre) == True:
            print('El nombre del comprador no se puede repetir')
            continue
        cantidad = validar_numero_entero_positivo('Ingresa la cantidad de entradas a comprar')
        if cantidad > 3:
            print('La cantidad maxima de entradas es de 3 por persona')
            continue
        stock -= cantidad
        compra_exitosa = {
            'nombre':nombre,
            'cantidad': cantidad
        }
        data['comprador'].append(compra_exitosa)
        print('--Compra en Puente Alto---')
        print(f'Nombre de comprador: {nombre}\nCantidad: {cantidad}')
        print(f'Stock: {stock}')
        break

def compra_entrada_valparaiso():
    stock = 100
    while True:
        nombre = input('ingresa el nombre del comprador').capitalize()
        nombre_unico(nombre)
        if nombre_unico(nombre) == True:
            print('El nombre del comprador no se puede repetir')
            continue
        codigo = input('Ingrese el codigo verificador').replace(' ','')
        longitud_codigo(codigo)
        if longitud_codigo(codigo) == False:
            print('El codigo debe tener 6 caracteres')
            continue
        validar_numero_codigo(codigo)
        if validar_numero_codigo == False:
            print('El codigo debe tener almenos 1 numero')
            continue
        validar_texto_codigo(codigo)
        if validar_texto_codigo(codigo) == False:
            print('El codigo debe tener al menos 1 letra')
            continue
        entrada = 'G'
        stock -= 1
        compra_exitosa = {
            'nombre': nombre,
            'codigo': codigo,
            'entrada':entrada
        }
        print('--Compra en Muelle Baron, Valparaiso--')
        print(f'Nombre del comprador: {nombre}\nTipo de entrada asignada: {entrada}')
        data['comprador'].append(compra_exitosa)
        print(f'Stock: {stock}')
        break

def tipo_entrada(tipo_de_entrada:str):
    if tipo_de_entrada == 'Sun' or tipo_de_entrada == 'Ni':
        return True
    else:
        return False
    
def compra_entrada_vina():
    stock = 50
    while True:
        nombre = input('ingresa el nombre del comprador\n').capitalize()
        nombre_unico(nombre)
        if nombre_unico(nombre) == True:
            print('El nombre del comprador no se puede repetir')
            continue
        tipo_de_entrada = input('ingresa el tipo de entrada Sun - Ni').capitalize()
        tipo_entrada(tipo_de_entrada)
        if tipo_entrada(tipo_de_entrada) == False:
            print('El tipo de entrada solo debe ser Sun o Ni')
            continue
        stock -= 1
        compra_exitosa = {
            'nombre': nombre,
            'tipo_de_entrada' : tipo_de_entrada
        }
        data['comprador'].append(compra_exitosa)
        print('--Compra en Muelle Vergara, Viña del Mar---')
        print(f'Nombre de comprador: {nombre}\nTipo de entrada: {tipo_de_entrada}')
        print(f'STOCK: {stock}')
        break

def menu():
    while True:
        print('TOTEM AUTOSERVICIO GIRA LOS FORTIFICADOS ROCK AND CHILE IN CHILE')
        print('[1] - Compra entradas en Concepción')
        print('[2] - Compra entradas en Puente Alto')
        print('[3] - Compra entradas en Muelle Barón, Valparaíso')
        print('[4] - Compra entradas en Muelle Vergara, Viña del Mar')
        print('[5] - Salir')
        opc = validar_numero_entero_positivo('Seleccione una opcion del 1 al 5')
        if opc == 1:
            comprar_entrada_concepcion()
        elif opc == 2:
            compra_entrada_puentealto()
        elif opc == 3:
            compra_entrada_valparaiso()
        elif opc == 4:
            compra_entrada_vina()
        elif opc == 5:
            print('Gracias por comprar en FORTIFICADOS.APK')
            break 
menu()