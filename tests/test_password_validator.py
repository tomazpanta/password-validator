import pytest
import sys
import os

# Adiciona a pasta 'src' ao caminho de busca do Python APENAS para este teste
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from password_validator import validate_password, InvalidPasswordException
# Cenários de Sucesso (Happy Path)
def test_valid_password_success():
    """Testa uma senha que atende a todos os requisitos."""
    # Deve retornar True e não levantar exceção
    assert validate_password("SenhaF0rte123") is True

def test_valid_password_with_symbols_success():
    """Testa uma senha que usa caracteres especiais (o que é permitido)."""
    assert validate_password("P@sswOrd123!") is True

# ----------------------------------------------------------------------
# Cenários de Falha (Regras de Negócio e Exceções)
# ----------------------------------------------------------------------

# 1. Teste para Senha Nula ou Vazia
def test_empty_password_raises_exception():
    """Não deve permitir senha vazia."""
    with pytest.raises(InvalidPasswordException) as excinfo:
        validate_password("")
    assert "nula ou vazia" in str(excinfo.value)

def test_none_password_raises_exception():
    """Não deve permitir entrada que não seja string (nula)."""
    with pytest.raises(InvalidPasswordException) as excinfo:
        validate_password(None)
    assert "deve ser uma string" in str(excinfo.value)

# 2. Teste para Mínimo de 8 Caracteres
def test_short_password_raises_exception():
    """Não deve permitir menos de 8 caracteres."""
    with pytest.raises(InvalidPasswordException) as excinfo:
        validate_password("S3nhA") # 5 caracteres
    assert "mínimo 8 caracteres" in str(excinfo.value)

# 3. Teste para Falta de Letra Maiúscula
def test_no_uppercase_raises_exception():
    """A senha deve ter pelo menos uma letra maiúscula."""
    with pytest.raises(InvalidPasswordException) as excinfo:
        validate_password("senhafraca123")
    assert "letra maiúscula" in str(excinfo.value)

# 4. Teste para Falta de Letra Minúscula
def test_no_lowercase_raises_exception():
    """A senha deve ter pelo menos uma letra minúscula."""
    with pytest.raises(InvalidPasswordException) as excinfo:
        validate_password("SENHAFORTE123")
    assert "letra minúscula" in str(excinfo.value)

# 5. Teste para Falta de Número
def test_no_number_raises_exception():
    """A senha deve ter pelo menos um número."""
    with pytest.raises(InvalidPasswordException) as excinfo:
        validate_password("SenhaSemNumero")
    assert "pelo menos um número" in str(excinfo.value)

# 6. Teste para Espaços em Branco
def test_whitespace_raises_exception():
    """A senha não pode conter espaços em branco."""
    with pytest.raises(InvalidPasswordException) as excinfo:
        validate_password("S enha123")
    assert "espaços em branco" in str(excinfo.value)