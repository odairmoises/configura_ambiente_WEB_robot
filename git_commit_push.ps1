# Confirma se está na pasta do projeto
Write-Host "Iniciando commit e push no repositório Git..."

# Inicializa git se ainda não estiver inicializado
if (-not (Test-Path ".git")) {
    git init
}

# Adiciona arquivos
git add .

# Commit com mensagem
git commit -m "Primeiro commit: estrutura inicial e scripts de configuração"

# Define branch principal
git branch -M main

# Configura remote (remove se já existir para evitar erro)
git remote remove origin -ErrorAction SilentlyContinue
git remote add origin https://github.com/odairmoises/configura_ambiente_WEB_robot.git

# Push para o remoto
git push -u origin main

Write-Host "Push realizado com sucesso!"
