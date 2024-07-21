from abc import ABC, abstractmethod
from transitions import Machine

class Dispositivo(ABC):
    @abstractmethod
    def status(self):
        pass

class Luz(Dispositivo):
    states = ['desligada', 'ligada']

    def __init__(self, nome):
        self.nome = nome
        self.machine = Machine(model=self, states=Luz.states, initial='desligada')
        self.machine.add_transition('ligar', 'desligada', 'ligada')
        self.machine.add_transition('desligar', 'ligada', 'desligada')

    def status(self):
        return f'Luz {self.nome} está {self.state}'

class Termostato(Dispositivo):
    states = ['desligado', 'aquecendo', 'esfriando']

    def __init__(self, nome):
        self.nome = nome
        self.machine = Machine(model=self, states=Termostato.states, initial='desligado')
        self.machine.add_transition('aquecer', 'desligado', 'aquecendo')
        self.machine.add_transition('esfriar', 'desligado', 'esfriando')
        self.machine.add_transition('desligar', ['aquecendo', 'esfriando'], 'desligado')

    def status(self):
        return f'Termostato {self.nome} está {self.state}'

class SistemaSeguranca(Dispositivo):
    states = ['desarmado', 'armado_com_gente_em_casa', 'armado_sem_ninguem_em_casa']

    def __init__(self, nome):
        self.nome = nome
        self.machine = Machine(model=self, states=SistemaSeguranca.states, initial='desarmado')
        self.machine.add_transition('armar_com_gente_em_casa', 'desarmado', 'armado_com_gente_em_casa')
        self.machine.add_transition('armar_sem_gente_em_casa', 'desarmado', 'armado_sem_ninguem_em_casa')
        self.machine.add_transition('desarmar', ['armado_com_gente_em_casa', 'armado_sem_ninguem_em_casa'], 'desarmado')

    def status(self):
        return f'Sistema de Segurança {self.nome} está {self.state}'
