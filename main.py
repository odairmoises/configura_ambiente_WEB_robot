import os
import tkinter as tk
from tkinter import messagebox, scrolledtext
import webbrowser
from verificacoes import verificar_internet, verificar_winget, verificar_python
from ambiente import (
    instalar_python, instalar_chrome, remover_ambientes, criar_ambiente_virtual,
    instalar_bibliotecas, baixar_chromedriver, configurar_path
)
from util import log

# Interface Tkinter
root = tk.Tk()
root.title("Configurar Ambiente Robot Framework")
root.geometry("700x500")

script_dir = os.path.dirname(os.path.abspath(__file__))

# Menu
menu_bar = tk.Menu(root)
menu_ajuda = tk.Menu(menu_bar, tearoff=0)
def abrir_sobre():
    sobre = tk.Toplevel(root)
    sobre.title("Sobre")
    sobre.geometry("400x200")
    sobre.resizable(False, False)
    tk.Label(sobre, text="Desenvolvido por Odair Oliveira", font=("Arial", 12, "bold")).pack(pady=10)
    tk.Label(sobre, text="LinkedIn:", font=("Arial", 11)).pack()
    link = tk.Label(sobre, text="https://www.linkedin.com/in/odair-m-oliveira/",
                    fg="blue", cursor="hand2")
    link.pack()
    link.bind("<Button-1>", lambda e: webbrowser.open_new(
        "https://www.linkedin.com/in/odair-m-oliveira/"))
    tk.Button(sobre, text="Fechar", command=sobre.destroy).pack(pady=20)
menu_ajuda.add_command(label="Sobre", command=abrir_sobre)
menu_bar.add_cascade(label="Ajuda", menu=menu_ajuda)
root.config(menu=menu_bar)

frame = tk.Frame(root)
frame.pack(pady=10)

var_remover = tk.BooleanVar()
chk_remover = tk.Checkbutton(frame, text="Remover ambientes virtuais existentes", variable=var_remover)
chk_remover.pack()

text_log = scrolledtext.ScrolledText(root, width=80, height=20)
text_log.pack(padx=10, pady=10)

def executar():
    log(text_log, "\n=== INICIANDO CONFIGURAÇÃO DO AMBIENTE ===")
    btn_testar.config(state="disabled")

    if not verificar_internet(text_log):
        messagebox.showerror("Erro", "Sem conexão com a internet.")
        return

    if not verificar_winget(text_log):
        messagebox.showerror("Erro", "Winget não encontrado.")
        return

    if not verificar_python(text_log):
        instalar_python(text_log)

    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if not os.path.exists(chrome_path):
        instalar_chrome(text_log)

    if var_remover.get():
        remover_ambientes(script_dir, text_log)

    venv_path = criar_ambiente_virtual(script_dir, text_log)
    instalar_bibliotecas(venv_path, text_log)
    driver_folder = baixar_chromedriver(script_dir, venv_path, text_log)
    configurar_path(venv_path, driver_folder, text_log)

    log(text_log, "\n=== AMBIENTE CONFIGURADO COM SUCESSO! ✅ ===")
    messagebox.showinfo("Sucesso", "Ambiente configurado com sucesso!")

    btn_testar.config(state="normal")

def testar_ambiente():
    # Aqui você pode importar e reutilizar a função testar_ambiente modularizada ou deixar inline.
    # Para simplificar, coloco ela aqui com os logs:
    from subprocess import run
    import urllib.request
    import winreg

    log(text_log, "\n=== INICIANDO TESTE DO AMBIENTE ===")

    try:
        log(text_log, "Testando conexão com a internet...")
        urllib.request.urlopen("https://pypi.org", timeout=5)
        log(text_log, "✅ Internet OK.")

        log(text_log, "Testando instalação do Python...")
        run(["python", "--version"], check=True, capture_output=True)
        log(text_log, "✅ Python OK.")

        log(text_log, "Testando instalação do Pip...")
        run(["pip", "--version"], check=True, capture_output=True)
        log(text_log, "✅ Pip OK.")

        venv_path = os.path.join(script_dir, "robot-env")
        if os.path.exists(venv_path):
            log(text_log, "✅ Ambiente virtual encontrado.")
        else:
            log(text_log, "❌ Ambiente virtual NÃO encontrado.")

        log(text_log, "Testando bibliotecas Robot Framework e SeleniumLibrary...")
        try:
            import robot
            import SeleniumLibrary
            log(text_log, "✅ Bibliotecas instaladas.")
        except ImportError:
            log(text_log, "❌ Bibliotecas não instaladas corretamente.")

        driver_folder = os.path.join(script_dir, "drivers")
        chromedriver_path = os.path.join(driver_folder, "chromedriver.exe")
        if os.path.exists(chromedriver_path):
            log(text_log, "✅ ChromeDriver encontrado.")
        else:
            log(text_log, "❌ ChromeDriver NÃO encontrado.")

        log(text_log, "Testando variável PATH do usuário...")
        reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        key = winreg.OpenKey(reg, r'Environment', 0, winreg.KEY_READ)
        current_path, _ = winreg.QueryValueEx(key, 'Path')
        winreg.CloseKey(key)
        paths = current_path.split(";")
        if any(p in paths for p in [os.path.join(venv_path, "Scripts"), driver_folder]):
            log(text_log, "✅ PATH configurado corretamente.")
        else:
            log(text_log, "❌ PATH não configurado corretamente.")

        messagebox.showinfo("Teste do Ambiente", "Teste concluído. Verifique os logs para detalhes.")
    except Exception as e:
        log(text_log, f"❌ Erro no teste: {e}")
        messagebox.showerror("Erro no Teste", f"Erro ao testar ambiente:\n{e}")

btn_executar = tk.Button(frame, text="Iniciar Configuração", command=executar,
                         bg="green", fg="white", width=25, height=2)
btn_executar.pack(pady=10)

btn_testar = tk.Button(frame, text="Testar Ambiente", command=testar_ambiente,
                       bg="blue", fg="white", width=25, height=2, state="disabled")
btn_testar.pack(pady=5)

root.mainloop()
