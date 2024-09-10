import subprocess
import platform

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

if __name__ == '__main__':
    # Aqui você pode ajustar as opções conforme necessário
    run_speedtest(list_servers=True, limit_servers=10)
