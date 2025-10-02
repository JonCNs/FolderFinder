# 🔎 Folder Finder (Python Automation Script)

Um simples script em **Python** desenvolvido para automatizar buscas em pastas de uma empresa, utilizando palavras-chave extraídas de uma planilha do **Excel**.  

A palavra-chave inserida é usada para identificar a **regional**, **cliente**, **investimento**, **ano** e **período**, montando automaticamente o caminho até os contratos. O script então exibe um relatório de pastas/arquivos encontrados e permite abrir a pasta diretamente no Explorer.

---

## 🇧🇷 Descrição (Português)

### ⚙️ Funcionalidades
- 🔒 **Controle de versão via Firebase** – apenas versões permitidas rodam.
- 📂 **Definição de pasta base** para buscas.
- 📝 **Configuração via JSON (`data.json`)** com clientes, regionais e investimentos.
- 🔍 **Busca automática** em diretórios com base nas palavras-chave fornecidas.
- 🖥️ **Interface em terminal** com menus interativos e saída colorida.
- 📊 **Relatório de resultados** mostrando pastas e arquivos encontrados.
- 📑 **Abertura do diretório no Explorer**.

### 📦 Dependências
Instale as bibliotecas necessárias:
```
bash
pip install pyrebase4 colorama
```

🚀 Como usar
Clone ou baixe este repositório.

Execute o script:

bash
Copiar código
python main.py
No menu principal:

```
[1] Procurar diretórios usando palavras-chave.

[2] Definir pasta base.

[3] Sair.

Insira as palavras-chave (ex.: COMBOS CLIENTE2 SUL P2 F24).
```

O script exibirá resultados e permitirá abrir a pasta no Explorer.

📂 Estrutura de dados (data.json)
Na primeira execução, um arquivo data.json é criado com dados como:

```
{
  "Regional": { "CO": "REGIONAL CO", "LESTE": "REGIONAL LESTE" },
  "Cliente": { "REGIONAL CO": [{ "cliente1": "cliente1", "cliente2": "cliente2" }] },
  "Investimento": { "Combos": "Combos", "Estrutural": "Execução Estrutural" },
  "Ano": { "F24": "FY24" },
  "Dia": { "Q1": "P03", "P1": "P01" },
  "dirBase": ""
}
```

🇬🇧 Description (English)
⚙️ Features
🔒 Version control via Firebase – only allowed versions run.

📂 Base folder setup for searches.

📝 Configuration via JSON (data.json) with clients, regions, and investments.

🔍 Automatic directory search based on input keywords.

🖥️ Terminal interface with interactive menus and colored output.

📊 Results report listing folders and files found.

📑 Open directory in Explorer.

📦 Dependencies
Install the required libraries:
```
pip install pyrebase4 colorama
```

🚀 How to use
Clone or download this repository.

Run the script:

```
python main.py
```

In the main menu:

```
[1] Search directories using keywords.

[2] Define base folder.

[3] Exit.

Enter keywords (e.g., COMBOS CLIENTE2 SUL P2 F24).
```

The script will show results and allow opening the folder in Explorer.

📂 Data structure (data.json)
On the first run, a data.json file is generated with data such as:

```
{
  "Regional": { "CO": "REGIONAL CO", "LESTE": "REGIONAL LESTE" },
  "Cliente": { "REGIONAL CO": [{ "cliente1": "cliente1", "cliente2": "cliente2" }] },
  "Investimento": { "Combos": "Combos", "Estrutural": "Execução Estrutural" },
  "Ano": { "F24": "FY24" },
  "Dia": { "Q1": "P03", "P1": "P01" },
  "dirBase": ""
}
```

⚠️ Aviso Legal / Legal Notice

Este script é confidencial e contém informações proprietárias.  
Ele é fornecido apenas para uso interno e não deve ser compartilhado sem autorização.  
Ao executar este script, você concorda com os termos de uso.  

This script is confidential and contains proprietary information.  
It is provided for internal use only and must not be shared without prior authorization.  
By running this script, you agree to the terms of use.  

📌 Versão / Version
Atual / Current: v1.0 BETA

👨‍💻 Tecnologias / Technologies
Python

Pyrebase4

Colorama

yaml

---
