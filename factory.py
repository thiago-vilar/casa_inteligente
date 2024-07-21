from dispositivos import Luz, Termostato, SistemaSeguranca

class DispositivoFactory:
    @staticmethod
    def criar_dispositivo(tipo, nome):
        tipo = tipo.lower()
        if tipo == 'luz':
            return Luz(nome)
        elif tipo == 'termostato':
            return Termostato(nome)
        elif tipo == 'sistemaseguranca':
            return SistemaSeguranca(nome)
        else:
            raise ValueError('Tipo de dispositivo desconhecido')
