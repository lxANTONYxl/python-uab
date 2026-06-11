# ejercicio de simulacion del hijo prodigo
class HijoProdigo:
    def __init__(self, nombre, arrepentimiento = 0, dinero=100, dignidad=50, hambre=0):
        self.nombre = nombre
        self.dinero = dinero
        self.dignidad = dignidad
        self.hambre = hambre
        self.arrpentimiento = arrepentimiento

    def gastar_todo(self, dinero, dignidad, hambre):
        # el problema no da indicaciones exactas de como realizar, asi que lo hare como se pueda
        if dinero > 0:
            print("Estas de fiesta y gastando tu dinero")
            dinero -= 20 #Cada fiesta reducira 20 monedas
            dignidad -= 20
            hambre += 50
            print(f"Estado: \nDinero = {dinero}\nDignidad = {dignidad}\nHambre = {hambre}")

    def invertir(self):
        pass
    def ahorrar(self):
        pass
    def trabajar(self):
        pass
    def reflexionar(self, arrepentimiento, hambre):
        if hambre > 40:
            arrepentimiento+=10


print("Bienvenido al juego del hijo prodigo")
jugador = HijoProdigo(input("Ingrese su nombre: "))
jugador.gastar_todo(jugador.dinero,jugador.dignidad,jugador.hambre)