import re

class InvalidPasswordException(Exception):
    """Exceção customizada para senhas inválidas."""
    def __init__(self, message="A senha não atende aos requisitos de segurança."):
        self.message = message
        super().__init__(self.message)

def validate_password(password: str) -> bool:
    """
    Valida se a senha atende a todas as regras de segurança.
    Regras:
    1. Mínimo de 8 caracteres.
    2. Deve conter pelo menos uma letra maiúscula.
    3. Deve conter pelo menos uma letra minúscula.
    4. Deve conter pelo menos um número.
    5. Não pode ter espaços em branco.
    """
    if not isinstance(password, str):
        raise InvalidPasswordException("A entrada deve ser uma string.")

    if not password:
        raise InvalidPasswordException("A senha não pode ser nula ou vazia.")

    # 1. Mínimo de 8 caracteres
    if len(password) < 8:
        raise InvalidPasswordException("A senha deve ter no mínimo 8 caracteres.")

    # 2. Pelo menos uma maiúscula (Regex: olhar de A a Z)
    if not re.search(r"[A-Z]", password):
        raise InvalidPasswordException("A senha deve conter pelo menos uma letra maiúscula.")

    # 3. Pelo menos uma minúscula (Regex: olhar de a a z)
    if not re.search(r"[a-z]", password):
        raise InvalidPasswordException("A senha deve conter pelo menos uma letra minúscula.")

    # 4. Pelo menos um número (Regex: olhar de 0 a 9)
    if not re.search(r"[0-9]", password):
        raise InvalidPasswordException("A senha deve conter pelo menos um número.")

    # 5. Não pode ter espaços em branco (Regex: olhar por \s)
    if re.search(r"\s", password):
        raise InvalidPasswordException("A senha não pode conter espaços em branco.")

    return True


if __name__ == '__main__':
    
    try:
        if validate_password("Senha123Forte"):
            print("Senha validada com sucesso!")
    except InvalidPasswordException as e:
        print(f"Falha na validação: {e.message}")