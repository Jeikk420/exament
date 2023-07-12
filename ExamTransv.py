#ExamTransversal
entradas_platino = [None] * 20
entradas_oro = [None] * 30
entradas_plata = [None] * 50
asistentes = []
precios = {'Platino': 120000, 'Oro': 80000, 'Plata': 50000}
total_entradas_vendidas = 0
total_ganancias = 0
print("Bienvenido a Creativos.cl")
def comprar_entradas():
    global total_entradas_vendidas, total_ganancias

    cantidad = int(input("Ingrese la cantidad de entradas a comprar (1-3): "))
    while cantidad < 1 or cantidad > 3:
        cantidad = int(input("Cantidad inválida. Ingrese la cantidad de entradas a comprar (1-3): "))

    for i in range(cantidad):
        print("\nUbicaciones disponibles:")
        mostrar_ubicaciones_disponibles()

        ubicacion = int(input("Seleccione la ubicación deseada: "))
        while not validar_ubicacion(ubicacion):
            print("Ubicación no disponible. Intente nuevamente.")
            ubicacion = int(input("Seleccione la ubicación deseada: "))

        tipo_entrada = obtener_tipo_entrada(ubicacion)
        precio_entrada = precios[tipo_entrada]

        run = input("Ingrese el RUN (Sin guiones-puntos o digito verificador): ")
        while not validar_run(run):
            print("RUN inválido. Intente nuevamente recuerde que es sin digito verificador.")
            run = input("Ingrese el RUN (Sin guiones-puntos o digito verificador): ")

     
        if tipo_entrada == 'Platino':
            entradas_platino[ubicacion - 1] = run
        elif tipo_entrada == 'Oro':
            entradas_oro[ubicacion - 21] = run
        else:
            entradas_plata[ubicacion - 51] = run

        asistentes.append({'RUN': run, 'Tipo': tipo_entrada, 'Precio': precio_entrada})
        total_entradas_vendidas += 1
        total_ganancias += precio_entrada

    print("Operación realizada correctamente.")

def mostrar_ubicaciones_disponibles():
    print("Platino:")
    for i, asistente in enumerate(entradas_platino):
        if asistente is None:
            print(f"{i + 1}: Disponible")
        else:
            print(f"{i + 1}: Vendido")

    print("\nOro:")
    for i, asistente in enumerate(entradas_oro):
        if asistente is None:
            print(f"{i + 21}: Disponible")
        else:
            print(f"{i + 21}: Vendido")

    print("\nPlata:")
    for i, asistente in enumerate(entradas_plata):
        if asistente is None:
            print(f"{i + 51}: Disponible")
        else:
            print(f"{i + 51}: Vendido")

def validar_ubicacion(ubicacion):
    tipo_entrada = obtener_tipo_entrada(ubicacion)

    if tipo_entrada == 'Platino':
        return entradas_platino[ubicacion - 1] is None
    elif tipo_entrada == 'Oro':
        return entradas_oro[ubicacion - 21] is None
    else:
        return entradas_plata[ubicacion - 51] is None

def obtener_tipo_entrada(ubicacion):
    if ubicacion >= 1 and ubicacion <= 20:
        return 'Platino'
    elif ubicacion >= 21 and ubicacion <= 50:
        return 'Oro'
    else:
        return 'Plata'

def validar_run(run):
    return run.isdigit() and len(run) == 8

def mostrar_listado_asistentes():
    print("\nListado de asistentes:")
    asistentes_ordenados = sorted(asistentes, key=lambda x: x['RUN'])
    for asistente in asistentes_ordenados:
        print(f"RUN: {asistente['RUN']}, Tipo: {asistente['Tipo']}, Precio: {asistente['Precio']}")

def mostrar_ganancias_totales():
    print("\nResumen de ganancias:")
    for tipo_entrada, precio in precios.items():
        cantidad = sum(1 for asistente in asistentes if asistente['Tipo'] == tipo_entrada)
        total_tipo_entrada = cantidad * precio
        print(f"{tipo_entrada}: ${precio} - {cantidad} - ${total_tipo_entrada}")

    print(f"\nTOTAL {total_entradas_vendidas} ${total_ganancias}")


while True:
    print("\n--- Menú ---")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        comprar_entradas()
    elif opcion == "2":
        mostrar_ubicaciones_disponibles()
    elif opcion == "3":
        mostrar_listado_asistentes()
    elif opcion == "4":
        mostrar_ganancias_totales()
    elif opcion == "5":
        print("\nSaliendo del sistema.")
        print("\nHasta luego.")
        print("\nProgramador--> Jeicov Diaz Astorga.")
        print("\nFecha---> 12-07-2023.")
        break
    else:
        print("Opción no válida. Intente nuevamente por favor.")
