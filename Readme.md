# Sistema de Casa Inteligente

## Visão Geral

O objetivo deste projeto é projetar e implementar um sistema de casa inteligente abrangente que integra vários conceitos de programação, incluindo programação orientada a objetos, padrões de projeto, máquinas de estados, e programação funcional.

## Estrutura do Projeto

- `casa_inteligente.py`: Contém a classe `CasaInteligente` e a implementação do padrão Singleton.
- `dispositivos.py`: Contém a classe base `Dispositivo` e as classes derivadas `Luz`, `Termostato`, e `SistemaSeguranca`.
- `factory.py`: Contém a implementação do padrão Factory.
- `observer.py`: Contém a implementação do padrão Observer.
- `main.py`: Contém a lógica principal do programa, incluindo a interface de linha de comando.
- `README.md`: Este arquivo.

## Instruções para Configurar e Executar o Projeto

1. Clone o repositório.
2. Instale as dependências necessárias:
    ```bash
    pip install transitions
    ```
3. Execute o programa:
    ```bash
    python main.py --max-dispositivos 10
    ```

## Componentes Principais

- **Padrão Singleton**: Assegura uma única instância de `CasaInteligente` para centralizar o gerenciamento dos dispositivos.
- **Padrão Factory**: Facilita a criação de diferentes tipos de dispositivos sem expor a lógica de criação ao cliente.
- **Padrão Observer**: Permite que o sistema notifique automaticamente os componentes registrados sobre quaisquer mudanças de estado nos dispositivos.
- **Máquinas de Estados**: Utilizado para gerenciar os estados dos dispositivos através da biblioteca `transitions`.
- **Programação Funcional**: Emprega `map`, `filter` e `reduce` para operações eficientes e expressivas sobre coleções de dispositivos.

## Exemplos de Uso da CLI

- Adicionar um dispositivo:
    ```
    Digite um comando (adicionar, remover, status, alterar, alterar todos, sair): adicionar
    Digite o tipo de dispositivo (Luz, Termostato, SistemaSeguranca): Luz
    Digite o nome do dispositivo: Sala
    ```
- Verificar o status dos dispositivos:
    ```
    Digite um comando (adicionar, remover, status, alterar, sair): status
    Luz Sala está desligada
    ```
