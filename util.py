import tkinter as tk
import os
import shutil
import winreg

def log(text_log: tk.Text, msg: str):
    text_log.insert(tk.END, msg + "\n")
    text_log.see(tk.END)
    text_log.update()

def atualizar_path(paths_to_add: list, text_log: tk.Text):
    import winreg
    try:
        reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        key = winreg.OpenKey(reg, r'Environment', 0, winreg.KEY_ALL_ACCESS)
        try:
            current_path, _ = winreg.QueryValueEx(key, 'Path')
        except FileNotFoundError:
            current_path = ""

        paths = current_path.split(";") if current_path else []
        for p in paths_to_add:
            if p not in paths:
                paths.append(p)

        new_path = ";".join(paths)
        winreg.SetValueEx(key, 'Path', 0, winreg.REG_EXPAND_SZ, new_path)
        winreg.CloseKey(key)

        log(text_log, "✅ PATH atualizado. Talvez precise reiniciar o terminal ou o PC.")
    except Exception as e:
        log(text_log, f"❌ Erro ao atualizar PATH: {e}")

def remover_diretorio(path: str, text_log: tk.Text):
    if os.path.exists(path):
        shutil.rmtree(path)
        log(text_log, f"Removido: {path}")
    else:
        log(text_log, f"Diretório não existe: {path}")
