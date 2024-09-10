# speed_test
teste de velocidade para uploads e downloads
Instruções: Como Criar um Script de Teste de Velocidade Local para Windows e Linux
Introdução

Este guia irá ensiná-lo a criar um script que executa um teste de velocidade de internet utilizando o speedtest-cli. O script é compatível com os sistemas operacionais Windows e Linux e pode ser configurado para listar servidores disponíveis e escolher um servidor específico para o teste.
Pré-requisitos

Antes de iniciar, você precisará dos seguintes itens:

    Python instalado (versão 3.x).
    speedtest-cli instalado:
        No Linux:

        bash

sudo apt install speedtest-cli

No Windows:
Use o gerenciador de pacotes pip para instalar:

bash

        pip install speedtest-cli

Estrutura do Script
1. Importar Bibliotecas Necessárias

Utilizamos a biblioteca subprocess para executar comandos do sistema operacional e platform para identificar o sistema operacional (Windows ou Linux).

python

import subprocess
import platform

2. Função Principal para Executar o Teste de Velocidade

A função run_speedtest permite:

    Listar servidores disponíveis com a opção --list.
    Selecionar um servidor específico usando a opção --server [ID].
    Customizar o teste de velocidade (com ou sem download/upload, formato JSON, etc.).

python

def run_speedtest(list_servers=False, server_id=None, simple=False, json_output=False, no_download=False, no_upload=False, limit_servers=10):
    system = platform.system().lower()

    # Define o comando para Windows ou Linux
    if system == 'windows':
        command = ['speedtest']
    elif system == 'linux':
        command = ['speedtest-cli']
    else:
        print("Sistema operacional não suportado.")
        return

    # Adiciona a opção de listar servidores
    if list_servers:
        command.append('--list')
        command.append(f'| head -n {limit_servers}')  # Limita a quantidade de servidores listados

    # Especifica um servidor pelo ID se fornecido
    if server_id:
        command.append('--server')
        command.append(str(server_id))

    # Outras opções
    if simple:
        command.append('--simple')
    if json_output:
        command.append('--json')
    if no_download:
        command.append('--no-download')
    if no_upload:
        command.append('--no-upload')

    # Executa o comando
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        print(result.stdout)
    except Exception as e:
        print(f"Erro ao executar o speedtest: {e}")

3. Executando o Script

Abaixo está um exemplo de como você pode configurar o script para:

    Listar os servidores disponíveis.
    Limitar a listagem de servidores a 10 entradas.
    Executar o teste de velocidade com um servidor específico (usando o server_id).

python

if __name__ == '__main__':
    # Aqui você pode ajustar as opções conforme necessário
    # Exemplo: Para listar servidores, use list_servers=True
    run_speedtest(list_servers=True, limit_servers=10)

4. Salvando e Executando o Script

    Salve o script com o nome speedtest.py.
    Torne o script executável no Linux (opcional):

    bash

chmod +x speedtest.py

Execute o script:

    No Linux:

    bash

python3 speedtest.py

No Windows:

bash

        python speedtest.py

5. Opções Adicionais

Você pode personalizar o script para diferentes cenários:

    Executar apenas o teste de upload:

    python

run_speedtest(no_download=True)

Listar servidores e escolher um servidor específico:

    Liste os servidores:

    bash

python3 speedtest.py --list

Escolha um servidor específico para o teste, utilizando o ID listado:

python

        run_speedtest(server_id=1234)

Conclusão

Este script oferece uma maneira simples de automatizar testes de velocidade de internet localmente em diferentes sistemas operacionais. Ele também permite personalizar o teste, escolhendo servidores específicos e ajustando o tipo de teste a ser executado.
