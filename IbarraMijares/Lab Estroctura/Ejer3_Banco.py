class CuentaBancaria:
    def __init__(self, titular, _saldo_inicial):
        self._titular = titular  #Protegido
        self._saldoinicial = _saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldoinicial += cantidad
            print(f"Se ha depositado la cantidad de ${cantidad}. Nuevo saldo ${self._saldoinicial}.")
        else:
            print("La cantidad debe ser positiva")

    def retirar(self, cantidad_retirar):
        if cantidad_retirar > 0:
            if cantidad_retirar <= self._saldoinicial:
                self._saldoinicial -= cantidad_retirar
                print(f"Se ha retirado la cantidad de ${cantidad_retirar}. Nuevo saldo ${self._saldoinicial}")
            else:
                print("Saldo Insuficiente")
        else:
            print(" Ingresar una cantidad positiva")

    def consultar_saldo(self):
        print(f"Tu saldo disponible es  ${self._saldoinicial}")

cuenta = CuentaBancaria("David ibarra", 500)
cuenta.depositar(100)
cuenta.retirar(200)
cuenta.consultar_saldo()