# ejercicio de simulacion del hijo prodigo
class HijoProdigo:
    def __init__(self, nombre, arrepentimiento = 0, dinero=100, dignidad=50, hambre=0):
        self.nombre = nombre
        self.dinero = dinero
        self.dignidad = dignidad
        self.hambre = hambre
        self.arrpentimiento = arrepentimiento
        print(f"\nBienvenido {nombre}")
        print(f"Felicidades, recibiste tu herrencia de {dinero}")


    def gastar_todo(self, dinero, dignidad, hambre):
        # el problema no da indicaciones exactas de como realizar, asi que lo hare como se pueda
        print("Te iras de casa y dejaras a tu padre y hermano")
        print("\nEstas seguro de hacer esto?")
        decicion = int(input("1: SI\n2: NO\n:"))
        if decicion == 1:
            print("Te fuiste de casa")
            if dinero > 0:
                print("Estas de fiesta y gastando tu dinero")
                dinero -= 20 #Cada fiesta reducira 20 monedas
                dignidad -= 20
                hambre += 50
                print(f"Estado: \nDinero = {dinero}\nDignidad = {dignidad}\nHambre = {hambre}")
        elif decicion == 2:
            return
        else:
            print("Opcion incorrecta")

    def invertir(self, dinero):
        print("Usted esta invirtiendo")
        dinero += 20
        print(f"Estado:\n Dinero = {dinero}")

    def ahorrar(self, dinero):
        print("Usted esta ahorrando :)")
        print(f"Estado:\n Dinero = {dinero}")

    def trabajar(self, dinero):
        print("Usted esta trabajando.")
        dinero += 40
        print(f"Estado:\n Dinero = {dinero}")

    def reflexionar(self, arrepentimiento, hambre):
        if hambre > 40:
            arrepentimiento+=10

    def estado_jugador(self):
        pass# quiero colocar un metodo estado el cual el jugador puede consultar


print("Bienvenido al juego del hijo prodigo")
jugador = HijoProdigo(input("Ingrese su nombre: "))
intentos = 0
opcion = 0
while jugador.dinero >= 0:

    if intentos == 0:
        print("Que quieres hacer?\n")
        print("1: Gastarlo todo en fiestas")
        print("2: Invertir una parte")
        print("3: Ahorrar")
        print("4: Trabajar")
        #intentos += 1
        opcion = int(input("\n Opcion: "))
        if opcion == 1:
            jugador.gastar_todo(jugador.dinero, jugador.dignidad, jugador.hambre)

