
# Configurador de Ambiente Robot Framework Web

Este projeto em Python com interface Tkinter automatiza a configuração do ambiente para testes automatizados usando Robot Framework, SeleniumLibrary e WebDriver Manager, incluindo criação de ambiente virtual, instalação de dependências e configuração do ChromeDriver.

---

## Funcionalidades

- Verificação de conexão com internet  
- Verificação e instalação do Python via Winget (Windows)  
- Instalação do Google Chrome via Winget (Windows)  
- Criação e remoção de ambientes virtuais  
- Instalação de bibliotecas necessárias (`robotframework`, `robotframework-seleniumlibrary`, `webdriver-manager`)  
- Download e configuração do ChromeDriver automaticamente  
- Atualização da variável de ambiente PATH do usuário  
- Botão para testar se o ambiente foi configurado corretamente após a configuração  

---

## Pré-requisitos

- Sistema operacional Windows  
- Acesso à internet  
- Winget instalado e configurado  
- Python 3.11 ou superior (pode ser instalado pelo próprio script)  
- Visual Studio Code recomendado para edição e debug  

---

## Como usar

1. Clone este repositório:  
   ```bash
   git clone https://github.com/odairmoises/configura_ambiente_WEB_robot.git
   cd configura_ambiente_WEB_robot
   ```

2. (Opcional) Configure seu interpretador Python no VSCode para Python 3.11+

3. Instale as dependências manualmente (caso não queira usar o instalador via Winget):  
   ```bash
   pip install robotframework robotframework-seleniumlibrary webdriver-manager
   ```

4. Execute o programa:  
   ```bash
   python main.py
   ```

5. Na interface:  
   - Clique em **Iniciar Configuração** para configurar o ambiente.  
   - Após a configuração, o botão **Testar Ambiente** será habilitado para verificar se está tudo OK.  

---

## Estrutura do Projeto

```
configura_ambiente_WEB_robot/
│
├── main.py                 # Script principal com interface Tkinter
├── ambiente.py             # Funções para criação de ambiente virtual e instalação
├── verificacoes.py         # Funções para verificação de internet, Python, Winget e Chrome
├── util.py                 # Funções auxiliares e de logging
├── drivers/                # Pasta onde o ChromeDriver será copiado
├── .vscode/                # Configurações para VSCode (launch.json, tasks.json)
├── git_commit_push.ps1     # Script PowerShell para commit e push automatizado
├── README.md               # Este arquivo de documentação
└── .gitignore              # Arquivo gitignore padrão para Python
```

---

## Debug e Desenvolvimento

- Use o VSCode com a configuração pronta no `.vscode/launch.json` para debugar o `main.py`.  
- Use as tasks do VSCode em `.vscode/tasks.json` para instalar dependências e rodar o programa rapidamente.  

---

## Contato

Desenvolvido por Odair Oliveira  

LinkedIn: [https://www.linkedin.com/in/odair-m-oliveira/](https://www.linkedin.com/in/odair-m-oliveira/)  

---

Qualquer dúvida, sugestão ou bug, abra uma issue ou envie uma mensagem.
