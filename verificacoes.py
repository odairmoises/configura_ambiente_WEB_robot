import subprocess
import urllib.request

def verificar_internet(text_log):
    from util import log
    log(text_log, "Verificando conexão com a internet...")
    try:
        urllib.request.urlopen("https://pypi.org", timeout=5)
        log(text_log, "✅ Conexão com a internet OK.")
        return True
    except:
        log(text_log, "❌ Sem conexão com a internet.")
        return False

def verificar_winget(text_log):
    from util import log
    log(text_log, "Verificando Winget...")
    try:
        subprocess.run(["winget", "--version"], capture_output=True, check=True)
        log(text_log, "✅ Winget encontrado.")
        return True
    except:
        log(text_log, "❌ Winget não encontrado.")
        return False

def verificar_python(text_log):
    from util import log
    log(text_log, "Verificando Python...")
    try:
        subprocess.run(["python", "--version"], capture_output=True, check=True)
        log(text_log, "✅ Python encontrado.")
        return True
    except:
        log(text_log, "❌ Python não encontrado.")
        return False
