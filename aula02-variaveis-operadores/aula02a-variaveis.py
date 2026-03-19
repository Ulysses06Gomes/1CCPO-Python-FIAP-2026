# desafio 1
nome = input("Digite seu nome: ")
print(f"Bem-vindo, {nome}!")

# desafio 2
dia = int(input("Digite seu dia de nascimento: "))
mes = int(input("Digite seu mês de nascimento: "))
ano = int(input("Digite seu ano de nascimento: "))
print(f"Você nasceu no {dia}/{mes}/{ano}")

# desafio 3
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um segundo número inteiro: "))
soma = num1 + num2
print(f"O valor da soma é {soma}")

# exercicio 1
area = (3.14 * 5**2)
print(f"A área do circulo de raio 5 é de {area}")

# exercicio 2
fahren = int(input("Indique a temperatura em Fahrenheit: "))
celsius = (fahren - 32) * 5/9
print(f"A temperatura convertida de Fahrenheit para Celsius é de {celsius:.2f}")

# exercicio 3
celsiusNew = int(input("Indique a temperatura em Celsius: "))
fahrenNew = (celsiusNew * 9/5) + 32
print(f"A temperatura convertida de Fahrenheit para Celsius é de {fahrenNew:.2f}")

# exercicio 4
livro = int(25)
caneta = int(5)
gasto = (livro * 3) + (caneta * 2)
print(f"O gasto total na compra de 3 livros e 2 canetas é de {gasto}")

# exercicio 5
velocidade = int(60/3.6)
distancia = int(150*1000)
tempo = distancia/velocidade
print(f"O carro levou {tempo*60}h para percorrer a distância de 150km")
