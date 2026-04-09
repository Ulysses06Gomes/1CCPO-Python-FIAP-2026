verifica_email = True
verifica_senha = True

login = verifica_email and verifica_senha
print(login)

if login:
    print("Entra no sistema")

if not login:
    print("Não entra no sistema")