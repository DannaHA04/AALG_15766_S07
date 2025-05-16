# Pedimos la capacidad máxima de la mochila
capacidad = float(input("Ingrese la capacidad máxima de la mochila (kg): "))

# Lista para guardar cajas
cajas = []

# Pedir número de cajas
n = int(input("Ingrese el número de cajas: "))

# Ingresar datos de cada caja
for i in range(n):
    nombre = input(f"\nNombre de la caja #{i+1}: ")
    peso = float(input(f"Peso de la caja {nombre} (kg): "))
    precio = float(input(f"Precio de la caja {nombre} (S/): "))
    valor_kg = precio / peso
    cajas.append((valor_kg, nombre, peso, precio))

# Ordenar manualmente por valor/kg (método de selección directa)
for i in range(n):
    max_idx = i
    for j in range(i + 1, n):
        if cajas[j][0] > cajas[max_idx][0]:
            max_idx = j
    # Intercambiar posiciones
    cajas[i], cajas[max_idx] = cajas[max_idx], cajas[i]

# Proceso de llenado de mochila
peso_total = 0
valor_total = 0
seleccionadas = []

for valor_kg, nombre, peso, precio in cajas:
    if peso_total + peso <= capacidad:
        # Tomamos la caja completa
        peso_total += peso
        valor_total += precio
        seleccionadas.append((nombre, peso, precio))
    else:
        # Tomamos solo una fracción
        restante = capacidad - peso_total
        if restante > 0:
            fraccion = restante / peso
            peso_total += restante
            valor_total += precio * fraccion
            seleccionadas.append((nombre, restante, precio * fraccion))
        break  # Ya no entra más

# Resultados
print("\nCajas seleccionadas:")
for nombre, peso, precio in seleccionadas:
    print(f"- {nombre}: {peso:.2f} kg, S/{precio:.2f}")

print(f"\nPeso total en la mochila: {peso_total:.2f} kg")
print(f"Valor total obtenido: S/{valor_total:.2f}")