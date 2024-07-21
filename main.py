import argparse
from casa_inteligente import CasaInteligente
from factory import DispositivoFactory
from observer import DispositivoObserver
from dispositivos import Luz, Termostato, SistemaSeguranca

def main():
    parser = argparse.ArgumentParser(description='Sistema de Casa Inteligente')
    parser.add_argument('--max-dispositivos', type=int, default=10, help='Número máximo de dispositivos')
    args = parser.parse_args()

    casa = CasaInteligente()
    casa.max_dispositivos = args.max_dispositivos

    observer = DispositivoObserver()
    casa.adicionar_observer(observer)

    acoes = {
        1: 'ligar luzes',
        2: 'desligar luzes',
        3: 'aquecer',
        4: 'esfriar',
        5: 'desligar termostato',
        6: 'armar com gente em casa',
        7: 'armar sem gente em casa',
        8: 'desarmar alarme',
        9: 'desligar todos os dispositivos'
    }

    while True:
        comando = input("Digite um comando (adicionar, remover, status, alterar, alterar todos, sair): ").strip().lower()
        if comando == 'sair':
            break
        elif comando == 'adicionar':
            tipo = input("Digite o tipo de dispositivo (Luz, Termostato, SistemaSeguranca): ").strip().capitalize()
            nome = input("Digite o nome do dispositivo: ").strip().upper()
            try:
                dispositivo = DispositivoFactory.criar_dispositivo(tipo, nome)
                casa.adicionar_dispositivo(dispositivo)
            except ValueError as e:
                print(e)
        elif comando == 'remover':
            nome = input("Digite o nome do dispositivo a ser removido: ").strip().upper()
            dispositivo = next((d for d in casa.dispositivos if d.nome == nome), None)
            if dispositivo:
                casa.remover_dispositivo(dispositivo)
        elif comando == 'status':
            status_info = casa.status_dispositivos()
            for info in status_info:
                print(info)
        elif comando == 'alterar':
            nome = input("Digite o nome do dispositivo: ").strip().upper()
            dispositivo = next((d for d in casa.dispositivos if d.nome == nome), None)
            if dispositivo:
                if isinstance(dispositivo, Luz):
                    estado = input("Digite a ação (ligar, desligar): ").strip().lower()
                    if estado == 'ligar' and dispositivo.state == 'desligada':
                        dispositivo.ligar()
                    elif estado == 'desligar' and dispositivo.state == 'ligada':
                        dispositivo.desligar()
                    else:
                        print("Ação inválida para Luz.")
                elif isinstance(dispositivo, Termostato):
                    estado = input("Digite a ação (aquecer, esfriar, desligar): ").strip().lower()
                    if estado == 'aquecer':
                        if dispositivo.state != 'desligado':
                            dispositivo.desligar()
                        dispositivo.aquecer()
                    elif estado == 'esfriar':
                        if dispositivo.state != 'desligado':
                            dispositivo.desligar()
                        dispositivo.esfriar()
                    elif estado == 'desligar' and dispositivo.state != 'desligado':
                        dispositivo.desligar()
                    else:
                        print("Ação inválida para Termostato.")
                elif isinstance(dispositivo, SistemaSeguranca):
                    estado = input("Digite a ação (armar com gente em casa, armar sem gente em casa, desarmar): ").strip().lower()
                    if estado == 'armar com gente em casa':
                        if dispositivo.state != 'desarmado':
                            dispositivo.desarmar()
                        dispositivo.armar_com_gente_em_casa()
                    elif estado == 'armar sem gente em casa':
                        if dispositivo.state != 'desarmado':
                            dispositivo.desarmar()
                        dispositivo.armar_sem_gente_em_casa()
                    elif estado == 'desarmar' and dispositivo.state != 'desarmado':
                        dispositivo.desarmar()
                    else:
                        print("Ação inválida para Sistema de Segurança.")
                else:
                    print("Tipo de dispositivo desconhecido.")
            else:
                print("Dispositivo não encontrado.")
        elif comando == 'alterar todos':
            print("\nEscolha uma ação fornecendo o número correspondente:")
            for key, value in acoes.items():
                print(f"{key}: {value}")
            while True:
                try:
                    escolha = int(input("Digite o número da ação desejada: "))
                    acao = acoes.get(escolha, None)
                    if acao:
                        casa.alterar_estado_todos_dispositivos(acao)
                        break
                    else:
                        print("Ação inválida. Por favor, digite um número de 1 a 9.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número. Ex: 1, 2, 3,...")
        else:
            print("Comando não reconhecido.")

if __name__ == "__main__":
    main()
