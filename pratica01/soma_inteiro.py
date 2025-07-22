"""
Calculadora de Número Inteiro
Leia quatro valores inteiros A, B, C e D. 
A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D 
segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada: O arquivo de entrada contém 4 valores inteiros.
Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.
"""

numero_a = int(input("Digite o valor de A: "))
numero_b = int(input("Digite o valor de B: "))
numero_c = int(input("Digite o valor de C: "))
numero_d = int(input("Digite o valor de D: "))


diferenca = numero_a * numero_b - numero_c * numero_d


print("A fórmula para a diferença é (A * B) - (C * D)")
print(f"Substituindo os valores fornecidos: ({numero_a} * {numero_b}) - ({numero_c} * {numero_d})")
print(f"O resultado da diferença é DIFERENÇA = {diferenca}")
