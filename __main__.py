import platform
import subprocess
import json
from tqdm import tqdm
import time

def run_speedtest(server_id=None):
    # Detecta o sistema operacional
    os_type = platform.system()
    
    # Comando base do Speedtest
    base_command = ["speedtest-cli"]
    
    # Adiciona opções para listar servidores ou escolher um específico
    if server_id:
        base_command += ["--server", str(server_id)]

    # Adiciona opções para resultados em JSON para análise
    base_command += ["--json"]

    # Exibe a configuração do Speedtest e lista de servidores
    print("Retrieving speedtest.net configuration...")
    
    try:
        # Executa o comando Speedtest para obter a configuração e lista de servidores
        config_result = subprocess.run(base_command[:-1], capture_output=True, text=True)
        print(config_result.stdout)
        
        # Exibe informações sobre o servidor selecionado
        print("Retrieving speedtest.net server list...")
        list_command = ["speedtest-cli", "--list"]
        list_result = subprocess.run(list_command, capture_output=True, text=True)
        print(list_result.stdout)
        
        print("Selecting best server based on ping...")
        server_result = subprocess.run(base_command[:-1] + ["--best"], capture_output=True, text=True)
        print(server_result.stdout)

        # Executa o comando Speedtest e captura a saída
        result = subprocess.run(base_command, capture_output=True, text=True)
        json_output = result.stdout
    except Exception as e:
        print(f"Ocorreu um erro ao executar o teste de velocidade: {e}")
        return
    
    # Processa o JSON para extrair download e upload
    try:
        data = json.loads(json_output)
        download_speed = data.get("download", 0) / 1_000_000  # Em Mbps
        upload_speed = data.get("upload", 0) / 1_000_000  # Em Mbps
    except json.JSONDecodeError:
        print("Erro ao processar o JSON da saída do Speedtest.")
        return
    except Exception as e:
        print(f"Ocorreu um erro ao processar os resultados do teste: {e}")
        return

    # Simulação de progresso para download
    print("Iniciando o teste de download...")
    for i in tqdm(range(100), desc="Download", ncols=100):
        time.sleep(0.05)  # Simulação de tempo de espera para cada etapa do progresso

    print(f"Velocidade de Download: {download_speed:.2f} Mbps")

    # Simulação de progresso para upload
    print("Iniciando o teste de upload...")
    for i in tqdm(range(100), desc="Upload", ncols=100):
        time.sleep(0.05)  # Simulação de tempo de espera para cada etapa do progresso

    print(f"Velocidade de Upload: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    # Executa o teste com o progresso para download e upload
    run_speedtest()
