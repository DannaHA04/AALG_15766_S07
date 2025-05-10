def calcular_cambio(montoVuelto, billetes):
    print("\nCambio necesario:")
    for valor in billetes:
        cantidad = int(montoVuelto // valor)
        if cantidad > 0:
            print(str(cantidad) + " de S/ " + str(valor))
            montoVuelto = montoVuelto - (cantidad * valor)
            montoVuelto = round(montoVuelto, 2)

billetesDisponibles = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05]
montoVuelto = float(input("Ingrese el monto del vuelto: "))
calcular_cambio(montoVuelto, billetesDisponibles)