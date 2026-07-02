#Atividade 1
numero = int(input("Digite um número: "))
dobro = numero * 2
print( " o dobro é", dobro)



#Atividade 2 verificando a idade
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")


#Atividade 3 média de notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print("Média:", media)
else:
    print("Média:", media)
    
    
#Atividade 4 contagem crescente
contagem = int(input("Para iniciar contagem ate 10 digite 1: "))
if contagem == 1:
    for i in range(1, 11):
        print(i)


#Atividade 5 calculadora simples
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print("Escolha a operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = int(input("Digite a opção desejada: "))

if opcao == 1:  
    resultado = num1 + num2
    print("Resultado:", resultado)
elif opcao == 2:
    resultado = num1 - num2
    print("Resultado:", resultado)
elif opcao == 3:
    resultado = num1 * num2
    print("Resultado:", resultado)
elif opcao == 4:
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado :", resultado)
    