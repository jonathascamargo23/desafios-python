def formatar_nome(nome):
    # Retorna o nome com a primeira letra de cada palavra em maiúsculo
    return ' '.join(palavra.capitalize() for palavra in nome.strip().split())

def validar_email(email):
    # Verifica se existe exatamente um '@'
    if email.count('@') != 1:
        return False

    # Divide o e-mail em duas partes
    usuario, dominio = email.split('@')

    # Verifica se há pelo menos um ponto após o '@'
    if '.' not in dominio:
        return False

    return True

def processar_cadastro(entrada):
    # Divide a entrada em nome e email
    if ', ' not in entrada:
        return 'Entrada inválida - ERRO'
    nome, email = entrada.split(', ', 1)
    nome_formatado = formatar_nome(nome)
    if validar_email(email):
        return f"{nome_formatado} - OK"
    else:
        return f"{nome_formatado} - ERRO"

# Entrada padrão
entrada = input()
print(processar_cadastro(entrada))
