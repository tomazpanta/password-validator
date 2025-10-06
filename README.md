# Projeto: Validador de Senhas (Python / Pytest)

Este é um projeto simples que implementa uma API de validação de senhas em Python. O foco principal é a criação de uma suíte robusta de **testes unitários** para garantir que todas as regras de negócio sejam estritamente seguidas, cobrindo cenários de sucesso e de falha (exceções), atingindo 100% de cobertura de código.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Testes Unitários:** Pytest
* **Cobertura de Testes:** pytest-cov
* **Configuração de Caminho:** `pytest.ini` e `__init__.py`

## 📋 Regras de Negócio Testadas

O módulo `password_validator.py` implementa as seguintes regras de segurança, sendo que a violação de qualquer uma delas deve disparar uma exceção customizada (`InvalidPasswordException`).

| Regra | Cenário de Teste |
| :--- | :--- |
| **R1. Comprimento Mínimo** | A senha deve ter no mínimo **8 caracteres**. |
| **R2. Caractere Maiúsculo** | A senha deve conter pelo menos **uma letra maiúscula**. |
| **R3. Caractere Minúsculo** | A senha deve conter pelo menos **uma letra minúscula**. |
| **R4. Dígito Numérico** | A senha deve conter pelo menos **um número**. |
| **R5. Espaços em Branco** | A senha **não pode** conter espaços em branco. |
| **R6. Entradas Inválidas** | A senha **não pode ser nula** ou uma **string vazia**. |

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar o ambiente e rodar os testes no macOS/Linux.

### 1. Clonar o Repositório

```bash
git clone [https://github.com/tomazpanta/password-validator]
cd password-validator-project
````

### 2\. Configurar e Ativar o Ambiente Virtual (venv)

```bash
# Cria o ambiente virtual
python3 -m venv venv

# Ativa o ambiente virtual (macOS/Linux)
source venv/bin/activate
```

### 3\. Instalar Dependências

Com o ambiente virtual **ATIVO** (`(venv)` no prompt):

```bash
pip install -r requirements.txt
```

### 4\. Rodar os Testes e Gerar o Relatório de Cobertura

Execute o comando a seguir para rodar todos os testes, gerar a saída de cobertura no terminal e criar a pasta `htmlcov/`.

```bash
pytest --cov=src --cov-report term-missing --cov-report html
```

## 📊 Relatório de Cobertura de Testes

Abaixo está o relatório de cobertura de testes, provando que todas as regras de negócio críticas do módulo `password_validator.py` foram validadas, atingindo **100% de cobertura**.

**[COLE SEU SCREENSHOT DE 100% AQUI]**

```
```