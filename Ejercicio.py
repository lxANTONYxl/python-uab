# ejercicio de simulacion del hijo prodigo

# variables

nombre_jugador = input("Ingrese su nombre: ")
dinero = 100
dignidad = 50
hambre = 0

print("Ustede a recibido su herencia.")

# condiciones
# mostrar 3 opciones: Gastarlo todo, Invertir una parte, Ahorrar
print("Seleccione una opcion\n")

print("1. Gastarlo todo en fiestas")
print("3. Invertir una parte")
print("3. Ahorrar")
opcion = input("Opcion: ")
if opcion == 1:
    dinero = 0
    dignidad -= 20
    hambre += 50
elif opcion == 2:
    dinero +=20
elif opcion ==3:
    print("Usted esta ahorrando")
else:
    print("Opcion invalida")