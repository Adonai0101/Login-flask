import secrets
import string

def codigo_api_key():
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(secrets.choice(caracteres) for _ in range(15))
    return codigo

def codigo_verificacion_usuario():
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(secrets.choice(caracteres) for _ in range(6))
    return codigo

def codigo_password():
    return "passored"