class Observer:
    def update(self, subject):
        pass

class DispositivoObserver(Observer):
    def update(self, dispositivo):
        print(f"Estado do dispositivo {dispositivo.nome} mudou para {dispositivo.state}")

