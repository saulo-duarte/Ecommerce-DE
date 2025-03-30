# 📦 E-commerce Data Engineering

Este repositório contém um projeto de engenharia de dados para um e-commerce, utilizando **FastAPI**, **PostgreSQL**, **Snowflake**, **Airflow** e **dbt**. O gerenciamento do ambiente virtual e das dependências é feito com [uv](https://github.com/astral-sh/uv).

## 🚀 Como executar o projeto

### 1️⃣ Instalar o `uv`
Se ainda não tiver o `uv` instalado, execute:
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2️⃣ Instalar a versão correta do Python
O projeto requer a versão do Python definida no arquivo `.python-version`. Para garantir que está instalada, execute:
```sh
uv python install
```

### 3️⃣ Criar o ambiente virtual
```sh
uv venv
```

### 4️⃣ Ativar o ambiente virtual
- No **Linux/macOS**:
  ```sh
  source .venv/bin/activate
  ```
- No **Windows (PowerShell)**:
  ```powershell
  .venv\Scripts\Activate.ps1
  ```

### 5️⃣ Instalar as dependências
```sh
uv pip sync
```

Agora o ambiente está pronto para uso! 🎉



