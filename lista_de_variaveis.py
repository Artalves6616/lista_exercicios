#Arthur Santana Alves - ADM 
#Lista de Exercício sobre Variáveis

#1.	Crie uma variável nome e atribua seu nome a ela.
nome = "Arthur "


#2.	Crie uma variável idade e atribua sua idade a ela.
idade = 22

#3.	Crie uma variável altura e atribua sua altura (em metros) a ela.
altura = 1.78

#4.	Verifique o tipo de cada uma dessas variáveis usando a função type()
nome = "Arthur"
idade = 22
altura = 1.78

print(type(nome))   
print(type(idade))  
print(type(altura)) 


#5.	Crie duas variáveis a e b e atribua a elas os valores 5 e 3, respectivamente.
a = 5
b = 3


#6.	Calcule e imprima a soma, subtração, multiplicação, divisão e o resto da divisão (a % b)
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto_divisao = a % b

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Resto da divisão:", resto_divisao)


#7.	Crie duas variáveis x e y e atribua a elas os valores 10 e 20, respectivamente.
x=10
y=20


#8.	Troque os valores de x e y sem usar uma terceira variável temporária.
x = 10
y = 20

x, y = y, x  # Troca

print("Valor de x após a troca:", x)
print("Valor de y após a troca:", y)


#9.	Imprima os valores de x e y após a troca.
print("Valor final de x:", x)
print("Valor final de y:", y)


#10.Crie as variáveis primeiro_nome e sobrenome e atribua seus valores correspondentes.
primeiro_nome = "Seu Primeiro Nome"  
sobrenome = "Seu Sobrenome" 


#11.	Concatene essas variáveis em uma nova variável nome_completo com um espaço entre elas.
nome_completo = primeiro_nome + " " + sobrenome


#12. Imprima nome_completo.
print(nome_completo)


#13. Crie três variáveis nota1, nota2 e nota3 e atribua a elas notas de 0 a 10.
nota1 = 8.0  
nota2 = 7.5
nota3 = 9.0


#14. Calcule a média das três notas e armazene o resultado em uma variável media.
media = (nota1 + nota2 + nota3) / 3


#15.Imprima a média.
print(media)


#16.Peça ao usuário para inserir seu nome e armazene em uma variável nome_usuario.
nome_usuario = input("Por favor, insira seu nome: ")

#17.Peça ao usuário para inserir sua idade e armazene em uma variável idade_usuario.
idade_usuario = input("Por favor, insira sua idade: ")

#18.Imprima uma mensagem saudando o usuário e informando sua idade.
print(f"Olá, {nome_usuario}! Você tem {idade_usuario} anos.")

#19.Crie uma variável numero_str e atribua a ela o valor "123".
numero_str = "123"

