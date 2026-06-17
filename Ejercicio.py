# ejercicio de simulacion del hijo prodigo
class HijoProdigo:
    def __init__(self, nombre, arrepentimiento = 0, dinero=100, dignidad=50, hambre=0):
        self.nombre = nombre
        self.dinero = dinero
        self.dignidad = dignidad
        self.hambre = hambre
        self.arrepentimiento = arrepentimiento
        print(f"\nBienvenido {nombre}")
        print(f"Felicidades, recibiste tu herrencia de {dinero}")


    def gastar_todo(self):
        # el problema no da indicaciones exactas de como realizar, asi que lo hare como se pueda
        print("Te iras de casa y dejaras a tu padre y hermano")
        print("\nEstas seguro de hacer esto?")
        decicion = int(input("1: SI\n2: NO\n:"))
        if decicion == 1:
            print("Te fuiste de casa")
            if self.dinero > 0:
                print("Estas de fiesta y gastando tu dinero")
                self.dinero -= 20 #Cada fiesta reducira 20 monedas
                self.dignidad -= 20
                self.hambre += 50
                print(f"Estado: \nDinero = {self.dinero}\nDignidad = {self.dignidad}\nHambre = {self.hambre}")
        elif decicion == 2:
            return decicion
        else:
            print("Opcion incorrecta")

    def invertir(self):
        print("Usted esta invirtiendo")
        self.dinero += 20
        print(f"Estado:\n Dinero = {self.dinero}")

    def ahorrar(self):
        print("Usted esta ahorrando :)")
        print(f"Estado:\n Dinero = {self.dinero}")

    def trabajar(self):
        print("Usted esta trabajando.")
        self.dinero += 40
        print(f"Estado:\n Dinero = {self.dinero}")

    def reflexionar(self):
        if self.hambre > 40:
            self.arrepentimiento +=10

    def estado_jugador(self):
        pass# quiero colocar un metodo estado el cual el jugador puede consultar


print("Bienvenido al juego del hijo prodigo")
jugador = HijoProdigo(input("Ingrese su nombre: "))
dinero = jugador.dinero
dignidad = jugador.dignidad
hambre = jugador.hambre
intentos = 0
opcion = 0
while dinero >= 0:

    if intentos == 0:
        print("Que quieres hacer?\n")
        print("1: Gastarlo todo en fiestas")
        print("2: Invertir una parte")
        print("3: Ahorrar")
        print("4: Trabajar")

        opcion = int(input("\n Opcion: "))
        if opcion == 1:
            jugador.gastar_todo()
            #intentos += 1
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        else:
            pass

