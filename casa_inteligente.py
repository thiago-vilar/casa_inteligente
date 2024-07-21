from functools import reduce 
from dispositivos import Luz, Termostato, SistemaSeguranca

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class CasaInteligente(metaclass=SingletonMeta):
    def __init__(self):
        self.dispositivos = []
        self.observers = []

    def adicionar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)

    def remover_dispositivo(self, dispositivo):
        self.dispositivos.remove(dispositivo)

    def adicionar_observer(self, observer):
        self.observers.append(observer)

    def notificar_observers(self, dispositivo):
        for observer in self.observers:
            observer.update(dispositivo)

    def status_dispositivos(self):
        return [dispositivo.status() for dispositivo in self.dispositivos]

    def desligar_todas_as_luzes(self):
        list(map(lambda d: d.desligar(), filter(lambda d: isinstance(d, Luz) and d.state == 'ligada', self.dispositivos)))

    def dispositivos_on(self):
        return list(filter(lambda d: d.state != 'desligado', self.dispositivos))

    def total_dispositivos_on(self):
        return reduce(lambda total, d: total + 1 if d.state != 'desligado' else total, self.dispositivos, 0)
    
    def alterar_estado_todos_dispositivos(self, acao):
        for dispositivo in self.dispositivos:
            if isinstance(dispositivo, Luz):
                if acao == 'ligar luzes' and dispositivo.state == 'desligada':
                    dispositivo.ligar()
                elif acao == 'desligar luzes' and dispositivo.state == 'ligada':
                    dispositivo.desligar()
                elif acao == 'desligar todos os dispositivos' and dispositivo.state == 'ligada':
                    dispositivo.desligar()
            elif isinstance(dispositivo, Termostato):
                if acao == 'aquecer':
                    if dispositivo.state != 'desligado':
                        dispositivo.desligar()
                    dispositivo.aquecer()
                elif acao == 'esfriar':
                    if dispositivo.state != 'desligado':
                        dispositivo.desligar()
                    dispositivo.esfriar()
                elif acao in ['desligar termostato', 'desligar todos os dispositivos']:
                    dispositivo.desligar()
            elif isinstance(dispositivo, SistemaSeguranca):
                if acao == 'armar com gente em casa':
                    if dispositivo.state != 'desarmado':
                        dispositivo.desarmar()
                    dispositivo.armar_com_gente_em_casa()
                elif acao == 'armar sem gente em casa':
                    if dispositivo.state != 'desarmado':
                        dispositivo.desarmar()
                    dispositivo.armar_sem_gente_em_casa()
                elif acao in ['desarmar alarme', 'desligar todos os dispositivos']:
                    dispositivo.desarmar()