def print_lyrics ():
    print("I ain't gonna live forever")
    print("I just want to live while I'm alive")

print_lyrics()

def boas_vindas(nome):
    print(f"\nOlá, {nome}! Seja bem-vindo!")

nome_digitado = input(("\nInsira seu nome: "))
boas_vindas(nome_digitado)

def soma(num1, num2):
    soma = num1 + num2
    return soma

resultado_soma = soma(17, 22)
print(resultado_soma)
