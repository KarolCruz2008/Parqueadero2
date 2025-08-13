import numpy as np

# Matriz 8x5: 8 plantas, 5 plazas por planta
plantas_y_parqueaderos = np.zeros((8, 5), dtype=int)

entrada = ""

while entrada.lower() != "s":
    print("\n--- MENÚ PARQUEADERO ---")
    print("1. Visualización de coches en cada planta")
    print("2. Aparcar")
    print("3. Sacar Coche")
    print("4. Plantas Libres")
    print("5. Planta más Vacía")
    print("6. Total Coches")
    print("7. Mantenimiento Planta")
    print("8. Porcentajes de Ocupación")
    print("9. No Reservadas")
    print("S. Salir")

    entrada = input("Ingrese la opción que desea ejecutar o S para salir: ")

    if entrada.lower() == "s":
        print("Saliendo del programa...")
        break

    # 1. Mostrar Parking
    if entrada == "1":
        for i in range(8):
            ocupadas = list(plantas_y_parqueaderos[i]).count(1)
            print(f"Planta {i+1}: {plantas_y_parqueaderos[i]} - {ocupadas} coches")

    # 2. Aparcar
    elif entrada == "2":
        planta = int(input("Ingrese el número de planta donde desea aparcar (1-8): "))
        if 1 <= planta <= 8:
            if 0 in plantas_y_parqueaderos[planta-1]:
                for i in range(5):
                    if plantas_y_parqueaderos[planta-1, i] == 0:
                        plantas_y_parqueaderos[planta-1, i] = 1
                        print(f"Vehículo aparcado en planta {planta}, plaza {i+1}")
                        break
            else:
                print("Planta ocupada, no hay espacios libres para aparcar")
        else:
            print("Número de planta inválido.")

    # 3. Sacar Coche
    elif entrada == "3":
        planta = int(input("Ingrese el número de planta de donde desea sacar el coche (1-8): "))
        if 1 <= planta <= 8:
            if 1 in plantas_y_parqueaderos[planta-1]:
                for i in range(5):
                    if plantas_y_parqueaderos[planta-1, i] == 1:
                        plantas_y_parqueaderos[planta-1, i] = 0
                        print(f"Coche retirado de planta {planta}, plaza {i+1}")
                        break
            else:
                print("No hay coches en esta planta.")
        else:
            print("Número de planta inválido.")

    # 4. Plantas Libres
    elif entrada == "4":
        for i in range(8):
            libres = list(plantas_y_parqueaderos[i]).count(0)
            print(f"Planta {i+1}: {libres} plazas libres")

    # 5. Planta más Vacía
    elif entrada == "5":
        libres_por_planta = [list(plantas_y_parqueaderos[i]).count(0) for i in range(8)]
        planta_vacia = libres_por_planta.index(max(libres_por_planta)) + 1
        print(f"La planta más vacía es la {planta_vacia} con {max(libres_por_planta)} plazas libres")

    # 6. Total Coches
    elif entrada == "6":
        total = sum(list(plantas_y_parqueaderos[i]).count(1) for i in range(8))
        print(f"Total de coches en el parking: {total}")

    # 7. Mantenimiento Planta (sin index_libre)
    elif entrada == "7":
        planta = int(input("Ingrese el número de planta a vaciar (1-8): "))
        if 1 <= planta <= 8:
            coches_a_mover = list(plantas_y_parqueaderos[planta-1]).count(1)
            if coches_a_mover == 0:
                print(f"La planta {planta} ya está vacía.")
            else:
                plantas_y_parqueaderos[planta-1] = 0
                movidos = 0
                for _ in range(coches_a_mover):
                    espacio_encontrado = False
                    for i in range(8):
                        if i != planta-1:
                            for j in range(5):
                                if plantas_y_parqueaderos[i][j] == 0:
                                    plantas_y_parqueaderos[i][j] = 1
                                    movidos += 1
                                    espacio_encontrado = True
                                    break
                            if espacio_encontrado:
                                break
                    if not espacio_encontrado:
                        print("⚠ No hay más huecos disponibles para mover todos los coches.")
                        break
                print(f"Planta {planta} vaciada. {movidos} coches fueron reubicados.")
        else:
            print("Número de planta inválido.")

    # 8. Porcentajes de Ocupación con barra visual
    elif entrada == "8":
        print("\nPorcentaje de ocupación por planta:")
        for i in range(8):
            ocupadas = list(plantas_y_parqueaderos[i]).count(1)
            libres = 5 - ocupadas
            ocupacion = int((ocupadas / 5) * 100)
            barra = "#" * ocupadas + "." * libres
            print(f"Planta {i+1}: [{barra}] {ocupacion}% ({ocupadas} ocupadas, {libres} libres)")

    # 9. No Reservadas (Plantas 1,4,6,8 son reservadas)
    elif entrada == "9":
        reservadas = [0, 3, 5, 7]
        total = 0
        for i in range(8):
            if i not in reservadas:
                total += list(plantas_y_parqueaderos[i]).count(1)
        print(f"Total de coches en plantas no reservadas: {total}")

    else:
        print("Opción inválida.")
