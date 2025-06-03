import os
import subprocess
import shutil
from util import log, atualizar_path

def instalar_python(text_log):
    log(text_log, "Instalando Python via Winget...")
    subprocess.run(["winget", "install", "--id", "Python.Python.3.11", "-e", "--silent"])
    log(text_log, "✅ Python instalado (verifique se a instalação foi concluída com sucesso).")

def instalar_chrome(text_log):
    log(text_log, "Instalando Google Chrome via Winget...")
    subprocess.run(["winget", "install", "Google.Chrome", "-e", "--silent"])
    log(text_log, "✅ Chrome instalado (verifique se a instalação foi concluída com sucesso).")

def remover_ambientes(script_dir, text_log):
    log(text_log, "Procurando ambientes virtuais...")
    found = False
    for dir_name in ["venv", "robot-env"]:
        path = os.path.join(script_dir, dir_name)
        if os.path.exists(path):
            log(text_log, f"Removendo {path}...")
            shutil.rmtree(path)
            found = True
    if not found:
        log(text_log, "Nenhum ambiente virtual encontrado.")
    else:
        log(text_log, "Ambientes removidos.")

def criar_ambiente_virtual(script_dir, text_log):
    venv_path = os.path.join(script_dir, "robot-env")
    if not os.path.exists(venv_path):
        log(text_log, f"Criando ambiente virtual em {venv_path}...")
        subprocess.run(["python", "-m", "venv", venv_path])
    else:
        log(text_log, "Ambiente virtual já existe.")
    return venv_path

def instalar_bibliotecas(venv_path, text_log):
    pip = os.path.join(venv_path, "Scripts", "pip.exe")
    python = os.path.join(venv_path, "Scripts", "python.exe")
    log(text_log, "Atualizando pip...")
    subprocess.run([python, "-m", "pip", "install", "--upgrade", "pip"])
    log(text_log, "Instalando robotframework, seleniumlibrary e webdriver-manager...")
    subprocess.run([pip, "install", "robotframework", "robotframework-seleniumlibrary", "webdriver-manager"])

def baixar_chromedriver(script_dir, venv_path, text_log):
    python = os.path.join(venv_path, "Scripts", "python.exe")
    log(text_log, "Baixando ChromeDriver via webdriver-manager...")
    script = """
from webdriver_manager.chrome import ChromeDriverManager
print(ChromeDriverManager().install())
"""
    result = subprocess.run([python, "-c", script], capture_output=True, text=True)
    chromedriver_path = result.stdout.strip().splitlines()[-1]
    log(text_log, f"ChromeDriver baixado em: {chromedriver_path}")

    driver_dest_folder = os.path.join(script_dir, "drivers")
    os.makedirs(driver_dest_folder, exist_ok=True)
    shutil.copy(chromedriver_path, driver_dest_folder)
    log(text_log, f"ChromeDriver copiado para {driver_dest_folder}")

    return driver_dest_folder

def configurar_path(venv_path, driver_folder, text_log):
    atualizar_path([os.path.join(venv_path, "Scripts"), driver_folder], text_log)
